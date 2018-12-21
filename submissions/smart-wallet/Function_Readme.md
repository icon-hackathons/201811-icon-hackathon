## 주요 함수

### add_account(self, account: str):
* 새로운 Account를 생성합니다. Owner만 새로운 Account를 생성할 수 있습니다.
* account의 id는 마지막으로 생성된 Account의 id + 1로 설정 됩니다.
* 추가된 Account의 정보는 Account 이벤트를 통해 확인 할 수 있습니다.
* params
```
   :param account: (str) String으로 Serialize된 JSON 형태의 Account 정보
```
    
    
### change_setting_value(self, account: str):
* Account의 정보를 변경합니다.
* 변경된 Account의 정보는 Account(str) 이벤트를 통해 확인 할 수 있습니다.
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

### change_new_wallet(self, did_infos: str):
* SmartWallet Owner를 Message Sender로 변경합니다.
* Owner를 변경하기 위해서는 모든 did 인증 데이터를 보내야 합니다.
* params
```
    :param did_infos: (str) serialize된 did 인증 정보들

```

### transfer(self, account_id: int, token_type: str, contract_addr: str, to: str, amount: int):
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

### approval(self, tx_id: int, did: str, auth_proof: str):
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
