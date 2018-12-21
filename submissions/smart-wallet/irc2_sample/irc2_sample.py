from iconservice import *

TAG = 'IRC2Sample'


class TokenContractInterface(InterfaceScore):
    @interface
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        pass


class IRC2Sample(IconScoreBase):

    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _value: int, _data: bytes):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._balance = DictDB("Balance", db, int, 1)

    def on_install(self) -> None:
        super().on_install()
        self._balance[self.msg.sender] = 100_000_000_000

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"

    @external
    def transfer(self, _to: Address, _value: int, _data: bytes = None):
        if _data is None:
            _data = b"None"

        if self._balance[self.msg.sender] < _value:
            revert("balance is low")
        self._balance[_to] = self._balance[_to] + _value
        self._balance[self.msg.sender] = self._balance[self.msg.sender] - _value
        self.Transfer(self.msg.sender, _to, _value, _data)
