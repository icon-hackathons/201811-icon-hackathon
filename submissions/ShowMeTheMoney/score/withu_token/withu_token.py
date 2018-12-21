from iconservice import *

TAG = 'WithUToken'


class IconTokenStandard(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def decimals(self) -> int:
        pass

    @abstractmethod
    def totalSupply(self) -> int:
        pass

    @abstractmethod
    def balanceOf(self, _owner: Address) -> int:
        pass

    @abstractmethod
    def transfer(self, _to: Address, _value: int, _data: bytes = None):
        pass


class TokenFallbackInterface(InterfaceScore):
    @interface
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        pass


EOA_ZERO = Address.from_string('hx' + '0' * 40)


class WithUToken(IconScoreBase, IconTokenStandard):

    __SCORE_VERSION = 'v0.1'

    _NAME = 'name'
    _SYMBOL = 'symbol'
    _TOTAL_SUPPLY = 'total_supply'
    _DECIMALS = 'decimals'
    _BALANCES = 'balances'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._name = VarDB(self._NAME, db, str)
        self._symbol = VarDB(self._SYMBOL, db, str)
        self._total_supply = VarDB(self._TOTAL_SUPPLY, db, int)
        self._decimals = VarDB(self._DECIMALS, db, int)
        self._balances = DictDB(self._BALANCES, db, int)

    def on_install(self, name: str, symbol: str, amount: int, decimals: int) -> None:
        super().on_install()
        self._precondition(0 <= amount, "Initial supply cannot be less than zero")
        self._precondition(0 <= decimals <= 20)
        total_supply = amount * 10 ** decimals
        self._name.set(name)
        self._symbol.set(symbol)
        self._total_supply.set(total_supply)
        self._decimals.set(decimals)
        self._balances[self.owner] = total_supply

    def on_update(self) -> None:
        super().on_update()

    def _precondition(self, condition: bool, message: str=None):
        """

        :param condition: condition
        :param message: message
        :return: none
        """
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)

    @external(readonly=True)
    def name(self) -> str:
        return self._name.get()

    @external(readonly=True)
    def symbol(self) -> str:
        return self._symbol.get()

    @external(readonly=True)
    def decimals(self) -> int:
        return self._decimals.get()

    @external(readonly=True)
    def totalSupply(self) -> int:
        return self._total_supply.get()

    @external(readonly=True)
    def balanceOf(self, _owner: Address) -> int:
        return self._balances[_owner]

    @external
    def transfer(self, _to: Address, _value: int, _data: bytes = None):
        Logger.debug(f'Transfer({self.msg.sender}, {_to}, {_value}, {_data})', TAG)
        self._precondition(_value > 0, "Transferring value cannot be less than zero")
        self._precondition(_value <= self._balances[self.msg.sender], "Out of balance")
        data = b'None' if _data is None else _data
        self._balances[self.msg.sender] -= _value
        self._balances[_to] += _value

        if _to.is_contract:
            recipient_score = self.create_interface_score(_to, TokenFallbackInterface)
            recipient_score.tokenFallback(self.msg.sender, _value, _data)

        self.Transfer(self.msg.sender, _to, _value, data)

    @external
    def mint(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(amount > 0)
        self._balances[self.owner] += amount
        self._total_supply.set(self._total_supply.get() + amount)

        self.Transfer(EOA_ZERO, self.owner, amount, b'mint')

    @external
    def burn(self, account: Address, amount: int):
        self._precondition(self.msg.sender == self.owner)

        distribute_amount = self._balances[account]
        total_supply = self._total_supply.get()

        self._precondition(0 < amount <= distribute_amount <= total_supply)
        self._balances[account] = distribute_amount - amount
        self._total_supply.set(total_supply - amount)

        self.Transfer(account, EOA_ZERO, amount, b'burn')

    @external(readonly=True)
    def version(self) -> str:
        return self.__SCORE_VERSION

    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _value: int, _data: bytes):
        pass

    @eventlog(indexed=1)
    def EventReturned(self, account: Address, amount: int):
        pass