import base64
import os

from jsonrpcserver.aio import AsyncMethods
from sanic import response
from secp256k1 import PrivateKey

import utils
from db_manager import db_manager

methods = AsyncMethods()
PRIVATE_KEY = PrivateKey()
USERS_RANDOM = dict()  # {address_bytes: random_bytes}


class UserDispatcher:
    @staticmethod
    async def dispatch(request):
        dispatch_response = await methods.dispatch(request.json)
        return response.json(dispatch_response, status=dispatch_response.http_status)

    @staticmethod
    @methods.add
    async def login_hash(**kwargs):
        """
        :param kwargs:
        address: "hxbe258ceb872e08851f1f59694dac2558708ece11"
        :return:
        result: "0x1fcf7c34dc875681761bdaa5d75d770e78e8166b5c4f06c226c53300cbe85f57"
        """
        address = kwargs.get('address')
        address_bytes = bytes.fromhex(address[2:])
        random = os.urandom(32)
        USERS_RANDOM[address_bytes] = random
        return '0x' + random.hex()

    @staticmethod
    @methods.add
    async def login(**kwargs):
        """
        :param kwargs:
        address: "hxbe258ceb872e08851f1f59694dac2558708ece11",
        signature: "VAia7YZ2Ji6igKWzjR2YsGa2m53nKPrfK7uXYW78QLE+ATehAVZPC40szvAiA6NEU5gCYB4c4qaQzqDh2ugcHgA="
        :return:
        result: "0x48757af881f76c858890fb41934bee228ad50a71707154a482826c39b8560d4b"
        """
        address = kwargs.get('address')
        signature = kwargs.get('signature')

        address_bytes = bytes.fromhex(address[2:])
        sign_bytes = base64.b64decode(signature.encode('utf-8'))

        await utils.verify_signature(
            address_bytes=address_bytes,
            random_bytes=USERS_RANDOM[address_bytes],
            sign_bytes=sign_bytes,
            private_key=PRIVATE_KEY
        )

        token = utils.generate_jwt(address)
        if address in db_manager.get_addresses():
            db_manager.update_token(address, token)
        else:
            db_manager.add_user(address, token)
        return token

    @staticmethod
    @methods.add
    async def set_nickname(**kwargs):
        """

        :param kwargs:
        token:
        nickname:
        :return:

        """
        token = kwargs.get('token')
        address = utils.get_address_from_token(token)
        nickname = kwargs.get('nickname')
        db_manager.update_nickname(address, nickname)

        return "success"

    @staticmethod
    @methods.add
    async def get_nickname(**kwargs):
        """

        :param kwargs:
        token:
        :return:
        nickname
        """
        address = utils.get_address_from_token(kwargs.get('token'))
        nickname = db_manager.get_nickname_by_address(address)
        return nickname
