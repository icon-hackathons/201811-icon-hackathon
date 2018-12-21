class MockKeyValueDatabase(object):

    def __init__(self, db: dict) -> None:
        """Constructor

        :param db: plyvel db instance
        """
        self._db : dict = db

    def get(self, key: bytes) -> bytes:
        """Get value from db using key

        :param key: db key
        :return: value indicated by key otherwise None
        """
        try:
            return self._db[key]
        except KeyError:
            return None

    def put(self, key: bytes, value: bytes) -> None:
        """Put value into db using key.

        :param key: (bytes): db key
        :param value: (bytes): db에 저장할 데이터
        """
        self._db[key] = value

    def delete(self, key: bytes) -> None:
        """Delete a row

        :param key: delete the row indicated by key.
        """
        self._db.pop(key)

    def close(self) -> None:
        """Close db
        """
        self._db = None

    def get_sub_db(self, key: bytes):
        """Get Prefixed db

        :param key: (bytes): prefixed_db key
        """
        return MockKeyValueDatabase(self._db[key])

    def iterator(self) -> iter:
        return self._db.items()

    def write_batch(self, states: dict) -> None:
        """bulk data modification

        :param states: key:value pairs
            key and value should be bytes type
        """
        print(states)
