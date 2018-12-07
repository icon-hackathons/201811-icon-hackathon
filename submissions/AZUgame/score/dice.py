from iconservice import *

TAG = 'DiceScore'

ROLL_FAILED = 0
ROLL_SUCCESS = 1

BET_ACTIVE = 0
BET_DONE = 1


class DiceScore(IconScoreBase):

    __SCORE_VERSION = 'v1.0.0'

    @property
    def _bet__account(self) -> ArrayDB:
        return ArrayDB('bet.account', self.db, Address)

    @property
    def _bet__amount(self) -> ArrayDB:
        return ArrayDB('bet.amount', self.db, int)

    @property
    def _bet__roll_under(self) -> ArrayDB:
        return ArrayDB('bet.roll_under', self.db, int)

    @property
    def _bet__dividend(self) -> ArrayDB:
        return ArrayDB('bet.dividend', self.db, int)

    @property
    def _bet__house_hash(self) -> ArrayDB:
        return ArrayDB('bet.house_hash', self.db, str)

    @property
    def _bet__player_seed(self) -> ArrayDB:
        return ArrayDB('bet.player_seed', self.db, str)

    @property
    def _bet__is_active(self) -> ArrayDB:
        return ArrayDB('bet.is_active', self.db, int)

    @property
    def _bet__timestamp(self) -> ArrayDB:
        return ArrayDB('bet.timestamp', self.db, int)

    def __init__(self, db: IconScoreDatabase):
        """

        :param db:
        """
        super().__init__(db)

        # CONTEXT
        self._context__roll_under_min = VarDB('context.roll_under_min', db, int)
        self._context__roll_under_max = VarDB('context.roll_under_max', db, int)
        self._context__bet_min = VarDB('context.bet_min', db, int)
        self._context__bet_max = VarDB('context.bet_max', db, int)

        # PLAYER_INFO
        self._player__available_amount = DictDB('player.bet_available_amount', db, int)

    def on_install(self,
                   roll_under_min: int,
                   roll_under_max: int,
                   bet_min: int,
                   bet_max: int):
        """

        :param roll_under_min: minimum value of roll_under
        :param roll_under_max: maximum value of roll_under
        :param bet_min: minimum betting amount
        :param bet_max: maximum betting amount
        :return: none
        """
        super().on_install()
        self._precondition(roll_under_max > 0)
        self._precondition(roll_under_max >= roll_under_min >= 0)
        self._precondition(bet_max >= bet_min >= 0)

        self._context__roll_under_min.set(roll_under_min)
        self._context__roll_under_max.set(roll_under_max)
        self._context__bet_min.set(bet_min)
        self._context__bet_max.set(bet_max)

    def on_update(self) -> None:
        """

        :return: none
        """
        super().on_update()

    # ==================================================================================================================
    # FALLBACK
    # ==================================================================================================================

    @payable
    def fallback(self):
        """

        :return: none
        """
        account = self.msg.sender
        amount = self.msg.value

        # EXECUTE
        self._player__available_amount[account] += amount

        # EVENT
        self.event_transfer(account, amount, self._player__available_amount[account])

    # ==================================================================================================================
    # API
    # ==================================================================================================================

    @external(readonly=True)
    def info(self) -> dict:
        """

        :return: score info values
        """
        return {
            'score_version': self.__SCORE_VERSION,
            'roll_under_min': self._context__roll_under_min.get(),
            'roll_under_max': self._context__roll_under_max.get(),
            'bet_min': self._context__bet_min.get(),
            'betMax': self._context__bet_max.get()
        }

    @external(readonly=True)
    def get_available_amount(self, account: Address) -> int:
        """

        :param account: player address
        :return: player's available amount
        """
        return self._player__available_amount[account]

    @external
    def withdraw(self, amount: int):
        """

        :param amount: requested amount to withdraw
        :return: none
        """
        account = self.msg.sender

        # PRECONDITION
        self._precondition(account == self.owner, 'Not owner of this score')
        self._precondition(0 < amount <= self.icx.get_balance(self.address))

        # EXECUTE
        self.icx.transfer(account, amount)

        # EVENT
        self.event_withdraw(amount)

    @external
    def safe_withdraw(self, account: Address, amount: int):
        """

        :param account: player address
        :param amount: requested amount to withdraw
        :return:
        """
        # PRECONDITION
        self._precondition(0 < amount <= self.icx.get_balance(self.address))
        self._precondition(amount > self._player__available_amount[account])

        # EXECUTE
        self.icx.transfer(account, amount)
        self._player__available_amount[account] -= amount

        # EVENT
        self.event_safe_withdraw(account, amount)

    @external
    def bet(self, amount: int, roll_under: int, house_hash: str, player_seed: str):
        """

        :param amount: requested amount to bet
        :param roll_under: value of roll_under
        :param house_hash: value of hash from house_seed
        :param player_seed: value of player_seed
        :return: none
        """
        account = self.msg.sender
        available_amount = self._player__available_amount[account]

        # PRECONDITION
        self._precondition(0 < amount <= available_amount, f'Invalid amount')
        self._precondition(self._context__bet_max.get() >= amount >= self._context__bet_min.get(), 'Invalid amount')
        self._precondition(self._context__roll_under_max.get() >= roll_under >= self._context__roll_under_min.get(),
                           'Invalid roll under')

        # EXECUTE
        index = len(self._bet__account)
        dividend = amount * 98 // (roll_under - 1)

        self._bet__account.put(account)
        self._bet__amount.put(amount)
        self._bet__roll_under.put(roll_under)
        self._bet__house_hash.put(house_hash)
        self._bet__player_seed.put(player_seed)
        self._bet__is_active.put(BET_ACTIVE)
        self._bet__timestamp.put(self.now())
        self._bet__dividend.put(dividend)

        # EVENT
        self.event_bet(str(index), account, amount)

    @external(readonly=True)
    def get_bets_size(self) -> int:
        """

        :return: count of all bets
        """
        return len(self._bet__account)

    @external(readonly=True)
    def get_bet(self, index: int) -> dict:
        """

        :param index:
        :return:
        """
        return {
            'account': self._bet__account.get(index),
            'amount': self._bet__amount.get(index),
            'roll_under': self._bet__roll_under.get(index),
            'house_hash': self._bet__house_hash.get(index),
            'player_seed': self._bet__player_seed.get(index),
            'active': self._bet__is_active.get(index),
            'timestamp': self._bet__timestamp.get(index),
            'dividend': self._bet__dividend.get(index)
        }

    @external
    def roll(self, index: int, house_seed: str):
        """

        :param index: value of bet index
        :param house_seed: value of house_seed
        :return: none
        """
        # PRECONDITION
        self._precondition(self.msg.sender == self.owner, 'Not owner of this score')
        self._precondition(self._bet__is_active.get(index) == BET_ACTIVE, 'Bet had been rolled already')
        self._precondition(self._bet__house_hash.get(index) == self._get_hash(house_seed).hex(), 'Incorrect house seed')

        # EXECUTE
        result = ROLL_FAILED

        account = self._bet__account.get(index)
        dividend = self._bet__dividend.get(index)
        roll_under = self._bet__roll_under.get(index)
        player_seed = self._bet__player_seed.get(index)
        dice_number = self._compute_random_roll(house_seed, player_seed)

        self._player__available_amount[account] -= self._bet__amount.get(index)

        if dice_number < roll_under:
            result = ROLL_SUCCESS
            self._player__available_amount[account] += dividend
            self.event_roll_success(str(index), account, dividend)

        self._bet__is_active[index] = BET_DONE

        # EVENT
        self.event_roll(str(index), str(result))

    @external
    def get_hash_from_str(self, content: str) -> str:
        """

        :param content: content to be hashed
        :return: str hash from str content
        """
        return self._get_hash(content).hex()

    def _get_hash(self, content: str) -> bytes:
        """

        :param content: content to be hashed
        :return: bytes hash from str content
        """
        return sha3_256(self._to_bytes(content))

    def _compute_random_roll(self, house_seed: str, player_seed: str) -> int:
        """

        :param house_seed: one of seeds to compute random roll from owner
        :param player_seed: one of seeds to compute random roll from player
        :return: generate integer from 1 to 100 from house seed and player seed
        """
        return int.from_bytes(self._get_hash(house_seed + player_seed), 'big') % 100 + 1

    # ==================================================================================================================
    # STATIC METHOD
    # ==================================================================================================================

    @staticmethod
    def _to_bytes(content: str):
        if isinstance(content, str):
            value = content.encode()
        else:
            value = content
        return value

    # ==================================================================================================================
    # EXCEPTION
    # ==================================================================================================================

    def _precondition(self, condition: bool, message: str=None):
        """

        :param condition: if revert
        :param message: cause by
        :return: none
        """
        if not condition:
            self.revert(f'PRECONDITION FAILED' if message is None else message)

    # ==================================================================================================================
    # EVENT
    # ==================================================================================================================

    @eventlog(indexed=3)
    def event_transfer(self, account: Address, amount: int, available_amount: int):
        pass

    @eventlog(indexed=3)
    def event_bet(self, index: str, account: Address, amount: int):
        pass

    @eventlog(indexed=2)
    def event_roll(self, index: str, result: str):
        pass

    @eventlog(indexed=3)
    def event_roll_success(self, index: str, account: Address, dividend: int):
        pass

    @eventlog(indexed=1)
    def event_withdraw(self, amount: int):
        pass

    @eventlog(indexed=2)
    def event_safe_withdraw(self, account: Address, amount: int):
        pass
