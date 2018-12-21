# Smart Wallet SCORE

## 기본 개념

- 지갑 키 분실 및 도난 위험에 대한 해결책 제시

- 해결책

  - Wallet 이 아닌 SCORE (contract) 에 예치
  - DID를 이용하여 자산 별 인증 레벨을 설정
  - 새로운 Private key 생성하여 키 복구 기능

- 기대 효과

  - 지갑 사용자 편의성 증대
  - 보안 강화
  - DID 네트워크 활용  


## 주요 기능

### 1. Wallet의 자산을 SCORE에 예치

- SCORE에 필요한 계약 조건을 명시함으로써 다양한 기능을 확장하여 구현 가능 
- Transaction을 수행하는데 필요한 소량의 자산을 제외한 나머지 금액을 SCORE의 기본 account 에 예치 
- 다양한 기능에 따라 SCORE에 기능별 여러 계좌를 관리 
  - 예를 들어, 기본, 소액 송금용, 거액 송금용, DApp 게임용 계좌를 생성하여 관리 가능
  
![screenshot1](https://github.com/boyeon555/201811-icon-hackathon/blob/master/submissions/smart-wallet/img/screenshot1.png)


### 2. DID인증을 통해 계좌별 인증레벨 설정

- Chain ID, Mail, KAKAO 등의 DID 인증을 각 계좌에 설정 가능 
- 계좌별 하루 송금 제한 설정 가능 
    - 예시
        - 소액 송금용 계좌에는 인증 레벨 1로 설정하여 Chain ID로 인증 필요
        - 거액 송금용 계좌에는 인증 레벨 2로 설정하여 Mail, Kakao 인증 필요
        - DApp 게임용 계좌에는 인증 레벨 1로 설정하여 Mail 인증 필요 및 하루 송금 10icx 이하로 송금 제한 설정

![screenshot1](https://github.com/boyeon555/201811-icon-hackathon/blob/master/submissions/smart-wallet/img/screenshot2.png)



### 3. 기존 Private key 분실 시 새로운 키 생성 

- 기존 Private key 분실 시 최고 3레벨 인증을 모두 통과할 경우 새로운 계좌 생성 후 Smart wallet SCORE와 연동하여 분실 위험성 최소화

![screenshot1](https://github.com/boyeon555/201811-icon-hackathon/blob/master/submissions/smart-wallet/img/screenshot3.png)


## 주요 함수

### on_install(self, account: str)

- account의 정보를 통해 초기 계좌를 생성하고 Sender를 Contract의 Owner로 설정
- 첫 계좌 id : 0
- 생성된 Account의 정보는 Account(str) 이벤트를 통해 확인 가능
-  Account 이벤트는 다음과 같은 메시지를 생성

```
    {
        "id": {AccountID (int)},
        "tokenType": {"ICX" or "IRC2" (str)},
        "contractAddr": {TokenType이 IRC2이면 IRC2 Contract의 주소(ICONAddr)},
        "balance": {잔액 (int)},
        "sendLimit": {하루 송금 제한 액(int)},
        "totalUsed": {하루 동안 사용한 Token 액수(int)},
        "lastUsedDate": {마지막 사용 날짜(int)},
        "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
    }
```

- params

```
    :param account: (str) String으로 Serialize된 JSON 형태의 Account 정보
    
    example)
    {
        "tokenType": {"ICX" or "IRC2" (str)},
        "contractAddr": {TokenType이 IRC2이면 IRC2 Contract의 주소(ICONAddr)},
        "sendLimit": {하루 송금 제한 액(int)},
        "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
    }
```

### add_account(self, account: str)

* 새로운 Account를 생성합니다. Owner만 새로운 Account를 생성
* account의 id는 마지막으로 생성된 Account의 id + 1로 설정
* 추가된 Account의 정보는 Account 이벤트를 통해 확인 가능
* params

```
    :param account: (str) String으로 Serialize된 JSON 형태의 Account 정보
```


### change_setting_value(self, account: str)

* Account의 정보를 변경
* 변경된 Account의 정보는 Account(str) 이벤트를 통해 확인 가능
* params

```
    :param account: (str) String으로 Serialize된 JSON 형태의 Account Setting 정보,
    Account Setting 정보에는 하루 송금 제한과 인증에 활용할 did가 명시되어 있어야 합니다.
    
    example)
    {
        "sendLimit": {하루 송금 제한 액(int)},
        "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
    }
```

### change_new_wallet(self, did_infos: str)
* SmartWallet Owner를 Message Sender로 변경 가능 
* Owner를 변경하기 위해서는 모든 did 인증 데이터를 보내야 합니다.
* params

```
    :param did_infos: (str) serialize된 did 인증 정보들
```

### transfer(self, account_id: int, token_type: str, contract_addr: str, to: str, amount: int)
* SmartWallet의 Account에 송금을 요청합니다.
* 송금을 시도하는 Account에 did 인증 요구사항이 있을 경우 송금 요청은 Pending 됩니다.
* 송금이 Pending 될 경우 Pending 이벤트를 발생합니다.
* Pending Event를 통해 Pending된 송금 요청의 id와 did인증 정보를 알 수 있습니다.
* 송금을 시도하는 Account에 did 인증 요구사항이 없을 경우 송금 요청을 바로 실행합니다.
* 송금이 성공할 경우 TransferSuccess 이벤트를 발생합니다.
* params

```
    :param account_id: (int) 송금하는 계좌의 id
    :param token_type: (str) 송금하는 Token Type ("ICX" or "IRC2")
    :param contract_addr: (str) 송금을 처리하는 Contract의 주소 (ICX의 경우 "")
    :param to: (str) 송금을 전송받는 계좌의 ICON Address
    :param amount: (int) 송금 수량
```

### approval(self, tx_id: int, did: str, auth_proof: str)
* Pending된 송금 요청을 did 인증을 통해 승인합니다.
* 모든 승인을 완료하면 송금 요청을 실행합니다.
* 추가 승인이 필요하면 Pending 이벤트를 발생해 새로운 Pending 이벤트를 발생합니다.
* params

```
    :param tx_id: (int) 승인하는 Transaction ID
    :param did: (str) 승인하는 did 이름
    :param auth_proof: (str) did 인증 정보
```

### fallback(self):
*  받은 icx를 기본 계좌(account id = 0)에 추가합니다.
