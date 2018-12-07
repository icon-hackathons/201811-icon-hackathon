# Crypto Bears
크립토 베어즈는 SCORE 가이드를 위한 교육용 컨텐츠로 제작된 프로젝트입니다. 스코어에 대한 설명은 [SCORE](https://github.com/icon-project/score-guide)를 참조하세요

크립토 베어즈는 bearFactory , CryptoBears , BattleSCORE 세가지 개별 스코어 패키지로 구성되어있습니다. 크립토 베어즈는 InterfaceScore 클래스를 이용하여 연결되어 있습니다. 먼저 CryptoBears 를 배포하고 그 결과로 받은 SCORE ADDRESS를 인자로 나머지 두개의 SCORE 패키지를 배포하면 프로젝트 구성이 완료됩니다.

그러면 먼저 가장 중심이 되는 CryptoBears를 먼저 살펴보겠습니다. 

## CryptoBears.py
### __init__

```python
	def __init__(self, db: IconScoreDatabase, _tokenId = None) -> None:
		super().__init__(db)
		self._bear_level = DictDB(self._BEAR_LEVEL, db, value_type=int)
		self._token_list = ArrayDB(self._TOKEN_LIST, db, value_type=int)
		self._token_owner = DictDB(self._TOKEN_OWNER, db, value_type=Address)
		self._token_id = DictDB(self._TOKEN_ID, db, value_type=str)
		self._token_approved = DictDB(self._TOKEN_APPROVED, db, value_type=Address)

```

크립토 베어즈는 IRC3 토큰을 따라 만들어졌습니다. 그래서 베어 하나를 IRC3 토큰과 같이 생각 할 수 있습니다. `__init__` 은 스코어 파일이 로드될 때 마다 수행되는 함수로 이때 stateDB의 값을 로드하게됩니다. 다음은 각 변수에 대한 설명입니다.
- `_bear_level` : 각 베어의 레벨이 저장된 dict DB 입니다.
- `_token_list` : 존재하는 베어들의 목록을 가지고 있는 array DB 입니다.
- `_token_owner` : 각 베어들의 id값을 key로 가지고 owner 정보를 저장한 dict DB 입니다.
- `_token_id` : 베어 소유자들의 address값을 key로 가지고 해당 address가 소유한 베어들의 id 값을 JSON형식 str으로 가지고 있는 dic DB입니다.
- `_token_approved` :  각 베어들의 id값을 key로 가지고 위임자 정보를 저장한 dict DB 입니다.

### IRC3
```python
	@eventlog(indexed=3)
	def Transfer(self, _from: Address, _to: Address, _tokenId: int):
		pass
        
	@eventlog(indexed=3)
	def Approval(self, _owner: Address, _approved: Address, _tokenId: int):
		pass
		
	@external(readonly=True)
	def name(self) -> str:
		return 'CryptoBears'
		
		...
		...
		...

```
IRC3 스탠다드 토큰을 따르기 위해 선언된 메소드들입니다. [IRC3](https://www.icondev.io/score031.do) 를 참조 하세요

### 외부호출함수
```python
	@external
    def enrollBattle(self, _score: Address, _nonce: int):
        self.approve(_score, self.getTokenId(self.msg.sender, 0))

        battelSCORE = self.create_interface_score(_score, BattleScoreInterface)
        battelSCORE.enroll(self.msg.sender, _nonce)
```
소유하고 있는 베어가 한마리 이상이라면 베틀에 참여할 수 있습니다. 베틀 스코어의 어드레스를 패러미터로 입력하면 해당 스코어의 enroll 메소드를 실행시킵니다.

```python
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
```
createCryptoBear는 BearFactory 스코어를 통해 실행되는 외부함수입니다. _createCryptoBear를 통해 베어의 탄생이 완료됩니다.

```python
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
```
happyMeal 함수를 통해 소유한 베어에게 먹이를 줄 수 있습니다. 함수 실행을 위해 1 ICX가 필요하며 수행 후 베어의 레벨이 1 상승합니다. 최고레벨은 10입니다.


## bearFactory.py
베어팩토리는 이름 그대로 베어를 만들기 위해 존재하는 공장 역활을 하는 SCORE 입니다.
### init
```python
 	def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._block_check = DictDB(self._BLOCK_CHECK, db, value_type=int)
        self._interface_score = VarDB(self._INTERFACE_SCORE, db, value_type=Address)
```
베어팩토리 SCORE는 로드되며 두가지 stateDB 값을 불러옵니다.
- `_block_check` : key 값으로 지갑의 Address를 가집니다. 해당 Address가 마지막으로 베어를 생성한 블록의 높이 정보를 가지고 있습니다. 이 정보는 베어 생성을 한 번 하고나서 바로 생성을 할 수 없게 만드는 타이머 역활을 하게 됩니다.
- `_interface_score` : CryptoCave(bearFactory의 메인 클래스)가 바라보는 스코어의 주소를 저장합니다. 인터페이스 스코어를 활용한 외부 스코어의 함수 호출에 쓰여지게 되고 install 과정에서 CryptoBears 스코어 주소로 초기화됩니다.

### createCryptoBear
```python
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
```
1 ICX 이상의 value로 함수호출을 할 경우 실행됩니다. `_block_check` 데이터를 조회하여 sender의 최근 베어 생성 기록을 조회하고 `최근 베어 생성했을 때의 블록 높이 + 30` 보다 현재 브록 높이가 높으면 실행 가능합니다.  `bearDNA` 에 난수값을 생성하여 초기화하고 인터페이스 스코어를 통해 CryptoBears 스코어의 createCryptoBear 외부함수를 실행시킴으로서 자기 소유의 베어 한마리를 생성해줍니다.

## BattleSCORE.py
### init
```python
	def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._participant = ArrayDB(self._PARTICIPANT, db, value_type=Address)
        self._nonce = DictDB(self._PARTICIPANT, db, value_type=int)
        self._interface_score = VarDB(self._INTERFACE_SCORE, db, value_type=Address)

```
- `_participant` : 참가자 주소를 저장합니다
- `_nonce` : battle 이 시작됐을 때 난수값 생성에 쓰일 nonce 값 정보입니다.
- `_interface_score` : CryptoBears 스코어의 주소입니다.

### enroll
```python
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
```
이 함수를 통해 battle에 참여 할 수 있습니다.(함수의 호출은 CryptoBears 스코어를 통해서 할 수 있습니다.) 베틀 참여를 위해서는 최소 1마리 이상의 베어를 소유해야 합니다. 참가자가 모여 두명이 되면 battle을 진행합니다. 게임은 각 플레이어마다 난수값을 생성해 결과 값이 큰 플레이어가 승리하는 방식으로 진행되며 패배자의 베어는 승리자의 소유로 옮겨지게 됩니다.



# UI
 