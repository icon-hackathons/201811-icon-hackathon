IconDice Dapp Guide
==

# Overview
IconDice에 대한 기능 설명 및 function설명


## const
- ICX_DECIMALS = 10 ** 18 <- Icx의 Decimal 상수세팅

- TICKET_PRICE = 1 * ICX_DECIMALS <- 게임 참가 티켓 가격

- LIMIT_MEMBER = 2 <- 제한 멤버

- EXPIRED_BLOCK = 3 <- 게임의 유통기한(해당 내용은 밑에서 자세히 설명, 변동될 수 있습니다.)


## Method List

* Query Methods
    * [get_deposit](#get_deposit)
    * [can_start_game](#can_start_game)
    * [get_enable_withdraw](#get_enable_withdraw)
* Invoke methods
    * [pay_advance](#pay_advance)
    * [start_game](#start_game)
    * [reveal_game](#reveal_game)
    * [end_game](#end_game)
    * [withdraw](#withdraw)
* Eventlog
    * [GameResult](#gameresult)

### Query Methods
Query method does not change state. Read-only.

#### get_deposit
* 해당 주소의 예치금을 보여줍니다

```python
def get_deposit(self, addr: Address) -> int:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_call",
  "params": {
    "from": "EOA-ADDRESS",
    "to": "SCORE_ADDRESS",
    "dataType": "call",
    "data": {
      "method": "get_deposit",
      "params": {
         "addr": "EOA_ADDRESS"
      }
    }
  },
  "id": 1
}
```

###### response
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": hex(DEPOSIT_BALANCE)
}
```

#### can_start_game
* 현재 해당 주소가 게임을 할수 있는지 알려줍니다.
* 예치금에서 staking된 돈이 TICKET_PRICE 크면 true, 아니면 false

```python
def can_start_game(self, addr: Address) -> bool:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_call",
  "params": {
    "from": "EOA-ADDRESS",
    "to": "SCORE_ADDRESS",
    "dataType": "call",
    "data": {
      "method": "can_start_game",
      "params": {
          "addr": "EOA-ADDRESS"
       }
    }
  },
  "id": 1
}

```

###### response
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": hex(BOOLEAN)
}
```

#### get_enable_withdraw
* 현재 해당 주소가 인출가능한 금액을 알려줍니다.
* 인출 가능한 금액 = 현제 예치금액 - staking된 금액

```python
def get_enable_withdraw(self, addr: Address) -> int:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_call",
  "params": {
    "from": "EOA-ADDRESS",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "get_enable_withdraw",
      "params": {
          "addr": "EOA-ADDRESS"
       }
    }
  },
  "id": 1
}
```

###### response
```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": hex(ENABLE_WITHDRAW_BALANCE)
}
```

### Invoke Methods
Invoke method can initiate state transition.

#### pay_advance
* 해당함수는 호출될때 ticket가격만큼 예치가 됩니다.
* 1회당 TICKET_PRICE

```python
def pay_advance(self) -> None:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "EOA-ADDRESS",
    "value": hex(TICKET_PRICE),
    "stepLimit": "0xSTEPLIMIT",
    "timestamp": "0xTIMESTAMP",
    "nid": "0xNID",
    "nonce": "0xANY",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "pay_advance",
      "params": {}
    }
  },
  "id": 1
}
```

#### start_game
* 1 phase 프론트앤드에서 게임스타트를 진행할때 해당 함수가 호출되며 해당 게임에 대한 TICKET_PRICE 가격이 예치금에서 staking됩니다.
* game_id : 백앤드에서 매칭된 id
* sha_key : 프론트앤드에서 생성된 sha3_256(seed)된 값

```python
def start_game(self, game_id: bytes, sha_key: bytes) -> None:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "EOA-ADDRESS",
    "value": "0x0",
    "stepLimit": "0xSTEPLIMIT",
    "timestamp": "0xTIMESTAMP",
    "nid": "0xNID",
    "nonce": "0xANY",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "start_game",
      "params": {
        "game_id": "0x{bytes.hex()}",
        "sha_key": "0x{bytes.hex()}"
      }
    }
  },
  "id": 1
}
```

#### reveal_game
* 1 phase에서 넘겨받은 sha_key를 2 phase 에서 넘겨밭은 seed값으로 validating을 진행하여 성공하면 넘겨받은 seed_key를 저장합니다.
* game_id : 백앤드에서 매칭된 id
* seed_key : 1 phase 에 넘겨준 sha_key를 생성한 seed값

```python
def reveal_game(self, game_id: bytes, seed_key: bytes) -> None:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "EOA-ADDRESS",
    "value": "0x0",
    "stepLimit": "0xSTEPLIMIT",
    "timestamp": "0xTIMESTAMP",
    "nid": "0xNID",
    "nonce": "0xANY",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "reveal_game",
      "params": {
        "game_id": "0x{bytes.hex()}",
        "seed_key": "0x{bytes.hex()}"
      }
    }
  },
  "id": 1
}
```

#### end_game
* 1, 2 phase를 최종 통과한 EOA참가자에 한하여 산출된 RANDOM값으로 주사위값을 계산후에 결과를 반영하고 서로 staking된 예치금을 승리자에게 분배합니다.
* 해당 tx는 BACKEND 또는 다른EOA계정이 해도 됩니다.
* 만약 A 는 2phase까지 진행하고, B가 2phase까지 진행하지 않은 상태에서 블럭유효기간(EXPIRED_BLOCK)이 지난후에 해당 함수를 호출하면 결과를 산출하여 예치금을 분배 합니다. 
    * 블럭유효기간이 지날동안 해당 2 phase까지 진행안한 참가자는 자동 패배자가 됩니다.
 
* game_id : 백앤드에서 매칭된 id
* seed_key : 1 phase 에 넘겨준 sha_key를 생성한 seed값

```python
def end_game(self, game_id: bytes, addr1: Address, addr2: Address) -> None:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "EOA-ADDRESS",
    "value": "0x0",
    "stepLimit": "0xSTEPLIMIT",
    "timestamp": "0xTIMESTAMP",
    "nid": "0xNID",
    "nonce": "0xANY",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "end_game",
      "params": {
        "game_id": "0x{bytes.hex()}",
        "addr1": "EOA-ADDRESS",
        "addr2": "EOA-ADDRESS"
      }
    }
  },
  "id": 1
}
```

#### withdraw
* [get_enable_withdraw](#get_enable_withdraw)한 icx 금액을 실제 해당 EOA주소로 환급합니다.

```python
def withdraw(self) -> None:
```

##### Examples

###### request
```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "EOA-ADDRESS",
    "value": "0x0",
    "stepLimit": "0xSTEPLIMIT",
    "timestamp": "0xTIMESTAMP",
    "nid": "0xNID",
    "nonce": "0xANY",
    "to": "SCORE-ADDRESS",
    "dataType": "call",
    "data": {
      "method": "withdraw",
      "params": {}
    }
  },
  "id": 1
}
```

### Eventlog

#### GameResult
* 게임 주사위 결과를 eventlog로 기록합니다.

```python
@eventlog
def GameResult(self, addr1: Address, addr2: Address, ran1: int, ran2: int):
    pass
```
