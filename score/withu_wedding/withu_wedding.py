from iconservice import *

TAG = 'WithUWedding'


class IWeddingManager(InterfaceScore):
    @interface
    def set_wedding_score_address_from_contract(self, wedding_score: Address):
        pass

    @interface
    def get_wedding_score_address(self, owner: Address) -> str:
        pass

    @interface
    def get_token_address(self) -> Address:
        pass


class IToken(InterfaceScore):
    @interface
    def transfer(self, _to: Address, _value: int, _data: bytes=None):
        pass


class Guests:
    _NAME = 'name'
    _AMOUNT = 'amount'
    _HASH = 'hash'
    _MESSAGE = 'message'
    _TIMESTAMP = 'timestamp'
    _ADDRESS = 'address'
    _SECRET = 'secret'

    @property
    def _address_array(self) -> ArrayDB:
        return ArrayDB(self.__name+self._ADDRESS+'.array', self.__db, Address)

    def __init__(self, db: IconScoreDatabase, name: str):
        self.__db = db
        self.__name = name
        self._address_dict = DictDB(self.__name+self._ADDRESS+'.dict', self.__db, bool)
        self._name = DictDB(self.__name+self._NAME, self.__db, str)
        self._amount = DictDB(self.__name+self._AMOUNT, self.__db, int)
        self._hash = DictDB(self.__name+self._HASH, self.__db, bytes)
        self._timestamp = DictDB(self.__name+self._TIMESTAMP, self.__db, int)
        self._message = DictDB(self.__name+self._MESSAGE, self.__db, str)
        self._secret = DictDB(self.__name+self._SECRET, self.__db, int)

    def put(self, guest_info: dict):
        Logger.info(f'>>>>>>>>>>>>> put:{guest_info}')
        address = guest_info['address']
        if not self._address_dict[address]:
            self._address_array.put(address)
            self._address_dict[address] = True
            self._name[address] = guest_info['name']
            self._message[address] = guest_info['message']
            self._hash[address] = guest_info['hash']
            self._timestamp[address] = guest_info['timestamp']
            self._amount[address] = guest_info['amount']
            self._secret[address] = guest_info['secret']

    def find(self, address: Address) -> dict:
        if self._address_dict[address]:
            return {
                'name': self._name[address],
                'address': address,
                'message': self._message[address],
                'hash': self._hash[address],
                'timestamp': self._timestamp[address],
                'amount': self._amount[address],
                'secret': self._secret[address]
            }
        return dict()

    def get(self, offset: int, count: int) -> list:
        Logger.info(f'>>>>>>>>>>>>> offset:{offset}, count:{count}')
        data = []
        count_of_guests = self.get_count()
        if 0 <= offset < count_of_guests:
            if offset + count > count_of_guests:
                count = count_of_guests - offset
            for i in range(count):
                address = self._address_array[offset + i]
                data.append({
                    'name': self._name[address],
                    'address': address,
                    'message': self._message[address],
                    'hash': self._hash[address],
                    'timestamp': self._timestamp[address],
                    'amount': self._amount[address],
                    'secret': self._secret[address]
                })
        return data

    def get_count(self) -> int:
        return len(self._address_array)


class MealTicket:
    _TOTAL_AMOUNT = 'total_amount'
    _DISTRIBUTE_AMOUNT = 'distribute_amount'
    _TOTAL_DISTRIBUTE_AMOUNT = 'total_distribute_amount'
    _RETURN_AMOUNT = 'return_amount'
    _TOTAL_RETURN_AMOUNT = 'total_return_amount'
    _MAX_DISTRIBUTED_AMOUNT = 'max_distributed_amount'

    def __init__(self, db: IconScoreDatabase, name: str, total_amount: int = 500, max_distributed_amount: int = 10):
        self._total_amount = VarDB(name+':'+self._TOTAL_AMOUNT, db, int)
        self._distribute_amount = DictDB(name+':'+self._DISTRIBUTE_AMOUNT, db, int)
        self._return_amount = DictDB(name+':'+self._RETURN_AMOUNT, db, int)
        self._total_distribute_amount = VarDB(name+':'+self._TOTAL_DISTRIBUTE_AMOUNT, db, int)
        self._total_return_amount = VarDB(name+':'+self._TOTAL_RETURN_AMOUNT, db, int)
        self._max_distributed_amount = VarDB(name+':'+self._MAX_DISTRIBUTED_AMOUNT, db, int)
        self._total_amount.set(total_amount)
        self._max_distributed_amount.set(max_distributed_amount)

    def information(self) -> dict:
        return {
            'total_amount': self._total_amount.get(),
            'total_distribute_amount': self._total_distribute_amount.get(),
            'total_return_amount': self._total_return_amount.get(),
            'remaining_amount': self._get_remaining_ticket(),
        }

    def set_total_amount(self, total_amount: int):
        self._total_amount.set(total_amount)

    def set_max_distributed_amount(self, max_distributed_amount: int):
        self._max_distributed_amount.set(max_distributed_amount)

    def _get_remaining_ticket(self) -> int:
        return self._total_amount.get() - self._total_distribute_amount.get()

    def get_ticket_count(self, account: Address) -> int:
        return self._distribute_amount[account]

    def distribute(self, account: Address, amount: int):
        remaining_ticket = self._get_remaining_ticket()
        if remaining_ticket > 0:
            amount_distribution = WithUWedding.min(remaining_ticket, amount)
            amount_distribution = WithUWedding.min(amount_distribution, self._max_distributed_amount.get())
            self._distribute_amount[account] += amount_distribution
            self._increase_amount_distributed(amount_distribution)
            Logger.info(f'>>>>>>>>>>>>> distributed mealticket:{account}, amount:{amount_distribution}')
        else:
            Logger.error('>>>>>>>>>>>>> remaining_ticket == 0')

    def return_ticket(self, account: Address, amount: int):
        distributed_amount = self._distribute_amount[account]
        if distributed_amount > 0:
            amount_return = WithUWedding.min(distributed_amount, amount)
            self._return_amount[account] += amount_return
            self._distribute_amount[account] -= amount_return
            self._increase_amount_returned(amount_return)
            Logger.info(f'>>>>>>>>>>>>> returned meal ticket:{account}, amount:{amount_return}')

    def _increase_amount_distributed(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._total_distribute_amount.set(self._total_distribute_amount.get() + amount)

    def _increase_amount_returned(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._total_return_amount.set(self._total_return_amount.get() + amount)


class WithUWedding(IconScoreBase):
    _GROOM_NAME = 'groom_name'
    _BRIDE_NAME = 'bride_name'
    _GROOM_FATHER_NAME = 'groom_father_name'
    _GROOM_MOTHER_NAME = 'groom_mother_name'
    _BRIDE_FATHER_NAME = 'bride_father_name'
    _BRIDE_MOTHER_NAME = 'bride_mother_name'
    _INVITATION_MESSAGE = 'invitation_message'
    _WEDDING_DATE = 'wedding_date'
    _WEDDING_DATE_STR = 'wedding_date_str'
    _WEDDING_PLACE_NAME = 'wedding_place_name'
    _WEDDING_PLACE_ADDRESS = 'wedding_place_address'
    _WEDDING_PLACE_MAP_URL = 'wedding_place_map_url'
    _WEDDING_PHOTO_URL = 'wedding_photo_url'
    _WEDDING_MANAGER = 'wedding_manager'
    _PUBLIC_KEY = 'public_key'
    _MEAL_TICKET_COUNT = 'meal_ticket_count'
    _MEAL_TICKET = '_meal_ticket'
    _TOTAL_GUESTS = '_total_guests'
    _GROOM_GUESTS = '_groom_guests'
    _BRIDE_GUESTS = '_bride_guests'
    _TOKEN_ADDRESS = '_token_address'
    _DISTRIBUTE_TOKEN_AMOUNT = '_distribute_token_amount'
    _WITHDRAW_AMOUNT = '_withdraw_amount'
    _AMOUNT_RAISED = 'amount_raised'

    _DEFAULT_KEYS = [_GROOM_NAME, _BRIDE_NAME, _GROOM_FATHER_NAME,
                     _GROOM_MOTHER_NAME, _BRIDE_FATHER_NAME, _BRIDE_MOTHER_NAME, _INVITATION_MESSAGE,
                     _WEDDING_DATE, _WEDDING_PLACE_NAME, _WEDDING_PLACE_ADDRESS,
                     _WEDDING_PLACE_MAP_URL, _WEDDING_PHOTO_URL, _WEDDING_DATE_STR]

    @property
    def _total_guests(self) -> ArrayDB:
        return ArrayDB(self._TOTAL_GUESTS, self.db, Address)

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self._wedding_manager = VarDB(self._WEDDING_MANAGER, db, value_type=Address)
        self._groom_name = VarDB(self._GROOM_NAME, db, value_type=str)
        self._bride_name = VarDB(self._BRIDE_NAME, db, value_type=str)
        self._groom_father_name = VarDB(self._GROOM_FATHER_NAME, db, value_type=str)
        self._groom_mother_name = VarDB(self._GROOM_MOTHER_NAME, db, value_type=str)
        self._bride_father_name = VarDB(self._BRIDE_FATHER_NAME, db, value_type=str)
        self._bride_mother_name = VarDB(self._BRIDE_MOTHER_NAME, db, value_type=str)
        self._invitation_message = VarDB(self._INVITATION_MESSAGE, db, value_type=str)
        self._wedding_place_name = VarDB(self._WEDDING_PLACE_NAME, db, value_type=str)
        self._wedding_place_address = VarDB(self._WEDDING_PLACE_ADDRESS, db, value_type=str)
        self._wedding_place_map_url = VarDB(self._WEDDING_PLACE_MAP_URL, db, value_type=str)
        self._wedding_photo_url = VarDB(self._WEDDING_PHOTO_URL, db, value_type=str)
        self._wedding_date = VarDB(self._WEDDING_DATE, db, value_type=str)
        self._wedding_date_str = VarDB(self._WEDDING_DATE_STR, db, value_type=str)
        self._public_key = VarDB(self._PUBLIC_KEY, db, value_type=bytes)
        self._meal_ticket = MealTicket(db, self._MEAL_TICKET)
        self._groom_guests = Guests(db, self._GROOM_GUESTS)
        self._bride_guests = Guests(db, self._BRIDE_GUESTS)
        self._token_address = VarDB(self._TOKEN_ADDRESS, db, value_type=Address)
        self._distribute_token_amount = VarDB(self._DISTRIBUTE_TOKEN_AMOUNT, db, value_type=int)
        self._meal_ticket_count = VarDB(self._MEAL_TICKET_COUNT, db, value_type=int)
        self._withdraw_amount = VarDB(self._WITHDRAW_AMOUNT, db, int)
        self._amount_raised = VarDB(self._AMOUNT_RAISED, db, int)

    def on_install(self, information_json: str, manager_score: Address,
                   meal_ticket_count: int, public_key: bytes) -> None:
        super().on_install()
        self._precondition(manager_score.is_contract)
        wedding_information: dict = json_loads(information_json)
        self._set_information(wedding_information)
        self._wedding_manager.set(manager_score)
        self._get_manager_score().set_wedding_score_address_from_contract(self.address)
        self._meal_ticket.set_total_amount(meal_ticket_count)
        self._public_key.set(public_key)

    def on_update(self) -> None:
        super().on_update()

    def _get_manager_score(self) -> IWeddingManager:
        """

        :return: score interface
        """
        Logger.info(f'>>>>>>>>>>>>> manager : {self._wedding_manager.get()}')
        return self.create_interface_score(self._wedding_manager.get(), IWeddingManager)

    def _set_information(self, wedding_information: dict):
        _information_db: dict = self._information_db()
        for key in wedding_information.keys():
            if self._check_information_key(key):
                Logger.info(f'>>>>>>>>>>>>> key {key}, value :{wedding_information[key]}')
                _information_db[key].set(wedding_information[key])

    def _information_db(self) -> dict:
        return {
            self._GROOM_NAME: self._groom_name,
            self._BRIDE_NAME: self._bride_name,
            self._GROOM_FATHER_NAME: self._groom_father_name,
            self._GROOM_MOTHER_NAME: self._groom_mother_name,
            self._BRIDE_FATHER_NAME: self._bride_father_name,
            self._BRIDE_MOTHER_NAME: self._bride_mother_name,
            self._INVITATION_MESSAGE: self._invitation_message,
            self._WEDDING_PLACE_NAME: self._wedding_place_name,
            self._WEDDING_PLACE_ADDRESS: self._wedding_place_address,
            self._WEDDING_PLACE_MAP_URL: self._wedding_place_map_url,
            self._WEDDING_DATE: self._wedding_date,
            self._WEDDING_DATE_STR: self._wedding_date_str,
            self._MEAL_TICKET_COUNT: self._meal_ticket_count,
            self._PUBLIC_KEY: self._public_key,
            self._WEDDING_PHOTO_URL: self._wedding_photo_url
        }

    @external(readonly=True)
    def get_public_key(self) -> bytes:
        if self._public_key.get():
            return self._public_key.get()
        return bytes()

    @external
    def set_public_key(self, public_key: bytes):
        self._precondition(self.msg.sender == self.owner)
        self._public_key.set(public_key)

    @external(readonly=True)
    def information(self) -> dict:
        information = {}
        _information_db: dict = self._information_db()
        for key, value in _information_db.items():
            information[key] = value.get()
        return information

    def _check_information_key(self, key: str) -> bool:
        for default_key in self._DEFAULT_KEYS:
            if key == default_key:
                return True
        return False

    @external
    def change_information(self, information_json: str):
        """
        :param information_json: json
            • groom_name :
            • bride_name :
            • groom_father_name :
            • groom_mother_name :
            • bride_father_name :
            • bride_mother_name :
            • invitation_message :
            • wedding_place_name :
            • wedding_place_address :
            • wedding_place_map_url :
            • wedding_date :
        :return: none
        """
        wedding_information: dict = json_loads(information_json)
        _information_db: dict = self._information_db()
        for key in wedding_information.keys():
            if self._check_information_key(key):
                _information_db[key].set(wedding_information[key])

    @external(readonly=True)
    def get_meal_ticket_info(self) -> dict:
        return self._meal_ticket.information()

    @external(readonly=True)
    def get_meal_ticket_count(self, account: Address) -> int:
        return self._meal_ticket.get_ticket_count(account)

    @external(readonly=True)
    def get_groom_guests(self, offset: int, count: int) -> list:
        self._precondition(count <= self.get_max_iteration())
        return self._groom_guests.get(offset, count)

    @external(readonly=True)
    def get_groom_guests_count(self) -> int:
        return self._groom_guests.get_count()

    @external(readonly=True)
    def get_bride_guests(self, offset: int, count: int) -> list:
        self._precondition(count <= self.get_max_iteration())
        return self._bride_guests.get(offset, count)

    @external(readonly=True)
    def get_bride_guests_count(self) -> int:
        return self._bride_guests.get_count()

    @external(readonly=True)
    def find_in_guests(self, address: Address) -> dict:
        if self._groom_guests.find(address):
            return self._groom_guests.find(address)
        else:
            return self._bride_guests.find(address)

    @external(readonly=True)
    def get_amount_raised(self) -> int:
        return self._amount_raised.get()

    @external(readonly=True)
    def get_guests_count(self) -> int:
        return len(self._total_guests)

    @external(readonly=True)
    def get_messages(self, offset: int, count: int) -> list:
        self._precondition(count <= self.get_max_iteration())
        data = []
        count_of_guests = self.get_guests_count()
        Logger.info(f'>>>>>>>>>>>>> get_messages count: {count_of_guests}')
        if 0 <= offset < count_of_guests:
            if offset + count > count_of_guests:
                count = count_of_guests - offset
            for i in range(count):
                address = self._total_guests[offset + i]
                guest = self.find_in_guests(address)
                data.append({
                    'name': guest['name'],
                    'message': guest['message'],
                    'hash': guest['hash']
                })
        return data

    @external
    def return_meal_ticket(self, account: Address):
        self._precondition(self.msg.sender == account or
                           self.msg.sender == self.get_owner(self._wedding_manager.get()))
        amount = self._meal_ticket.get_ticket_count(account)
        if amount > 0:
            self._meal_ticket.return_ticket(account, amount)

    @payable
    def fallback(self):
        self.revert(f'Please use icon service')

    @payable
    @external
    def congratulation(self, guest_information_json: str):
        sender = self.msg.sender
        value = self.msg.value
        self._precondition(not sender.is_contract and value >= 1000000000000000000, 'Sender is not contract or value > 0')
        self._precondition(not bool(self.find_in_guests(sender)), 'You already paid')
        Logger.info(f'>>>>>>>>>>>>> congratulation sender:{sender}, value:{value}')
        data = json_loads(guest_information_json)
        guest_info = {
            'name': data['name'],
            'address': self.msg.sender,
            'amount': self.msg.value,
            'hash': self.tx.hash,
            'message': data['message'],
            'timestamp': self.tx.timestamp,
            'secret': data['secret']
        }
        self._total_guests.put(sender)
        self._amount_raised.set(self._amount_raised.get() + value)
        if data['attend']:
            ticket_amount = int(data['ticket_amount'])
            self._meal_ticket.distribute(sender, ticket_amount)
        if data['host'] == "0" or data['host'] == 0:
            self._groom_guests.put(guest_info)
        else:
            self._bride_guests.put(guest_info)
        if self._distribute_token_amount.get() > 0:
            token_score = self.create_interface_score(self._get_manager_score().get_token_address(), IToken)
            token_score.transfer(sender, self._distribute_token_amount.get(), b'called from Wedding score')

    @external
    def set_token_address(self, token_score: Address):
        self._token_address.set(token_score)

    @external(readonly=True)
    def get_token_address(self) -> str:
        if self._token_address.get():
            return self._token_address.get()
        return "cx"

    @external
    def set_distribute_token_amount(self, value: int):
        self._distribute_token_amount.set(value)

    @external(readonly=True)
    def get_distribute_token_amount(self) -> int:
        return self._distribute_token_amount.get()

    @external
    def withdraw(self, account: Address):
        self._precondition(self.msg.sender == self.owner)
        amount = self.icx.get_balance(self.address)
        self._precondition(0 < amount, f'Out of balance')
        self.icx.transfer(account, amount)
        self._withdraw_amount.set(self._withdraw_amount.get() + amount)

    @external(readonly=True)
    def get_withdraw_amount(self) -> int:
        return self._withdraw_amount.get()

    def _precondition(self, condition: bool, message: str=None):
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)

    @external
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        self._precondition(self.msg.sender == self._get_manager_score().get_token_address(),
                           "Unknown token address")
        Logger.debug(f'tokenFallback: token supply = "{_value}"')

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a <= b else b

    @external(readonly=True)
    def get_max_iteration(self) -> int:
        return 1000