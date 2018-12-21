import asyncio
import json
import unittest
from threading import Thread

import websockets
from jsonrpcclient.clients.http_client import HTTPClient

import utils
from app import app
from config import CONFIG

user_client = HTTPClient(CONFIG.http_uri + '/users')
v3_client = HTTPClient(CONFIG.v3_uri)
address1, private_key1 = utils.create_new_address_and_privkey()
address2, private_key2 = utils.create_new_address_and_privkey()


class TestWebsocketClient(unittest.TestCase):
    def test_index_returns_200(self):
        request, response = app.test_client.get('/')
        self.assertEqual(response.status, 200)

    def test_websocket_hello(self):
        loop = asyncio.new_event_loop()
        nickname = loop.run_until_complete(self.hello())

        self.assertEqual(nickname, 'ICONDICE websocket')

    async def hello(self):
        uri = CONFIG.ws_uri + '/hello'
        async with websockets.connect(uri) as websocket:
            await websocket.send('hello')
            nickname = await websocket.recv()

        return nickname

    def test_websocket_game(self):
        player1_thread = Thread(target=self._run, args=(address1, private_key1, ))
        player1_thread.start()

        player2_thread = Thread(target=self._run, args=(address2, private_key2, ))
        player2_thread.start()

        player1_thread.join()
        player2_thread.join()

    def _run(self, address, private_key):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.create_task(self.game(address, private_key))
        loop.run_forever()

    async def game(self, address, private_key):
        token = await utils.get_token_from_login_process(address, private_key)
        print(f"token: {token}")

        uri = CONFIG.ws_uri + '/game'
        async with websockets.connect(uri) as websocket:
            # round 1
            await websocket.send(token)
            response1 = json.loads(await websocket.recv())

            game_room_id = response1.get('game_room_id')
            opposite_address = response1.get('opposite_address')
            opposite_nickname = response1.get('opposite_nickname')
            print(f"game_room_id: {game_room_id}, "
                  f"opposite_address: {opposite_address}, "
                  f"opposite_nick: {opposite_nickname}")

            # round 2
            # params, random = utils.get_start_game_params(address1, game_room_id)
            # print(f"params: {params}, random: {random}")

        async def _stop():
            loop.stop()

        loop = asyncio.get_event_loop()
        loop.create_task(_stop())

        return response1

    def test_v3(self):
        last_block_response = v3_client.request(method_name='icx_getLastBlock')
        print(last_block_response.text, type(last_block_response.text))
