from iconservice import *

TAG = 'CryptoCave'

class CryptoBearsInterface(InterfaceScore):

    @interface
    def createCryptoBear(self):
        pass

class CryptoCave(IconScoreBase):

    _ONE_ICX = 1
    _BLOCK_CHECK = 'block_check'
    _INTERFACE_SCORE = 'interface_score'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._block_check = DictDB(self._BLOCK_CHECK, db, value_type=int)
        self._interface_score = VarDB(self._INTERFACE_SCORE, db, value_type=Address)

    def on_install(self, _score: Address) -> None:
        super().on_install()
        self._interface_score.set(_score)

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def name(self) -> str:
        return 'CryptoCave'

    @payable
    @external
    def createCryptoBear(self):
        if self.msg.value < self._ONE_ICX:
            Logger.info(f'need at least 1 ICX to create a CryptoBear', TAG)
            revert("need at least 1 ICX to create a CryptoBear")
        else:
            self.icx.transfer(self.msg.sender, self.msg.value - self._ONE_ICX)

        if self._block_check[self.msg.sender] == 0 or self._block_check[self.msg.sender] + 30 < self.block_height :
            self._block_check[self.msg.sender] = self.block_height
        else:
            Logger.info(f'Please wait for 30 blocks to be created before requesting again', TAG)
            revert('Please wait for 30 blocks to be created before requesting again')

        bearDNA = self._createBearDNA(self._block_check[self.msg.sender])

        bearSCORE = self.create_interface_score(self._interface_score.get(), CryptoBearsInterface)
        bearSCORE.createCryptoBear(bearDNA, self.msg.sender)

    def _createBearDNA(self, _block_height: int) -> int:
        bearDNA = self.msg.sender.to_bytes() + str(_block_height).encode()
        return int.from_bytes(sha3_256(bytes(bearDNA)), 'big')