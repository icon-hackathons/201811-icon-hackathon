from iconservice import *


class IconTokenStandard(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def decimals(self) -> int:
        pass

    @abstractmethod
    def totalSupply(self) -> int:
        pass

    @abstractmethod
    def balanceOf(self, _owner: Address) -> int:
        pass

    @abstractmethod
    def transfer(self, _to: Address, _value: int, _data: bytes=None):
        pass


class ITokenApis(IconTokenStandard):

    @abstractmethod
    def information(self) -> dict:
        """

        :return: dict
            • score_version
            • name
            • symbol
            • amount (in decimals)
            • decimals
        """
        pass

    @abstractmethod
    def get_max_iteration(self) -> int:
        """

        :return: max iteration
        """
        pass

    @abstractmethod
    def get_free_balance(self, owner: Address) -> int:
        """

        :param owner: token owner
        :return: unlocked token balance in decimals
        """
        pass

    @abstractmethod
    def get_frozen_balance(self, owner: Address) -> int:
        """

        :param owner: token owner
        :return: locked token balance in decimals
        """
        pass

    @abstractmethod
    def airdrops(self, formatted_json: str, data: bytes=None):
        """

        :param formatted_json: json array
            • account : account address
            • amount : token amount in decimals
        :param data: data
        :return: none
        """
        pass

    @abstractmethod
    def distribute(self, account: Address, amount: int, data: bytes=None) -> bool:
        """

        :param account: account address
        :param amount: token amount in decimals
        :param data: data
        :return: true if succeeded, otherwise false
        """
        pass

    @abstractmethod
    def dispossess(self, account: Address, amount: int, data: bytes=None) -> bool:
        """

        :param account: token owner
        :param amount: token amount in decimals
        :param data: data
        :return: true if succeeded, otherwise false
        """
        pass

    @abstractmethod
    def unlock(self, account: Address, amount: int) -> bool:
        """
        • A.K.A. UNLOCK
        :param account: token owner
        :param amount: token amount in decimals
        :return: true if succeeded, otherwise false
        """
        pass

    @abstractmethod
    def mint(self, amount: int):
        """

        :param amount: token amount in decimals
        :param amount: token amount in decimals
        :return: none
        """
        pass

    @abstractmethod
    def burn(self, account: Address, amount: int):
        """

        :param account: token owner
        :param amount: token amount in decimals
        :return: none
        """
        pass

    @abstractmethod
    def is_broker(self, broker: Address) -> bool:
        """
        • BROKER: A.K.A. CROWD SALE, RULE
        :param broker: score address
        :return: true if broker, otherwise false
        """
        pass

    @abstractmethod
    def count_of_brokers(self) -> int:
        """

        :return: count of brokers
        """
        pass

    @abstractmethod
    def get_brokers(self) -> list:
        """

        :return: broker addresses
        """
        pass

    @abstractmethod
    def get_some_brokers(self, offset: int, count: int) -> dict:
        """

        :param offset: zero based start index
        :param count: count
        :return: dict
            • success (boolean)
            • brokers (optional: array)
        """
        pass

    @abstractmethod
    def attach_broker(self, broker: Address):
        """

        :param broker: broker address
        :return: none
        """
        pass

    @abstractmethod
    def detach_broker(self, broker: Address):
        """

        :param broker: broker address
        :return: none
        """
        pass


class IScore(InterfaceScore):

    @interface
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        pass


EOA_ZERO = Address.from_string('hx' + '0' * 40)

MAX_ITERATION = 1000


class IconScoreToken(IconScoreBase, ITokenApis):

    __SCORE_VERSION = 'v1.00'

    @property
    def _context__brokers(self) -> ArrayDB:
        return ArrayDB('context.brokers', self.db, Address)

    def __init__(self, db: IconScoreDatabase):
        super().__init__(db)
        self._context__name = VarDB('context.name', db, str)
        self._context__symbol = VarDB('context.symbol', db, str)
        self._context__amount_in_decimals = VarDB('context.amount_in_decimals', db, int)  # AMOUNT * 10 ** DECIMALS
        self._context__decimals = VarDB('context.decimals', db, int)  # EXPONENT
        # self._context__brokers = ArrayDB('context.brokers', db, Address)  # AKA. RULE CONTRACTS
        self._context__free_balances = DictDB('context.free_balances.dict:address', db, int)
        self._context__frozen_balances = DictDB('context.frozen_balances.dict:address', db, int)

    def on_install(self, name: str, symbol: str, amount: int, decimals: int):
        """

        :param name: token name
        :param symbol: token symbol
        :param amount: token amount (not in decimals)
        :param decimals: exponent
        :return: none
        """
        super().on_install()
        self._precondition(amount >= 0)
        self._precondition(decimals >= 0)
        amount_in_decimals = amount * 10 ** decimals
        self._context__name.set(name)
        self._context__symbol.set(symbol)
        self._context__amount_in_decimals.set(amount_in_decimals)
        self._context__decimals.set(decimals)
        self._context__free_balances[self.owner] = amount_in_decimals

    def on_update(self):
        """

        :return: none
        """
        super().on_update()

    # ==================================================================================================================
    #
    # ==================================================================================================================

    def _precondition(self, condition: bool, message: str=None):
        """

        :param condition: condition
        :param message: message
        :return: none
        """
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)

    # ==================================================================================================================
    # IconTokenStandard
    # ==================================================================================================================

    @external(readonly=True)
    def name(self) -> str:
        return self._context__name.get()

    @external(readonly=True)
    def symbol(self) -> str:
        return self._context__symbol.get()

    @external(readonly=True)
    def decimals(self) -> int:
        return self._context__decimals.get()

    @external(readonly=True)
    def totalSupply(self) -> int:
        return self._context__amount_in_decimals.get()

    @external(readonly=True)
    def balanceOf(self, _owner: Address) -> int:
        return self.get_free_balance(_owner) + self.get_frozen_balance(_owner)

    @external
    def transfer(self, _to: Address, _value: int, _data: bytes=None):
        """

        :param _to: destination address
        :param _value: token amount in decimals
        :param _data: additional data
        :return: none
        """
        sender_free_balance = self._context__free_balances[self.msg.sender]
        self._precondition(0 < _value <= sender_free_balance)
        self._context__free_balances[self.msg.sender] = sender_free_balance - _value
        self._context__free_balances[_to] += _value
        data = b'None' if _data is None else _data
        if _to.is_contract:
            score = self.create_interface_score(_to, IScore)
            score.tokenFallback(self.msg.sender, _value, data)
        self.Transfer(self.msg.sender, _to, _value, data)

    # ==================================================================================================================
    # ITokenApis
    # ==================================================================================================================

    @external(readonly=True)
    def information(self) -> dict:
        """

        :return: dict
            • score_version
            • name
            • symbol
            • amount (in decimals)
            • decimals
        """
        return {
            'score_version': self.__SCORE_VERSION,
            'name': self._context__name.get(),
            'symbol': self._context__symbol.get(),
            'amount': self._context__amount_in_decimals.get(),
            'decimals': self._context__decimals.get()
        }

    @external(readonly=True)
    def get_max_iteration(self) -> int:
        """

        :return: max iteration
        """
        return MAX_ITERATION

    @external(readonly=True)
    def get_free_balance(self, owner: Address) -> int:
        """

        :param owner: token owner
        :return: unlocked token balance in decimals
        """
        return self._context__free_balances[owner]

    @external(readonly=True)
    def get_frozen_balance(self, owner: Address) -> int:
        """

        :param owner: token owner
        :return: locked token balance in decimals
        """
        return self._context__frozen_balances[owner]

    @external
    def airdrops(self, formatted_json: str, data: bytes=None):
        """

        :param formatted_json: json array (e.g. '[{"account":"address_1", "amount":10}, {...}]')
            • account: account address
            • amount: token amount in decimals
        :param data: data
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        obj = {
            'amounts': 0,
            'participants': list()
        }
        param = json_loads(formatted_json)
        param_size = len(param)
        self._precondition(0 < param_size <= self.get_max_iteration())
        for i in range(param_size):
            account = Address.from_string(param[i]['account'])
            amount = int(param[i]['amount'])
            self._precondition(not account.is_contract and amount > 0)
            obj['amounts'] += amount
            obj['participants'].append({
                'account': account,
                'amount': amount
            })
        balance = self._context__free_balances[self.msg.sender]
        self._precondition(0 < obj['amounts'] <= balance)
        data = b'airdropped' if data is None else data
        for i in range(param_size):
            account = obj['participants'][i]['account']
            amount = obj['participants'][i]['amount']
            self._context__free_balances[self.msg.sender] -= amount
            self._context__free_balances[account] += amount
            self.Transfer(self.msg.sender, account, amount, data)

    @external
    def distribute(self, account: Address, amount: int, data: bytes=None) -> bool:
        """

        :param account: account address
        :param amount: token amount in decimals
        :param data: data
        :return: true if succeeded, otherwise false
        """
        if not account.is_contract:
            if self.is_broker(self.msg.sender):
                sender_free_balance = self._context__free_balances[self.msg.sender]
                if 0 < amount <= sender_free_balance:
                    self._context__free_balances[self.msg.sender] = sender_free_balance - amount
                    self._context__frozen_balances[account] += amount
                    self.Transfer(self.msg.sender, account, amount, b'distributed' if data is None else data)
                    return True
        return False

    @external
    def dispossess(self, account: Address, amount: int, data: bytes=None) -> bool:
        """

        :param account: token owner
        :param amount: token amount in decimals
        :param data: data
        :return: true if succeeded, otherwise false
        """
        if self.is_broker(self.msg.sender):
            owner_frozen_balance = self._context__frozen_balances[account]
            if 0 < amount <= owner_frozen_balance:
                self._context__free_balances[self.msg.sender] += amount
                self._context__frozen_balances[account] = owner_frozen_balance - amount
                self.Transfer(account, self.msg.sender, amount, b'dispossess' if data is None else data)
                return True
        return False

    @external
    def unlock(self, account: Address, amount: int) -> bool:
        """
        • A.K.A. UNLOCK
        :param account: token owner
        :param amount: token amount in decimals
        :return: true if succeeded, otherwise false
        """
        if self.is_broker(self.msg.sender):
            owner_frozen_balance = self._context__frozen_balances[account]
            if 0 < amount <= owner_frozen_balance:
                self._context__free_balances[account] += amount
                self._context__frozen_balances[account] = owner_frozen_balance - amount
                self.EventUnlocked(account, amount)
                return True
        return False

    @external
    def mint(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(amount > 0)
        self._context__free_balances[self.owner] += amount
        self._context__amount_in_decimals.set(self._context__amount_in_decimals.get() + amount)

        self.Transfer(EOA_ZERO, self.owner, amount, b'mint')

    @external
    def burn(self, account: Address, amount: int):
        """

        :param account: token owner
        :param amount: token amount in decimals
        :return: none
        """

        self._precondition(self.msg.sender == self.owner)

        owner_free_balance = self._context__free_balances[account]
        amount_in_decimals = self._context__amount_in_decimals.get()

        self._precondition(0 < amount <= owner_free_balance <= amount_in_decimals)
        self._context__free_balances[account] = owner_free_balance - amount
        self._context__amount_in_decimals.set(amount_in_decimals - amount)

        self.Transfer(account, EOA_ZERO, amount, b'burn')

    @external(readonly=True)
    def is_broker(self, broker: Address) -> bool:
        """
        • BROKER: A.K.A. CROWD SALE, RULE
        :param broker: score address
        :return: true if broker, otherwise false
        """
        return broker.is_contract and broker in self._context__brokers

    @external(readonly=True)
    def count_of_brokers(self) -> int:
        """

        :return: count of brokers
        """
        return len(self._context__brokers)

    @external(readonly=True)
    def get_brokers(self) -> list:
        """

        :return: broker addresses
        """
        return [broker for broker in self._context__brokers]

    @external(readonly=True)
    def get_some_brokers(self, offset: int, count: int) -> dict:
        """

        :param offset: zero based start index
        :param count: count
        :return: dict
            • success (boolean)
            • brokers (optional: array)
        """
        success, data = False, []
        count_of_brokers = len(self._context__brokers)
        if 0 < count <= self.get_max_iteration():
            if 0 <= offset < count_of_brokers:
                if offset + count > count_of_brokers:
                    count = count_of_brokers - offset
                for i in range(count):
                    data.append(self._context__brokers[offset + i])
                success = True
        return {
            'success': success,
            'brokers': data
        }

    @external
    def attach_broker(self, broker: Address):
        """

        :param broker: broker address
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(broker.is_contract)

        if broker not in self._context__brokers:
            self._context__brokers.put(broker)
            self.EventBrokerAttached(broker)

    @external
    def detach_broker(self, broker: Address):
        """

        :param broker: broker address
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(broker.is_contract)

        top = self._context__brokers[-1]
        if top == broker:
            self._context__brokers.pop()
            self.EventBrokerDetached(broker)
        else:
            for i in range(len(self._context__brokers)):
                if self._context__brokers[i] == broker:
                    self._context__brokers[i] = top
                    self._context__brokers.pop()
                    self.EventBrokerDetached(broker)
                    break

    # ==================================================================================================================
    # EVENT
    # ==================================================================================================================

    @eventlog(indexed=3)
    def Transfer(self, _from: Address, _to: Address, _value: int, _data: bytes):
        pass

    # ------------------------------------------------------------------------------------------------------------------

    @eventlog(indexed=1)
    def EventUnlocked(self, account: Address, amount: int):
        pass

    @eventlog(indexed=1)
    def EventBrokerAttached(self, broker: Address):
        pass

    @eventlog(indexed=1)
    def EventBrokerDetached(self, broker: Address):
        pass

    # ==================================================================================================================
    # EOF
    # ==================================================================================================================
