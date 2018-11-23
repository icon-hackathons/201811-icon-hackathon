# ICONDICE server app

> Server app for ICONDICE developed with sanic

## Requirements
* OS: MacOS, Linux
  - Windows are not supported yet.
* Python
  - Make Virtual Env for Python 3.6.5+ (recommended version, 3.7 is not supported)
  - check your python version

    ```
    $ python3 -V
    ```
* Install third party tools
  ```
  $ brew install leveldb automake libtool pkg-config libffi gmp openssl
  ```


## How to Start

#### Git clone and install requirements

```
$ git clone git@repo.theloop.co.kr:hackathon/dice_server.git
$ cd dice_server
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

#### Let's run the app!
It's simple as this:

```
(venv) $ python3 app.py
```

## Client Example for Python

#### Check hello world

* http request

```python
import requests

uri = 'http://127.0.0.1:8000'
response = requests.get(uri)
print(response)

# {"Hello": "ICONDICE world"}
```

> Otherwise, simply by terminal:
  
```
$ curl http://127.0.0.1:8000
>>  {"Hello": "ICONDICE world"}
```

* websocket Request

```python
uri = 'ws://127.0.0.1:8000/hello'
async with websockets.connect(uri) as websocket:
  await websocket.send('hello')
  response = await websocket.recv()
  print(response)

# 'ICONDICE websocket'
```

#### Login

```python
import json
from jsonrpcclient.cliets.http_client import HTTPClient
import utils

# create your private_key and address
test_address, private_key = utils.create_new_address_and_privkey()

# login_hash request and sign
url = 'https://bicon.net.solidwallet.io/api/v3'
http_client = HTTPClient(url)
response = http_client.request(method_name='login_hash', address=test_address)
random_bytes = bytes.fromhex(json.loads(response.text)['result'][2:])
signature_base64str = utils.sign(private_key, random_bytes)

# login and get your token
response = http_client.request(method_name='login', address=test_address, signature=signature_base64str)
token = json.loads(response.text)['result']
```

## Configuration

You should set the ICONex wallet and private key of the backend server in order to integrate ICONDICE game with client service. 
Currently, it's replaced with an arbitrary string for security purposes, 
and the game will not work without these items.

```python
# utils.py
import binascii
from secp256k1 import PrivateKey
from icx_wallet import IcxWallet

class CONFIG:
    ...
    # <example>
    deserialized_private_key = "5257a9df23980000000000000000000000000000000000000000000000000000"
    private_key = PrivateKey(binascii.unhexlify(deserialized_private_key))
    address = 'hxa94f1eb1ba891c680d00bc000000000000000000'
    icx_wallet = IcxWallet(private_key)

```


## API References

### JsonRPC API

####  login_hash

* Request

```json
{
    "jsonrpc": "2.0",
    "method": "login_hash",
    "id": 1234,
    "params": {
        "address": "hxbe258ceb872e08851f1f59694dac2558708ece11"
        }
    }
}
```

* Response

```json
{
    "jsonrpc": "2.0",
    "id": 1234,
    "result": "0x1fcf7c34dc875681761bdaa5d75d770e78e8166b5c4f06c226c53300cbe85f57" // random hash to sign
}
```


#### login

* Request

```json
{
    "jsonrpc": "2.0",
    "method": "login",
    "id": 1234,
    "params": {
        "address": "hxbe258ceb872e08851f1f59694dac2558708ece11",
        "signature": "VAia7YZ2Ji6igKWzjR2YsGa2m53nKPrfK7uXYW78QLE+ATehAVZPC40szvAiA6NEU5gCYB4c4qaQzqDh2ugcHgA="  // signed by address's private. base64 encoded
        }
    }
}
```

* Response

```json
{
    "jsonrpc": "2.0",
    "id": 1234,
    "result": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZGRyZXNzIjoiaHg3YjQxMjBmNzRjOTNiNDhmZWQ1OTljM2NiMjJlOGRmOWRlY2RiZThlIn0.X9sR6yIBvOvw7T8wBtUQGRT_CAJWXWgsKzDShH2MYFY" # a jwt token.
}
```

#### set_nickname

* Request

```json
{
    "jsonrpc": "2.0",
    "method": "set_nickname",
    "id": 1234,
    "params": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZGRyZXNzIjoiaHg3YjQxMjBmNzRjOTNiNDhmZWQ1OTljM2NiMjJlOGRmOWRlY2RiZThlIn0.X9sR6yIBvOvw7T8wBtUQGRT_CAJWXWgsKzDShH2MYFY",
        "nickname": "june"
        }
    }
}
```

* Reponse

```json
{
    "jsonrpc": "2.0",
    "id": 1234,
    "result": "success"
}
```

#### get_nickname

* Request

```json
{
    "jsonrpc": "2.0",
    "method": "get_nickname",
    "id": 1234,
    "params": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZGRyZXNzIjoiaHg3YjQxMjBmNzRjOTNiNDhmZWQ1OTljM2NiMjJlOGRmOWRlY2RiZThlIn0.X9sR6yIBvOvw7T8wBtUQGRT_CAJWXWgsKzDShH2MYFY"
        }
    }
}
```

* Reponse

```json
{
    "jsonrpc": "2.0",
    "id": 1234,
    "result": "june"
}
```

### Websocket Api

#### Phase 1 Start

* Request

```json
{
   "token": "token_string"
}
```

* Response

```json
{
   "game_room_id": int,
   "opposite_address": "hx1212abcd",
   "opposite_nickname": "junepark"
}
```

#### Phase 1 End

• Request

```json
{
   "start_game_tx": "0x122123ba"
}
```

* Response

```json
{
   "success"
}
```

#### Reveal Game web socket

* Request

```json
{
   "reveal_game_tx_hash": "0x123122"
}
```

* Response

```json
{
   "player_dice_result": int  // range[1, 6],
   "opposite_dice_result": int  // range[1, 6]
}
```
