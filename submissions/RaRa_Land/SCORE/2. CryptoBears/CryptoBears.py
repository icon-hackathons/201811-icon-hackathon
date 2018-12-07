from iconservice import *

TAG = 'CryptoBear'

class BattleScoreInterface(InterfaceScore):

    @interface
    def enroll(self, _participant: Address, _nonce: int):
        pass

class CryptoBear(IconScoreBase):

    _ZERO_ADDRESS = 'cx0000000000000000000000000000000000000000'
    _ONE_ICX = 1
    _TOKEN_LIST = 'token_list'
    _TOKEN_ID = 'token_id'
    _TOKEN_OWNER = 'token_owner'
    _TOKEN_APPROVED = 'token_approved'
    _BEAR_LEVEL = 'bear_level'

    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _tokenId: int):
        pass

    @eventlog(indexed=3)
    def Approval(self, _owner: Address, _approved: Address, _tokenId: int):
        pass

    def __init__(self, db: IconScoreDatabase, _tokenId = None) -> None:
        super().__init__(db)
        self._bear_level = DictDB(self._BEAR_LEVEL, db, value_type=int)
        self._token_list = ArrayDB(self._TOKEN_LIST, db, value_type=int)
        self._token_owner = DictDB(self._TOKEN_OWNER, db, value_type=Address)
        self._token_id = DictDB(self._TOKEN_ID, db, value_type=str)
        self._token_approved = DictDB(self._TOKEN_APPROVED, db, value_type=Address)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def name(self) -> str:
        return 'CryptoBears'

    @external(readonly=True)
    def symbol(self) -> str:
        return 'CBT'

    @external(readonly=True)
    def balanceOf(self, _owner: Address) -> int:
        if _owner == self._ZERO_ADDRESS:
            raise IconScoreException("balanceOf : zero address is not allowed")

        balance = 0
        for iterator in self._token_list:
            if self._token_owner[iterator] == _owner:
                balance += 1
        return balance

    @external(readonly=True)
    def ownerOf(self, _tokenId: int) -> Address:
        if _tokenId in self._token_list:
            return self._token_owner[_tokenId]
        else:
            raise IconScoreException("ownerOf : Can't find the token which has the value of _tokenId")

    @external(readonly=True)
    def getApproved(self, _tokenId: int) -> Address:

        if _tokenId in self._token_list:
            return self._token_approved[_tokenId]
        else:
            raise IconScoreException("getApproved : Can't find the token which has the value of _tokenId")


    @external
    def approve(self, _to: Address, _tokenId: int):

        if self._token_owner[_tokenId] != self.msg.sender:
            raise IconScoreException("approve : sender does not own token")

        self._token_approved[_tokenId] = _to
        self.Approval(self.msg.sender, _to, _tokenId)

    @external
    def enrollBattle(self, _score: Address, _nonce: int):
        self.approve(_score, self.getTokenId(self.msg.sender, 0))

        battelSCORE = self.create_interface_score(_score, BattleScoreInterface)
        battelSCORE.enroll(self.msg.sender, _nonce)

    @external
    def transfer(self, _to: Address, _tokenId: int):
        if self._token_owner[_tokenId] != self.msg.sender:
            raise IconScoreException("transfer : sender does not own token")

        elif _tokenId not in self._token_list:
            raise IconScoreException("transfer : sender does not own token")

        elif _to == Address.from_string(self._ZERO_ADDRESS):
            raise IconScoreException("transfer : zero address is not allowed")

        self._token_owner[_tokenId] = _to
        self._token_approved[_tokenId] = _to
        self.Transfer(self.msg.sender, _to, _tokenId)

    @external
    def transferFrom(self, _from: Address, _to: Address, _tokenId: int):
        if self._token_owner[_tokenId] != _from:
            raise IconScoreException("transferFrom : _from does not own token")

        elif self.getApproved(_tokenId) != self.msg.sender and self._token_owner[_tokenId] != self.msg.sender:
            raise IconScoreException("transferFrom : msg.sender is not allowed of transferring")

        elif _tokenId not in self._token_list:
            raise IconScoreException("transferFrom : sender does not own token")

        elif _to == Address.from_string(self._ZERO_ADDRESS):
            raise IconScoreException("transferFrom : zero address is not allowed")

        self._token_owner[_tokenId] = _to
        del self._token_approved[_tokenId]
        self.Transfer(_from, _to, _tokenId)

    @external
    def createCryptoBear(self, _bearDNA: bytes, _address: Address):
        if self.msg.sender.is_contract:
            self._createCryptoBear(_bearDNA, _address)
        else:
            revert("You can only create CryptoBear via CryptoCave's method")

    def _createCryptoBear(self, _bearDNA: bytes, _address: Address):

        if self._token_id[_address] == "":
            tokenIdList = list()
        else:
            tokenIdList = json_loads(self._token_id[_address])

        tokenIdList.append(_bearDNA)
        self._token_list.put(_bearDNA)
        self._token_id[_address] = json_dumps(tokenIdList)
        self._token_owner[_bearDNA] = _address
        self._token_approved[_bearDNA] = _address
        self._bear_level[_bearDNA] = 0

    @external(readonly=True)
    def getTokenId(self, _address: Address, index: int) -> int:
        if self._token_id[_address] == "":
            raise IconScoreException("_address has no token")
        else:
            tokenIdList = list(json_loads(self._token_id[_address]))[index]
            return tokenIdList

    @payable
    @external
    def happyMeal(self, _index: int):
        if self.msg.value < self._ONE_ICX :
            revert("need at least 1 ICX to feed a CryptoBear")
        else:
            self.icx.send(self.msg.sender, self.msg.value - self._ONE_ICX)

        tokenId = list(json_loads(self._token_id[self.msg.sender]))[_index]
        if self._bear_level == 10:
            revert("Can grow up to MAX LEVEL 10")
        self._bear_level[tokenId] += 1

    @external(readonly=True)
    def getBearLevel(self, _tokenId: int) -> int:
        return self._bear_level[_tokenId]
