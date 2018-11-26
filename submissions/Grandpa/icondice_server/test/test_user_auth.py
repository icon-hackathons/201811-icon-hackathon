import hashlib
import json
import unittest

import jwt
import requests
from jsonrpcclient.clients.http_client import HTTPClient
from secp256k1 import PrivateKey

import utils
from app import app
from config import CONFIG

http_client = HTTPClient(CONFIG.http_uri + '/users')

PRIVATE_KEY = PrivateKey()
serialized_pub = PRIVATE_KEY.pubkey.serialize(compressed=False)
hashed_pub = hashlib.sha3_256(serialized_pub[1:]).digest()
test_address = "hx" + hashed_pub[-20:].hex()
test_token = None


class TestUserAuth(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        self.assertEqual(response.status, 200)

    def test_login(self):
        # test login_hash
        response = http_client.request(method_name='login_hash', address=test_address)
        result = json.loads(response.text)['result']
        random_bytes = bytes.fromhex(result[2:])
        random_result_example = '0x9aa0330713174af486fb46144ed479bbee6054d448e6484d86e7507c780779b4'

        self.assertNotEqual(result, random_result_example)
        self.assertEqual(len(result), 66)

        # test login
        signature_base64str = utils.sign(PRIVATE_KEY, random_bytes)
        response = http_client.request(method_name='login', address=test_address, signature=signature_base64str)
        result = json.loads(response.text)['result']

        token = utils.generate_jwt(test_address)

        self.assertEqual(result, token)

        # test set_nickname
        response = http_client.request(method_name='set_nickname', token=token, nickname='june')
        user_data = requests.get(CONFIG.http_uri + '/db').json()
        nickname = user_data[test_address]['nickname']

        self.assertEqual(nickname, 'june')

        # test login again and nickname remains
        response = http_client.request(method_name='login_hash', address=test_address)
        random_result = json.loads(response.text)['result']
        random_bytes = bytes.fromhex(random_result[2:])
        signature_base64str = utils.sign(PRIVATE_KEY, random_bytes)
        response = http_client.request(method_name='login', address=test_address, signature=signature_base64str)
        nickname_response = http_client.request(method_name='get_nickname', token=token)
        nickname = json.loads(nickname_response.text)['result']

        self.assertEqual(nickname, 'june')

    def test_jwt_decode_address(self):
        key = 'secret'
        encoded = jwt.encode(
            payload={'address': test_address},
            key=key,
            algorithm='HS256')
        decoded = jwt.decode(encoded, key, algorithms='HS256')
        self.assertEqual(decoded['address'], test_address)
