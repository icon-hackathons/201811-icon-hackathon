from iconservice import *

TAG = 'WithUManager'


class IToken(InterfaceScore):
    @interface
    def transfer(self, _to: Address, _value: int, _data: bytes=None):
        pass


class Users:
    _USER_ADDRESSES = 'user_addresses'
    _SCORE_ADDRESSES = 'score_addresses'

    @property
    def user_addresses(self) -> ArrayDB:
        return ArrayDB(self._USER_ADDRESSES, self.__db, value_type=Address)

    def __init__(self, db: IconScoreDatabase):
        self.__db = db
        self._score_addresses = DictDB(self._SCORE_ADDRESSES, db, value_type=Address)

    def __setitem__(self, user_address: Address, score_address: Address):
        if user_address not in self._score_addresses:
            self.user_addresses.put(user_address)

        self._score_addresses[user_address] = score_address

    def __getitem__(self, user_address: Address):
        return self._score_addresses[user_address]

    def __delitem__(self, user_address: Address):
        # delete does not actually do delete but set zero
        if user_address in self._score_addresses:
            self._score_addresses.remove(user_address)

    def __contains__(self, user_address: Address):
        return user_address in self._score_addresses

    def __iter__(self):
        return self.user_addresses.__iter__()

    def __len__(self):
        return self.user_addresses.__len__()

    def items(self):
        for user_address in self.user_addresses:
            yield (user_address, self._score_addresses[user_address])


class TokenManager:
    _TOKEN_ADDRESS = 'token_address'

    def __init__(self, db: IconScoreDatabase, from_score: 'IconScoreBase'):
        self.__db = db
        self.__icon_score_base = from_score
        self._token_address = VarDB(self._TOKEN_ADDRESS, db, value_type=Address)

    def set_token_address(self, token_address):
        self._token_address.set(token_address)

    def get_token_address(self) -> Address:
        return self._token_address.get()

    def _get_token_score(self) -> IToken:
        return self.__icon_score_base.create_interface_score(self._token_address.get(), IToken)

    def distribute(self, account: Address, amount: int):
        token_score = self._get_token_score()
        token_score.transfer(account, amount, b'called from WeddingManager')


class WithUManager(IconScoreBase):

    __SCORE_VERSION = 'v0.1'

    _WEDDINGS = 'weddings'
    _WEDDING_SCORE_CODE = 'wedding_score_code'
    _EXCHANGE_RATE = 'exchange_rate'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.__db = db
        self._users = Users(db)
        self._token_manager = TokenManager(db, self)
        self._wedding_score_code = VarDB(self._WEDDING_SCORE_CODE, db, value_type=bytes)
        self._exchange_rate = VarDB(self._EXCHANGE_RATE, db, value_type=int)

    def on_install(self, token_score: Address, exchange_rate: int) -> None:
        super().on_install()
        self._token_manager.set_token_address(token_score)
        self._exchange_rate.set(exchange_rate)

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_wedding_score_address(self, owner: Address) -> str:
        if self._users[owner]:
            return self._users[owner]
        return "cx"

    @external(readonly=True)
    def get_token_address(self) -> Address:
        return self._token_manager.get_token_address()

    @external
    def set_wedding_score_address_from_contract(self, wedding_score: Address):
        if self.msg.sender.is_contract:
            origin = self.get_owner(self.msg.sender)
            self._users[origin] = wedding_score

    @external
    def set_wedding_score_address(self, wedding_score: Address, address: Address):
        self._precondition(not self.msg.sender.is_contract)
        self._precondition(self.msg.sender == self.get_owner(wedding_score))
        self._users[address] = wedding_score

    @external(readonly=True)
    def get_users(self, offset: int, count: int) -> list:
        result = []
        count_of_users = len(self._users)
        if 0 < count <= self.get_max_iteration() and 0 <= offset < count_of_users:
            if offset + count > count_of_users:
                count = count_of_users - offset
            for i in range(count):
                user_address = self._users.user_addresses[offset + i]
                user_score = self._users[user_address]
                result.append({
                    "user_address" : user_address,
                    "user_score" : user_score
                })
        return result

    @external(readonly=True)
    def get_wedding_score_code(self) -> bytes:
        return self._wedding_score_code.get()

    @external
    def set_wedding_score_code(self, wedding_score_code: bytes):
        self._precondition(self.msg.sender == self.owner)
        self._wedding_score_code.set(wedding_score_code)

    @external
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        self._precondition(self.msg.sender == self._token_manager.get_token_address(),
                           "Unknown token address")
        Logger.debug(f'tokenFallback: token supply = "{_value}"')

    @payable
    def fallback(self):
        wedding_score_address = self._users[self.msg.sender]
        self._precondition(wedding_score_address is not None, 'There is none wedding score address')
        Logger.debug(f'>>>>>>>>>>>>>>> wedding_score_address = "{wedding_score_address}"')
        amount = self.msg.value
        distribute_amount = self._get_rated_amount(amount, self._exchange_rate.get())
        self._token_manager.distribute(wedding_score_address, distribute_amount)

    @external(readonly=True)
    def get_max_iteration(self) -> int:
        """

        :return: max iteration
        """
        return 1000

    @staticmethod
    def _get_rated_amount(amount: int, rate: int) -> int:
        """

        :param amount: amount (don't care unit)
        :param rate: rate in millions
        :return:
        """
        if amount <= 0:
            return 0
        else:
            return amount * rate // 10 ** 6

    def _precondition(self, condition: bool, message: str = None):
        """

        :param condition: condition
        :param message: message
        :return: none
        """
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)
