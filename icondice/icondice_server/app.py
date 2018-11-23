from sanic import Sanic
from sanic.request import Request
from sanic.response import json, HTTPResponse
from sanic_session import InMemorySessionInterface

from dispatcher.game_dispatcher import GameDispatcher
from dispatcher.user_dispatcher import UserDispatcher
from db_manager import db_manager

app = Sanic(__name__)
app.add_route(UserDispatcher.dispatch, '/users', methods=['POST'])
app.add_websocket_route(GameDispatcher.game, '/game')
app.add_websocket_route(GameDispatcher.hello, '/hello')
app.session_interface = InMemorySessionInterface()


@app.route('/')
async def index(_request: Request) -> HTTPResponse:
    return json({"Hello": "ICONDICE world"})


@app.route('/db')
async def db(_request: Request):
    return json(db_manager.user_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
