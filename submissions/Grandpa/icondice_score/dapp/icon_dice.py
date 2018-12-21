from iconservice import *


class IconDice(IconScoreBase):

    ICX_DECIMALS = 10 ** 18
    TICKET_PRICE = 1 * ICX_DECIMALS
    LIMIT_MEMBER = 2
    EXPIRED_BLOCK = 50

    @eventlog
    def GameResult(self, addr1: Address, addr2: Address, ran1: int, ran2: int): pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._deposit = DictDB("deposit", db, value_type=int)
        self._stake_deposit = DictDB("stake_deposit", db, value_type=int)

        self._game_sha = DictDB("game", db, value_type=bytes, depth=2)
        self._game_seed = DictDB("game_seed", db, value_type=bytes, depth=2)
        self._game_block = DictDB("game_block", db, value_type=int)
        self._game_member = DictDB("game_member", db, value_type=int)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_deposit(self, addr: Address) -> int:
        return self._deposit[addr]

    @external(readonly=True)
    def get_enable_withdraw(self, addr: Address) -> int:
        return self._deposit[addr] - self._stake_deposit[addr]

    @external(readonly=True)
    def can_start_game(self, addr: Address) -> bool:
        return self._deposit[addr] - self._stake_deposit[addr] >= self.TICKET_PRICE

    @payable
    @external
    def pay_advance(self) -> None:
        if self.msg.value != self.TICKET_PRICE:
            revert("invalid ticket_price")

        balance = self._deposit[self.msg.sender]
        balance += self.msg.value
        self._deposit[self.msg.sender] = balance

    @external
    def start_game(self, game_id: bytes, sha_key: bytes) -> None:
        account = self._deposit[self.msg.sender]
        stake_account = self._stake_deposit[self.msg.sender]

        if account - stake_account < self.TICKET_PRICE:
            revert("have to pay deposit")

        member_count = self._game_member[game_id]
        if member_count >= self.LIMIT_MEMBER:
            revert("full member")

        if self._game_sha[game_id][self.msg.sender] is not None:
            revert("duplicated address")

        stake_account += self.TICKET_PRICE
        self._stake_deposit[self.msg.sender] = stake_account

        self._game_sha[game_id][self.msg.sender] = sha_key
        self._game_member[game_id] += 1

        prev_block_height = self._game_block[game_id]
        if prev_block_height < self.block_height:
            self._game_block[game_id] = self.block_height

    @external
    def reveal_game(self, game_id: bytes, seed_key: bytes) -> None:
        if self._game_sha[game_id][self.msg.sender] is None:
            revert("have to start")

        new_sha_key = sha3_256(seed_key)
        prev_sha_key = self._game_sha[game_id][self.msg.sender]
        if prev_sha_key != new_sha_key:
            revert("mismatch key")

        self._game_seed[game_id][self.msg.sender] = seed_key

        prev_block_height = self._game_block[game_id]
        if prev_block_height < self.block_height:
            self._game_block[game_id] = self.block_height

    @external
    def end_game(self, game_id: bytes, addr1: Address, addr2: Address) -> None:
        if self._stake_deposit[addr1] < self.TICKET_PRICE:
            revert("less stake account")

        addr1_sha = self._game_sha[game_id][addr1]
        addr2_sha = self._game_sha[game_id][addr2]
        addr1_seed = self._game_seed[game_id][addr1]
        addr2_seed = self._game_seed[game_id][addr2]

        if addr1_sha and addr2_sha and addr1_seed and addr2_seed:
            # valid!
            ran_seed_src1 = addr1_seed + addr2_seed + addr1.to_bytes()
            ran_seed_src1 = sha3_256(ran_seed_src1)
            ran_num1 = int(bytes.hex(ran_seed_src1), 16) % 6 + 1

            ran_seed_src2 = addr2_seed + addr1_seed + addr2.to_bytes()
            ran_seed_src2 = sha3_256(ran_seed_src2)
            ran_num2 = int(bytes.hex(ran_seed_src2), 16) % 6 + 1

            for _ in range(50):
                if ran_num1 != ran_num2:
                    break
                ran_seed_src1 = sha3_256(ran_seed_src1)
                ran_num1 = int(bytes.hex(ran_seed_src1), 16) % 6 + 1

            if ran_num1 > ran_num2:
                self._winner_send_icx(addr1, addr2, self.TICKET_PRICE)
            elif ran_num1 < ran_num2:
                self._winner_send_icx(addr2, addr1, self.TICKET_PRICE)
            else:
                revert("not implement")

            self.GameResult(addr1, addr2, ran_num1, ran_num2)
        else:
            # invlid!
            game_block = self._game_block[game_id]
            if game_block < self.block_height + self.EXPIRED_BLOCK:
                revert("not expired")

            if addr1_sha and addr1_seed:
                self._winner_send_icx(addr1, addr2, self.TICKET_PRICE)
            elif addr2_sha and addr2_seed:
                self._winner_send_icx(addr2, addr1, self.TICKET_PRICE)

    def _winner_send_icx(self, win: Address, lose: Address, ticket_price: int) -> None:
        self._deposit[win] += ticket_price
        self._deposit[lose] -= ticket_price

        self._stake_deposit[win] -= ticket_price
        self._stake_deposit[lose] -= ticket_price

    @external
    def withdraw(self):
        amount = self._deposit[self.msg.sender] - self._stake_deposit[self.msg.sender]
        self._deposit[self.msg.sender] -= amount
        self.icx.send(self.msg.sender, amount)

    @payable
    def fallback(self) -> None:
        print("fallback!!")
