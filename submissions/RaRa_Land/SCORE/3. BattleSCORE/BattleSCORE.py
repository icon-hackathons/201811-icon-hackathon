from iconservice import *

TAG = 'Battle'

class CryptoBearsinterface(InterfaceScore):

    @interface
    def transferFrom(self, _from: Address, _to: Address, _tokenId: int):
        pass

    @interface
    def getTokenId(self):
        pass

    @interface
    def balanceOf(self, _owner: Address):
        pass

    @interface
    def getBearLevel(self, _tokenId):
        pass

class Battle(IconScoreBase):

    _PARTICIPANT = 'participant'
    _NONCE = 'nonce'
    _INTERFACE_SCORE = 'interface_score'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._participant = ArrayDB(self._PARTICIPANT, db, value_type=Address)
        self._nonce = DictDB(self._PARTICIPANT, db, value_type=int)
        self._interface_score = VarDB(self._INTERFACE_SCORE, db, value_type=Address)

    def on_install(self, _score: Address) -> None:
        super().on_install()
        self._interface_score.set(_score)

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def name(self) -> str:
        return 'BattleSCORE'

    @external
    def enroll(self, _participant: Address, _nonce: int):
        if self.msg.sender.is_contract :
            bearsScore = self.create_interface_score(self._interface_score.get(), CryptoBearsinterface)
            if bearsScore.balanceOf(_participant) < 1 :
                Logger.info(f'need at least 1 Token to join the battle', TAG)
                revert('out of balance')

            self._participant.put(_participant)

            if len(self._participant) == 2:
                self._battle(self._participant.pop(), self._participant.pop())
        else:
            revert("You can only use enroll via CryptoBears' method")

    def _battle(self, player1: Address, player2: Address):
        bearsScore = self.create_interface_score(self._interface_score.get(), CryptoBearsinterface)

        p1 = self._getRandomValue(player1)
        p2 = self._getRandomValue(player2)

        while(p1 == p2):
            self._nonce[player1] += 1
            self._nonce[player2] += 1
            p1 = self._getRandomValue(player1)
            p2 = self._getRandomValue(player2)

        if p1 > p2:
            Logger.debug("player1 WIN!!!", TAG)
            bearsScore.transferFrom(player2, player1, bearsScore.getTokenId(player2, 0))
        else:
            Logger.debug("player2 WIN!!!", TAG)
            bearsScore.transferFrom(player1, player2, bearsScore.getTokenId(player1, 0))

    def _getRandomValue(self, player: Address):
        bearsScore = self.create_interface_score(self._interface_score.get(), CryptoBearsinterface)

        result = int.from_bytes(sha3_256(player.to_bytes() + str(self._nonce[player]).encode()), 'big') % 100
        return result + bearsScore.getBearLevel(0)