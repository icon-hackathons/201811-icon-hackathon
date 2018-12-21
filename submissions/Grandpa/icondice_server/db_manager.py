import leveldb
import json
from config import CONFIG


class DBManager:
    def __init__(self, db: leveldb.LevelDB):
        self.__db = db
        self.__user_data = dict()  # {address: {'token': [token], 'nickname': [nickname]}}
        self.__update_user_data_from_db()

    @property
    def user_data(self):
        return self.__user_data

    def __update_user_data_from_db(self):
        self.__user_data = {address.decode('utf-8'): json.loads(info.decode('utf-8'))
                            for address, info in self.__db.RangeIter()}

    def get_tokens(self) -> list:
        tokens = [info['token'] for address, info in self.__user_data.items()]
        return tokens

    def get_addresses(self) -> list:
        return list(self.__user_data)

    def add_user(self, address, token, nickname=''):
        user_info = {
            'token': token,
            'nickname': nickname
        }
        self.__user_data[address] = user_info
        self.__db.Put(address.encode('utf-8'),
                      json.dumps(user_info).encode('utf-8'))

    def update_token(self, address, token):
        self.__user_data[address]['token'] = token
        new_user_info = self.__user_data[address]

        self.__db.Put(address.encode('utf-8'),
                      json.dumps(new_user_info).encode('utf-8'))

    def update_nickname(self, address, nickname):
        self.__user_data[address]['nickname'] = nickname
        new_user_info = self.__user_data[address]

        self.__db.Put(address.encode('utf-8'),
                      json.dumps(new_user_info).encode('utf-8'))

    def get_nickname_by_address(self, address):
        return self.__user_data[address]['nickname']


DB = leveldb.LevelDB(CONFIG.db_path)
db_manager = DBManager(DB)
