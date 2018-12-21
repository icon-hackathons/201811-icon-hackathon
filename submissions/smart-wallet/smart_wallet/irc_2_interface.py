from iconservice import InterfaceScore, interface, Address


class IRC2Interface(InterfaceScore):

    @interface
    def name(self) -> str:
        pass

    @interface
    def symbol(self) -> str:
        pass

    @interface
    def decimals(self) -> int:
        pass

    @interface
    def totalSupply(self) -> int:
        pass

    @interface
    def balanceOf(self, _owner: Address) -> int:
        pass

    @interface
    def transfer(self, _to: Address, _value: int, _data: bytes = None):
        pass

    @interface
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        pass
