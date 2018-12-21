# DPES(Decentralized Performance Evaluation System)


> - 우주 최초의 완전한 탈중앙화 성과 평가 시스템 DPES
> - ICON SCORE 기술을 적용한 탈중앙화 P2P 성과 평가 시스템으로, 온체인에서 지갑을 통해 수평조직 내에서 조직원 간의 평가를 구현.
> - Front-end: Vue.js + Vue router + Vuex + icon-sdk-js
> - Blockchain: ICON SCORE (https://www.icondev.io/gettingStart01.do)
> - Back-end: json-server (mock server)
> - Utility: [ICONex](https://chrome.google.com/webstore/detail/iconex/flpiciilemghbmfalicajoolhkkenfel?hl=ko)
> - 개발자: 김진현(couldseeme@icon.foundation), 하봉안(bongan@icon.foundation), 김태영(thinktyk@icon.foundation)

## 핵심 가치

#### Value Proposition: Technology

익명성
>- 공개 계정을 통한 피평가
>- 비밀 계정을 통한 평가
>- 아이덴티티 이중화를 통한 완전한 익명화 실현

투명성
>- 평가의 과정과 그 결과가 완전히 투명하게 공개
>- 평가 결과를 통한 인센티브의 전송이 투명하게 공개

불변성
>- 정보가 공용 블록체인에 저장되어 노드 대한 침입, 조작의 가능성 차단

#### Value Proposition: Product

P2P 다면 평가
>- 실무자, 외부 평가자를 통해 피평가자에 대한 정보를 수집하고, 피드백을 확보할 수 있음
>- 평가 결과의 주된 목적은 보상보다는 개발과 조직 관리
>- 조직원들에 대한 구체적인 데이터를 수집할 수 있고, 평가자 간 성장 자극 효과

평가 신뢰 확보
>- 3자 컨센서스를 통해 다면 평가의 결과를 검증하여, 신뢰성 확보

Token Economy 기반 인센티브/패널티
>- 참여자에게 인센티브를 추구하고, 패널티를 회피하게 하여, 합리적으로 행동하도록 유도
>- 평가를 보다 신중하고 신뢰도 있게 만듬

#### Value Proposition: Business

확정적 트랜잭션
>- 네트워크 활성화에 도움되는 활성 트랜잭션이 확정적으로 발생
>- 활성 트랜잭션 발생 수 =
>- ex) 1분기 인사평가를, 10개의 부서가 있으며, 부서 당 10명이 있는 회사일 경우 = 1 x 10 x 100

수익 창출
>- 워크스페이스 개설 시, 차지풀에 토큰 납입.
>- 매 워크스페이스의 24시간마다 Stake된 ICX를 차감하는 Pricing Model 수립

확장성
>- 성과 평과 시스템을 추상화 된 평가 모델로 활용하여, 성과 평과 이외에 다양한 분야로 활용이 가능

## 구성

> - dpes-score : ICON Network에서 작동하는 SCORE 기반의 스마트 컨트랙트
> - dpes: Vue.js 기반의 프론트엔드 클라이언트

## Tutorial - dpes-score

### 디렉토리 구조

	.
	├── src         # SCORE code directory
	│   ├── dpes_project_score  # DPES workspace score
	│   └── dpes_score	    # DPES main app score
	├── keystores	# keystore files for example
	└── config	# example tx object

DPES의 SCORE는 `dpes_score` 와 `dpes_project_score`, 크게 두 가지로 구성되어 있습니다. `dpes_score`는 앱마다 고유하게 존재하는 앱 데이터 저장 및 유저 화이트리스트 관리용 SCORE이며, `dpes_project_score`는 새로운 워크스페이스를 생성할 때마다 deploy되는 SCORE입니다. 

### dpes_score API

#### Methods

##### `create_parent_dict`

팀 공용계정 주소 화이트리스트를 생성합니다. 이 단계에서 추가된 계정주소만 팀 공용계정으로 사용될 수 있습니다. 

```python
def create_parent_dict(self, formatted_json: str) -> None:
	"""
	:param formatted_json: parent json array (e.g. '[{"address":"address_1", "limit":10}, {...}]')
		• address
		• parent_name
		• limit
		• parent_level (team, oracle)
	:return: None
	"""
	pass
```

##### `sign_up`

자신의 평가 계정 주소를 팀 공용계정 멤버 화이트리스트에 등록시킵니다. 팀 리더도 `sign_up` 함수를 사용해 자신의 계정 주소를 등록시킵니다.

```python
def sign_up(self, child_address: Address, is_leader: int) -> None:
	"""
	:param 
		child_address: child address
		is_leader: whether leader of team or not (0x0, 0x1)
	:return: None
	"""
	pass
```

##### `close_vote`

해당 워크스페이스의 페이즈를 평가 단계에서 심사 단계로 전환시킵니다. 

```python
def close_vote(self, project_address: Address) -> None:
	"""
	:param project_address: project cx address
	"""
	pass
```

##### `audit_vote`

해당 워크스페이스의 평가들을 팀 리더가 심사한 뒤, 이상이 없으면 심사를 완료하였음을 알립니다.

```python
def audit_vote(self, _project_address: Address) -> None:
	"""
	:param project_address: project cx address
	"""
	pass
```

##### `distribute_prize`

우수 평가 직원에게 리워드를 분배합니다.

```python
def distribute_prize(self, project_address: Address, prize_amount: int, formatted_score_and_gainer_dict: str) -> None:
	"""
	:param 
		project_address: project cx address
		formatted_score_and_gainer_dict: score list, gainer list included
	"""
	pass
```

#### Methods (readonly)

##### `get_user_info`

직원 계정의 총 평가 등급과, 총 리워드 수령 양을 가져옵니다.

```python
def get_user_info(self, user_address: Address) -> dict:
	"""
	:param user_address: user address
	:return: dict
		• balance
		• grade
	"""
	pass
```

##### `check_parent_exist`

해당 지갑 주소가 팀 공용계정 주소인지 체크합니다.

```python
def check_parent_exist(self, parent_address: Address) -> bool:
	"""
	:param parent_address: parent address
	:return: bool
	"""
	pass
```

##### `check_child_exist`

해당 지갑 주소가 평가 계정 주소인지 체크합니다.

```python
def check_child_exist(self, child_address: Address) -> bool:
	"""
	:param child_address: child address
	:return: bool
	"""
	pass
```

##### `get_parent_level`

해당 팀 공용계정 주소가 오라클 팀인지, 일반 팀인지를 가져옵니다. (일반 팀: 1, 오라클 팀: 2)

```python
def get_parent_level(self, parent_address: Address) -> int:
	"""
	:param parent_address: parent address
	:return: int
	"""
	pass
```

##### `get_child_level`

해당 평가 계정 주소가 오라클인지, 팀 리더인지, 일반 평가자인지를 가져옵니다. (일반 평가자: 1, 팀 리더: 2, 오라클 평가자: 3)

```python
def get_parent_level(self, parent_address: Address) -> int:
	"""
	:param parent_address: parent address
	:return: int
	"""
	pass
```

##### `get_team_count`

팀의 전체 수를 가져옵니다.

```python
def get_team_count(self) -> int:
	"""
	:return: team count
	"""
	pass
```

### dpes_project_score API

#### Methods (readonly)

##### `get_project_info`

워크스페이스 정보를 가져옵니다.

```python
def get_project_info(self) -> dict:
	"""
	:return: dict
		• name: 워크스페이스 제목
		• desc: 워크스페이스 설명
		• prize_amount: 우수 평가자에게 지급되는 리워드 양
		• due_date: 평가 기한
		• status: 워크스페이스 페이즈 (평가단계: 1, 심사단계: 2, 완료: 3)
	"""
```

##### `get_message_list`

이 워크스페이스에서 해당 직원이 받은 코멘트들을 가져옵니다.

```python
def get_message_list(self, _user_address: Address) -> list:
	"""
	:return: list
	"""
```

##### `get_review_result`

이 워크스페이스에서 해당 직원이 받은 팀 내 모든 평가 목록 및 점수를 가져옵니다.

```python
def get_review_result(self, _user_address: Address) -> list:
	"""
	:return: list
	"""
```

### 스코어 실행 flow example

먼저 관리자 계정으로 `dpes_score` 를 deploy합니다. 
(모든 예제 계정 키스토어 파일의 비밀번호는 "@1234qwer" 입니다.)

```bash
# deploy dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json

# deploy_dpes_score.json
{
    "uri": "https://bicon.net.solidwallet.io/api/v3",
    "nid": "0x3",
    "keyStore": null,
    "from": "hxa4c3a78d73bb7287f72801c09298f1a5743b1655",
    "to": "cx0000000000000000000000000000000000000000",
    "deploy": {
        "stepLimit": "0x5a0000000",
        "contentType": "zip",
        "mode": "install",
        "scoreParams": {
        }
    },
    "txresult": {},
    "transfer": {}
}
```

아래 커맨드를 통해 deploy한 `dpes_score` 를 수정할 수도 있습니다. 

```bash
# update deployed dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json -m update -o cx635118b9865c8cddee4759dff5d29360f5664d5a
```

워크스페이스 생성 및 리워드 지급을 위한 ICX를 미리 예치합니다.

```bash
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/send_icx_to_contract.json

# send_icx_to_contract.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hxa4c3a78d73bb7287f72801c09298f1a5743b1655",
        "value": "0x1a055690d9db80000",
        "stepLimit": "0x9502f900",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cx635118b9865c8cddee4759dff5d29360f5664d5a"
    },
    "id": 1
}
```

다음으로, 팀 공용계정주소 화이트리스트를 생성합니다. 이 단계에서 추가된 계정주소만 팀 공용계정으로 사용될 수 있습니다. 

```bash
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/create_parent_dict.json

# create_parent_dict.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hxa4c3a78d73bb7287f72801c09298f1a5743b1655",
        "value": "0x0",
        "stepLimit": "0x9502f900",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cx635118b9865c8cddee4759dff5d29360f5664d5a",
        "dataType": "call",
            "data": {
                "method": "create_parent_dict",
                "params": {
                    "_formatted_json": "[{\"address\":\"hx435b4dd5f623f2e31c691bf480902a3056b828ac\",\"limit\":\"0x2\",\"name\":\"Global\",\"parent_level\":\"0x1\"},{\"address\":\"hx4ed9e9c34451bd3ceb85a7530cb0b0986fd46f79\",\"limit\":\"0x2\",\"name\":\"Develop\",\"parent_level\":\"0x1\"},{\"address\":\"hx6efa0281337beea3c3888398e0cba640482aec36\",\"limit\":\"0x1\",\"name\":\"Oracle\",\"parent_level\":\"0x2\"}]"
                }
            }
    },
    "id": 1
}
```

화이트리스트가 생성되면, 팀 공용계정 주소로 평가 계정 주소를 화이트리스트에 추가하는 트랜잭션을 발생시킬 수 있습니다. 각 팀의 리더도 이 과정을 통해 자신의 계정을 화이트리스트에 추가할 수 있습니다.

```bash
tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_1.json

# sign_up_1_1.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hx435b4dd5f623f2e31c691bf480902a3056b828ac",
        "value": "0x0",
        "stepLimit": "0xdbba0",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cx635118b9865c8cddee4759dff5d29360f5664d5a",
        "dataType": "call",
            "data": {
                "method": "sign_up",
                "params": {
                    "_child_address": "hx8a6f27ec9347b3e0f330ac929920e3f48ad4e5cd",
                    "_is_leader": "0x0"
                }
            }
    },
    "id": 1
}
```

한편, 관리자 계정은 `dpes_project_score`를 deploy하여 워크스페이스를 생성할 수 있습니다. 

```bash
# deploy project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json

# deploy_dpes_project_score.json
{
    "uri": "https://bicon.net.solidwallet.io/api/v3",
    "nid": "0x3",
    "keyStore": null,
    "from": "hxa4c3a78d73bb7287f72801c09298f1a5743b1655",
    "to": "cx0000000000000000000000000000000000000000",
    "deploy": {
        "stepLimit": "0x5a0000000",
        "contentType": "zip",
        "mode": "install",
        "scoreParams": {
            "name": "2018 1Q 평가",
            "desc": "2018 1Q 평가 섹션입니다.",
            "prize_amount": "0x2386f26fc10000",
            "due_date": "0x59b08c1fa4000",
            "dpes_score_address": "cx635118b9865c8cddee4759dff5d29360f5664d5a"
        }
    },
    "txresult": {},
    "transfer": {}
}

# update project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json -m update -o cxb787980518b717a7f986500576c6a24c0294ed64
```

각 워크스페이스마다, 평가 계정은 자신의 팀원들을 평가할 수 있습니다.

```bash
tbears sendtx -k ../keystores/P1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_1_t_1_1.json

# vote_f_1_1_t_1_1.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hx8a6f27ec9347b3e0f330ac929920e3f48ad4e5cd",
        "value": "0x0",
        "stepLimit": "0xdbba0",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cxb787980518b717a7f986500576c6a24c0294ed64",
        "dataType": "call",
            "data": {
                "method": "vote",
                "params": {
                    "_from": "hx8a6f27ec9347b3e0f330ac929920e3f48ad4e5cd", 
                    "_to": "hxcacb3b4b04f0f0e4e1667163476d436c87dd11bc",
                    "_formatted_json": "[{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x3\"},{\"type\":\"int\",\"value\":\"0x3\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x3\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x4\"},{\"type\":\"int\",\"value\":\"0x3\"},{\"type\":\"bool\",\"value\":\"0x1\"}]",
                    "_message": "진짜 열심히 하는 친구랍니다."
                }
            }
    },
    "id": 1
}
```

모든 사람이 평가를 완료하면, 관리자는 워크스페이스의 페이즈를 평가 단계에서 심사 단계로 전환합니다.  (실제 시나리오에선 평가가 전부 완료되거나, 평가 기간이 지나면 자동으로 평가 단계에서 심사 단계로 전환되어야 합니다.)

```bash
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/close_vote.json

# close_vote.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hxa4c3a78d73bb7287f72801c09298f1a5743b1655",
        "value": "0x0",
        "stepLimit": "0x9502f900",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cx635118b9865c8cddee4759dff5d29360f5664d5a",
        "dataType": "call",
            "data": {
                "method": "close_vote",
                "params": {
                    "_project_address": "cxb787980518b717a7f986500576c6a24c0294ed64"
                }
            }
    },
    "id": 1
}
```

모든 평가가 종료되면, 각 팀의 리더가 평가를 검증하는 절차를 거칩니다. 리더 모두가 검증 절차를 완료하면, 리워드 수령 조건을 만족한 직원의 계정으로 리워드가 입금됩니다.

```bash
tbears sendtx -k ../keystores/P1-L.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/audit_vote_1.json

# audit_vote_1.json
{
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "params": {
        "version": "0x3",
        "from": "hx908f59b7ea6bbbc6b2fcfc629d7cacdb22db6432",
        "value": "0x0",
        "stepLimit": "0x9502f9",
        "nid": "0x3",
        "nonce": "0x1",
        "to": "cx635118b9865c8cddee4759dff5d29360f5664d5a",
        "dataType": "call",
            "data": {
                "method": "audit_vote",
                "params": {
                    "_project_address": "cxb787980518b717a7f986500576c6a24c0294ed64"
                }
            }
    },
    "id": 1
}
```

## Tutorial - dpes (FRONT-END & BACK-END)

### 디렉토리 구조
	.
	├── src              # App code directory
	│   ├── api             # api (SCORE, ICONex-connect, etc.)
	│   ├── assets          # static images
	│   ├── constants       # Constants
	│   ├── sdk             # icon-sdk-js helper func
	│   ├── server          # json-server db
	│   ├── store           # Vuex store 
	│   └── views           # Vue components
	├── App.vue          # App main container 
	├── main.js          # App entry file 
	└── router.js        # Vue-router config

### 설치 및 실행방법

의존성 모듈을 설치한 후, json-server를 구동합니다.
```bash
cd dpes
npm i # npm install
json-server --watch ./src/server/db.json
```

`serve` 스크립트를 실행하면, `http://localhost:8080` 를 통해 로컬 환경에서 앱을 사용할 수 있습니다. 
```bash
npm run serve 
# App running at http://localhost:8080
```

## 가이드
[ICON SCORE](https://www.icondev.io/gettingStart01.do)
[Vue.js](http://vuejs-templates.github.io/webpack/)
[Vue Loader](https://vue-loader-v14.vuejs.org/)
