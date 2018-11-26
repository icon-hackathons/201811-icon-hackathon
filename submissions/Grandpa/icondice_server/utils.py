import base64
import hashlib
import json
import os

import jwt
from jsonrpcclient.clients.http_client import HTTPClient
from secp256k1 import PublicKey, PrivateKey

from config import CONFIG


async def verify_signature(address_bytes, random_bytes, sign_bytes, private_key):
    recoverable_sig = private_key.ecdsa_recoverable_deserialize(
        ser_sig=sign_bytes[:-1],
        rec_id=sign_bytes[-1]
    )
    raw_public_key = private_key.ecdsa_recover(
        msg=random_bytes,
        recover_sig=recoverable_sig,
        raw=True,
        digest=hashlib.sha3_256
    )
    public_key = PublicKey(raw_public_key)
    hash_pub = hashlib.sha3_256(public_key.serialize(compressed=False)[1:]).digest()
    expect_address = hash_pub[-20:]
    if expect_address != address_bytes:
        raise RuntimeError


def get_address_from_token(token: str):
    token_bytes = token.encode('utf-8')
    decoded = jwt.decode(token_bytes, CONFIG.jwt_key, algorithms='HS256')
    return decoded['address']


def generate_jwt(address):
    token = jwt.encode(
        payload={'address': address},
        key=CONFIG.jwt_key,
        algorithm='HS256').decode('utf-8')
    return token


def create_new_address_and_privkey():
    private_key = PrivateKey()
    serialized_pub = private_key.pubkey.serialize(compressed=False)
    hashed_pub = hashlib.sha3_256(serialized_pub[1:]).digest()
    address = "hx" + hashed_pub[-20:].hex()
    return address, private_key


async def get_token_from_login_process(address, private_key):
    http_client = HTTPClient(CONFIG.http_uri + '/users')
    response = http_client.request(method_name='login_hash', address=address)
    random_result = json.loads(response.text)['result']
    random_bytes = bytes.fromhex(random_result[2:])
    signature_base64str = sign(private_key, random_bytes)
    response = http_client.request(method_name='login', address=address, signature=signature_base64str)
    token = json.loads(response.text)['result']
    response = http_client.request(method_name='set_nickname', token=token, nickname=address)
    return token


def sign(private_key: PrivateKey, random_bytes):
    raw_sig = private_key.ecdsa_sign_recoverable(msg=random_bytes,
                                                 raw=True,
                                                 digest=hashlib.sha3_256)
    serialized_sig, recover_id = private_key.ecdsa_recoverable_serialize(raw_sig)
    signature = serialized_sig + bytes((recover_id,))
    signature_base64str = base64.b64encode(signature).decode('utf-8')
    return signature_base64str


def get_start_game_params(address, game_room_id):
    random = os.urandom(32)
    digested_random = hashlib.sha3_256(random).digest()
    data = {
        "method": 'start_game',
        'params': {
            'game_id': game_room_id,
            'sha_key': '0x' + digested_random.hex()
        }
    }
    params = CONFIG.icx_wallet.create_icx_origin_v3(data)
    return params, random


def get_transaction_result(tx_hash):
    response = HTTPClient(CONFIG.v3_uri).request(method_name='icx_getTransactionResult', txHash=tx_hash)
    return json.loads(response.text)['result']


def send_end_game_request(game_room_id, addr1, addr2) -> str:
    data = {
        'method': 'end_game',
        'params': {
            'game_id': game_room_id,
            'addr1': addr1,
            'addr2': addr2
        }
    }
    params = CONFIG.icx_wallet.create_icx_origin_v3(data)
    print(f"params: {params}")
    response = HTTPClient(CONFIG.v3_uri).request('icx_sendTransaction', params)
    return json.loads(response.text)['result']  # tx_hash
