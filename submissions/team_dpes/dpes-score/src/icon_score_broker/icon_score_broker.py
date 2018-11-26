from iconservice import *
from enum import IntEnum

class IBrokerApis(ABC):

    """
    BROKER: A.K.A. CROWDSALE
    """

    @abstractmethod
    def get_max_iteration(self) -> int:
        """

        :return: max iteration
        """
        pass

    @abstractmethod
    def information(self) -> dict:
        """

        :return: dict
            • score_version
            • name
            • score_cap (in loops, 1 icx = 1000000000000000000 loop)
            • exchange_rate (in millions)
            • start (timestamp in microseconds)
            • end (timestamp in microseconds)
            • account_min_cap (in loops, 1 icx = 1000000000000000000 loop)
            • account_max_cap (in loops, 1 icx = 1000000000000000000 loop)
            • deactivated
            • amount_raised (in loops, 1 icx = 1000000000000000000 loop)
            • count_of_investors
            • register_deactivated
        """
        pass

    @abstractmethod
    def get_exchange_rate(self) -> int:
        """

        :return: exchange rate (in millions)
        """
        pass

    @abstractmethod
    def set_name(self, name: str):
        """

        :param name: broker name
        :return: none
        """
        pass

    @abstractmethod
    def get_deactivation(self) -> bool:
        """

        :return: true if deactivated, otherwise false
        """
        pass

    @abstractmethod
    def deactivate(self, deactivation: bool):
        """

        :param deactivation: deactivating if true, otherwise activating
        :return: none
        """
        pass

    @abstractmethod
    def get_remaining_cap(self) -> int:
        """

        :return: remaining cap(score_cap - amount_raised) in loops
        """
        pass

    @abstractmethod
    def get_amount_raised(self) -> int:
        """

        :return: amount raised in loops
        """
        pass

    @abstractmethod
    def get_itemized_distribution_size(self) -> int:
        """

        :return: distribution size
        """
        pass

    @abstractmethod
    def get_itemized_distribution(self, indexes: str) -> dict:
        """

        :param indexes: distribution log index
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • amount_requested (icx amount in loops)
                • amount_accepted (icx amount in loops)
                • amount_distributed (token amount in decimals)
                • status (0:LOCKED, 1:REFUNDED, 2:UNLOCKED)
        """
        pass

    @abstractmethod
    def get_itemized_bonus_size(self) -> int:
        """

        :return: itemized bonus size
        """
        pass

    @abstractmethod
    def get_itemized_bonus(self, indexes: str) -> dict:
        """

        :param indexes: bonus index
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • account
                • bonus_rate (in millions)
                • amount (token amount in decimals)
                • amount_bonused (token amount in decimals)
                • status (0:LOCKED, 2:UNLOCKED)
        """
        pass

    @abstractmethod
    def get_itemized_airdrop_size(self) -> int:
        """

        :return: itemized airdrop size
        """
        pass

    @abstractmethod
    def get_itemized_airdrop(self, indexes: str) -> dict:
        """

        :param indexes: airdrop index
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • account
                • amount_airdropped (token amount in decimals)
                • status (0:LOCKED, 1:DISPOSSESSED, 2:UNLOCKED)
        """
        pass

    @abstractmethod
    def refund(self, indexes: str):
        """

        :param indexes: distribution indexes (comma separated)
        :return: none
        """
        pass

    @abstractmethod
    def unlock_distributed(self, indexes: str):
        """

        :param indexes: distribution indexes (comma separated)
        :return: none
        """
        pass

    @abstractmethod
    def unlock_bonused(self, indexes: str):
        """

        :param indexes: bonus indexes (comma separated)
        :return: none
        """
        pass

    @abstractmethod
    def unlock_airdropped(self, indexes: str):
        """

        :param indexes: airdrop indexes (comma separated)
        :return: none
        """
        pass

    @abstractmethod
    def bonus(self, rate: int, count: int):
        """

        :param rate: rate in millions
        :param count: count from bonus_offset
        :return: none
        """
        pass

    @abstractmethod
    def get_current_bonus_offset(self) -> int:
        """

        :return: current bonus offset
        """
        pass

    @abstractmethod
    def reset_bonus_offset(self, offset: int=0):
        """

        :param offset: offset
        :return: none
        """
        pass

    @abstractmethod
    def get_bonus_pending_count(self) -> int:
        """

        :return: bonus pending(remained) count
        """
        pass

    @abstractmethod
    def airdrop(self, accounts: str, amount: int):
        """

        :param accounts: account addresses (comma separated)
        :param amount: token amount in decimals
        :return: none
        """
        pass

    @abstractmethod
    def dispossess_broker_tokens(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        pass

    @abstractmethod
    def dispossess_bonused_tokens(self, index: int):
        """

        :param index: bonus index
        :return: none
        """
        pass

    @abstractmethod
    def dispossess_airdropped_tokens(self, index: int):
        """

        :param index: airdrop index
        :return: none
        """
        pass

    @abstractmethod
    def withdraw(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: icx amount in loops
        :return: none
        """
        pass

    @abstractmethod
    def get_amount_withdrew(self) -> int:
        """

        :return: amount withdrew in loops
        """
        pass

    @abstractmethod
    def get_investor_count(self) -> int:
        """

        :return: count of investors
        """
        pass

    @abstractmethod
    def get_investor(self, account: Address) -> dict:
        """

        :param account: account address
        :return: dict
            • amount_accepted (icx amount in loops)
            • amount_distributed (token amount in decimals)
            • amount_bonused (token amount in decimals)
        """
        pass

    @abstractmethod
    def get_investors(self, offset: int, count: int) -> list:
        """

        :param offset: zero based start index
        :param count: count
        :return: some investor addresses
        """
        pass

    @abstractmethod
    def get_register_deactivation(self) -> bool:
        """
        • REGISTER: A.K.A. WHITELIST
        :return: true if register deactivated, otherwise false
        """
        pass

    @abstractmethod
    def deactivate_register(self, deactivation: bool):
        """

        :param deactivation: deactivating if true, otherwise activating
        :return: none
        """
        pass

    @abstractmethod
    def get_register_size(self) -> int:
        """

        :return: count of registered accounts
        """
        pass

    @abstractmethod
    def find_in_register(self, account: Address) -> dict:
        """

        :param account: account address
        :return: dict
            • account (optional: account address)
            • min_cap (optional: minimum investable icx amounts in loops)
            • max_cap (optional: maximum investable icx amounts in loops)
        """
        pass

    @abstractmethod
    def get_accounts_in_register(self, offset: int, count: int) -> dict:
        """

        :param offset: zero based start offset
        :param count: count
        :return: dict
            • success (boolean)
            • data (optional: array)
                • dict
                    • account
                    • min_cap
                    • max_cap
        """
        pass

    @abstractmethod
    def put_accounts_to_register(self, conditions: str):
        """

        :param conditions: comma and pipe separated conditions, e.g. hx0…01|0|1,hx0…02|0|1, ...
        :return: none
        """
        pass


class IToken(InterfaceScore):

    @interface
    def transfer(self, _to: Address, _value: int, _data: bytes=None):
        pass

    @interface
    def is_broker(self, broker: Address) -> bool:
        pass

    @interface
    def decimals(self) -> int:
        pass

    @interface
    def get_free_balance(self, owner: Address) -> int:
        pass

    @interface
    def distribute(self, account: Address, amount: int, data: bytes=None) -> bool:
        pass

    @interface
    def dispossess(self, account: Address, amount: int):
        pass

    @interface
    def unlock(self, account: Address, amount: int) -> bool:
        pass


class Status(IntEnum):
    LOCKED = 0
    REFUNDED = 1
    UNLOCKED = 2
    DISPOSSESSED = 3


class Scope(IntEnum):
    DISTRIBUTION = 0
    BONUS = 1
    AIRDROP = 2


LOOP_DECIMALS = 18
LOOP = 10 ** LOOP_DECIMALS

MILLION = 10 ** 6
MAX_ITERATION = 5000


class IconScoreBroker(IconScoreBase, IBrokerApis):

    """
    A.K.A. CROWDSALE
    """

    __SCORE_VERSION = 'v0.64a'

    def __init__(self, db: IconScoreDatabase):
        """

        :param db:
        """

        super().__init__(db)

        # CONTEXT
        self._context__deactivation = VarDB('context.deactivation', db, bool)
        self._context__name = VarDB('context.name', db, str)
        self._context__score_cap = VarDB('context.score_cap', db, int)
        self._context__exchange_rate = VarDB('context.exchange_rate', db, int)
        self._context__start = VarDB('context.start', db, int)
        self._context__end = VarDB('context.end', db, int)
        self._context__account_min_cap = VarDB('context.account_min_cap', db, int)
        self._context__account_max_cap = VarDB('context.account_max_cap', db, int)
        self._context__amount_raised = VarDB('context.amount_raised', db, int)
        self._context__amount_distributed = VarDB('context.amount_distributed', db, int)
        self._context__amount_bonused = VarDB('context.amount_bonused', db, int)
        self._context__amount_airdropped = VarDB('context.amount_airdropped', db, int)
        self._context__amount_withdrew = VarDB('context.amount_withdrew', db, int)
        self._context__bonus_offset = VarDB('context.bonus_offset', db, int)

        # SCORE
        self._score__token_address = VarDB('score.token_address', db, Address)

        # REGISTER(A.K.A. WHITELIST)
        self._register__deactivation = VarDB('register.deactivation', db, bool)
        self._register__accounts = ArrayDB('register.accounts', db, Address)
        self._register__accounts_dict = DictDB('register.accounts.dict:address', db, bool)
        self._register__min_caps_dict = DictDB('register.min_caps.dict:address', db, int)
        self._register__max_caps_dict = DictDB('register.max_caps.dict:address', db, int)

        # ACCUMULATOR
        self._acc_distr__accounts = ArrayDB('acc.distr.accounts', db, Address)
        self._acc_distr__accounts_dict = DictDB('acc.distr.accounts.dict:address', db, bool)
        self._acc_distr__amounts_accepted_dict = DictDB('acc.distr.amounts_accepted.dict:address', db, int)
        self._acc_distr__amounts_distributed_dict = DictDB('acc.distr.amounts_distributed.dict:address', db, int)
        self._acc_distr__amounts_bonused_dict = DictDB('acc.distr.amounts_bonused.dict:address', db, int)
        self._acc_airdrop__accounts = ArrayDB('acc.airdrop.accounts', db, Address)
        self._acc_airdrop__accounts_dict = DictDB('acc.airdrop.accounts.dict:address', db, bool)
        self._acc_airdrop__amounts_airdropped_dict = DictDB('acc.airdrop.amounts_airdropped.dict:address', db, int)

        # LOG(DISTRIBUTION)
        self._distr__accounts = ArrayDB('distr.accounts', db, Address)
        self._distr__hashes = ArrayDB('distr.hashes', db, bytes)
        self._distr__amounts_requested = ArrayDB('distr.amounts_requested', db, int)
        self._distr__amounts_accepted = ArrayDB('distr.amounts_accepted', db, int)
        self._distr__amounts_distributed = ArrayDB('distr.amounts_distributed', db, int)
        self._distr__statuses = ArrayDB('distr.statuses', db, int)
        self._distr__timestamps = ArrayDB('distr.timestamps', db, int)

        # LOG(BONUS)
        self._bonus__accounts = ArrayDB('bonus.accounts', db, Address)
        self._bonus__hashes = ArrayDB('bonus.hashes', db, bytes)
        self._bonus__amounts_held = ArrayDB('bonus.amounts_held', db, int)
        self._bonus__amounts_bonused = ArrayDB('bonus.amounts_bonused', db, int)
        self._bonus__statuses = ArrayDB('bonus.statuses', db, int)
        self._bonus__rates = ArrayDB('bonus.rate', db, int)
        self._bonus__timestamps = ArrayDB('bonus.timestamp', db, int)

        # LOG(AIRDROP)
        self._airdrop__accounts = ArrayDB('airdrop.accounts', db, Address)
        self._airdrop__hashes = ArrayDB('airdrop.hashes', db, Address)
        self._airdrop__amounts_airdropped = ArrayDB('airdrop.amounts_airdropped', db, int)
        self._airdrop__statuses = ArrayDB('airdrop.statuses', db, int)
        self._airdrop__timestamps = ArrayDB('airdrop.timestamp', db, int)

    def on_install(self,
                   name: str,
                   score_cap: int,
                   exchange_rate: int,
                   start: int,
                   end: int,
                   account_min_cap: int,
                   account_max_cap: int,
                   score_token: Address,
                   ):
        """

        :param name: contract name
        :param score_cap: score cap (in loops, 1 icx = 1000000000000000000 loop)
        :param exchange_rate: exchange rate (in millions)
        :param start: timestamp (in microseconds)
        :param end: timestamp (in microseconds)
        :param account_min_cap: minimum investable icx amount per account (in loops, 1 icx = 1000000000000000000 loop)
        :param account_max_cap: maximum investable icx amount per account (in loops, 1 icx = 1000000000000000000 loop)
        :param score_token: address of token score
        :return: none
        """
        super().on_install()
        self._precondition(end >= start >= 0)
        self._precondition(score_cap >= account_max_cap >= account_min_cap >= 0)
        self._precondition(exchange_rate > 0)
        self._precondition(score_token.is_contract)
        self._context__name.set(name)
        self._context__score_cap.set(score_cap)
        self._context__exchange_rate.set(exchange_rate)
        self._context__start.set(start)
        self._context__end.set(end)
        self._context__account_min_cap.set(account_min_cap)
        self._context__account_max_cap.set(account_max_cap)
        self._score__token_address.set(score_token)


    def on_update(self):
        """

        :return: none
        """
        super().on_update()

    # ==================================================================================================================
    # FALLBACK
    # ==================================================================================================================

    @external
    def make_addr_list(self, _addr_offset:int, _addr_count:int):
        for i in range(_addr_offset, _addr_offset+_addr_count):
            sender = Address.from_string("hx" + "%040d" % i)
            amount = 1 * 10 ** 18
            self._fallback(sender, amount)

    @payable
    def fallback(self):
        """
        :return: none
        """
        # PRECONDITION
        sender = self.msg.sender
        amount = self.msg.value
        self._fallback(sender, amount)

    def _fallback(self, sender, amount):
        self._precondition(not self.get_deactivation() and self._on_campaign(), 'test1')
        self._precondition(not sender.is_contract and amount > 0, 'test2')
        account_cap = self._get_account_cap(sender, amount)
        self._precondition(account_cap > 0, 'test3')

        # SCORE
        score = self._get_score_token()

        # AMOUNT ACCEPTED(ICX) & DISTRIBUTED(TOKEN)
        amount_acceptance = self._min(account_cap, amount)
        amount_distribution = self._get_rated_amount(amount_acceptance, self.get_exchange_rate())

        # EXCHANGE LOOPS FOR DECIMALS
        exponent = score.decimals() - LOOP_DECIMALS
        if exponent != 0:
            amount_distribution = amount_distribution * 10 ** exponent

        # DISTRIBUTE
        self._precondition(score.distribute(sender, amount_distribution, b'investment'),'test4')
        self._increase_amount_raised(amount_acceptance)
        self._increase_amount_distributed(amount_distribution)
        if amount_acceptance < amount:
            self.icx.transfer(sender, amount - amount_acceptance)

        # ACCUMULATE
        if not self._acc_distr__accounts_dict[sender]:
            self._acc_distr__accounts.put(sender)
            self._acc_distr__accounts_dict[sender] = True
        self._increase_acc_amount_accepted(sender, amount_acceptance)
        self._increase_acc_amount_distributed(sender, amount_distribution)

        # LOG(DISTRIBUTION)
        index = self._append_distribution(sender, self.tx.hash, amount, amount_acceptance, amount_distribution)

        # EVENT
        self.EventDistributed(sender, amount, amount_acceptance, amount_distribution, index)

    @external
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        self._precondition(
            self.msg.sender == self._score__token_address.get() and _from == self.owner,
            f'PRECONDITION FAILED !! UNEXPECTED TOKEN OWNER !!'
        )

    # ==================================================================================================================
    #
    # ==================================================================================================================

    @staticmethod
    def _min(a: int, b: int) -> int:
        """

        :param a: candidate a
        :param b: candidate b
        :return: a if 'a <= b', otherwise b
        """
        return a if a <= b else b

    @staticmethod
    def _get_rated_amount(amount: int, rate: int) -> int:
        """

        :param amount: amount (don't care unit)
        :param rate: rate in millions
        :return:
        """
        if amount <= 0:
            return 0
        else:
            return int(amount * rate / MILLION)

    # ==================================================================================================================
    #
    # ==================================================================================================================

    def _precondition(self, condition: bool, message: str=None):
        """

        :param condition:
        :param message:
        :return:
        """
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)

    def _on_campaign(self) -> bool:
        """

        :return: true if 'remaining_cap > 0 and start <= now <= end', otherwise false
        """
        if self.get_remaining_cap() > 0:
            s = self._context__start.get()
            e = self._context__end.get()
            if s <= self.now() <= e:
                return True
        return False

    def _get_score_token(self) -> IToken:
        """

        :return: score interface
        """
        return self.create_interface_score(self._score__token_address.get(), IToken)

    def _get_register_caps(self, account: Address) -> (int, int):
        """

        :param account: account address
        :return: tuple(min cap, max cap)
        """
        return \
            self._register__min_caps_dict[account], \
            self._register__max_caps_dict[account]

    def _get_contribution_caps(self) -> (int, int):
        """
        • Investable min/max cap per account
        :return: tuple(min cap, max cap)
        """
        return \
            self._context__account_min_cap.get(), \
            self._context__account_max_cap.get()

    def _append_distribution(self, account: Address, hash_: bytes, amount: int, accepted: int, distributed: int) -> int:
        """

        :param account: account address
        :param hash_: icon transaction hash
        :param amount: requested icx amount in loops
        :param accepted: accepted icx amount in loops
        :param distributed: distributed token amount in decimals
        :return: transaction index
        """
        index = len(self._distr__accounts)

        self._distr__accounts.put(account)
        self._distr__hashes.put(hash_)
        self._distr__timestamps.put(self.now())
        self._distr__amounts_requested.put(amount)
        self._distr__amounts_accepted.put(accepted)
        self._distr__amounts_distributed.put(distributed)
        self._distr__statuses.put(Status.LOCKED)

        return index

    def _append_bonus(self, account: Address, hash_: bytes, bonus_rate: int, amount: int, bonused: int) -> int:
        """

        :param account: account address
        :param hash_: hash
        :param bonus_rate: bonus rate in millions
        :param amount: token amount in decimals
        :param bonused: bonus token amount in decimals
        :return: bonux index
        """
        index = len(self._bonus__accounts)

        self._bonus__accounts.put(account)
        self._bonus__hashes.put(hash_)
        self._bonus__rates.put(bonus_rate)
        self._bonus__amounts_held.put(amount)
        self._bonus__amounts_bonused.put(bonused)
        self._bonus__statuses.put(Status.LOCKED)

        return index

    def _append_airdrop(self, account: Address, hash_: bytes, airdropped: int) -> int:
        """

        :param account: account address
        :param hash_: hash
        :param airdropped: airdropped token amount in decimals
        :return: airdrop index
        """
        index = len(self._airdrop__accounts)

        self._airdrop__accounts.put(account)
        self._airdrop__hashes.put(hash_)
        self._airdrop__amounts_airdropped.put(airdropped)
        self._airdrop__statuses.put(Status.LOCKED)

        return index

    def _get_account_cap(self, account: Address, amount_requested: int) -> int:
        """

        :param account: account address
        :param amount_requested: requested icx amount in loops
        :return: investable icx amount in loops
        """
        score_remaining_cap = self.get_remaining_cap()
        if score_remaining_cap == 0:
            return 0
        if not self._register__deactivation.get():
            min_cap, max_cap = self._get_register_caps(account)
            if min_cap == 0 == max_cap:
                return 0
        else:
            min_cap, max_cap = self._get_contribution_caps()
            if min_cap == 0 == max_cap:
                return score_remaining_cap
        acc_amount_accepted = self._acc_distr__amounts_accepted_dict[account]
        account_remaining_cap = max_cap - acc_amount_accepted
        condition = account_remaining_cap <= 0 or acc_amount_accepted + amount_requested < min_cap

        return 0 if condition else self._min(score_remaining_cap, account_remaining_cap)

    def _refund(self, index: int) -> bool:
        """

        :param index: distribution(investment info) index
        :return: true if succeeded, otherwise false
        """
        if not (0 <= index < self.get_itemized_distribution_size()):
            return False

        account = self._distr__accounts.get(index)
        amount_accepted = self._distr__amounts_accepted.get(index)
        amount_distributed = self._distr__amounts_distributed.get(index)
        status = self._distr__statuses.get(index)

        if amount_accepted == 0:  # CHECK BONUS
            return False

        if status != Status.LOCKED:
            return True if status == Status.REFUNDED else False

        score = self._get_score_token()
        if not score.dispossess(account, amount_distributed):
            return False
        # noinspection PyBroadException
        try:
            icx_sent = self.icx.transfer(account, amount_accepted)
        except Exception:
            icx_sent = False
        if not icx_sent:  # if not self.icx.send(account, amount_accepted):
            self._precondition(score.distribute(account, amount_distributed, b'distribution for refund'))
            return False
        self._decrease_amount_raised(amount_accepted)
        self._decrease_amount_distributed(amount_distributed)
        self._decrease_acc_amount_accepted(account, amount_accepted)
        self._decrease_acc_amount_distributed(account, amount_distributed)
        self._distr__statuses[index] = Status.REFUNDED
        self.EventDistributionStatusChanged(index, Status.REFUNDED)

        return True

    def _unlock_distributed(self, index: int) -> bool:
        """
        • A.K.A. UNLOCK
        :param index: distribution index
        :return: true if succeeded, otherwise false
        """
        if not 0 <= index < self.get_itemized_distribution_size():
            return False

        status = self._distr__statuses[index]
        if status != Status.LOCKED:
            return True if status == Status.UNLOCKED else False

        account = self._distr__accounts[index]
        amount_distributed = self._distr__amounts_distributed[index]
        if not self._get_score_token().unlock(account, amount_distributed):
            return False
        self._distr__statuses[index] = Status.UNLOCKED
        self.EventDistributionStatusChanged(index, Status.UNLOCKED)
        return True

    def _unlock_bonused(self, index: int) -> bool:
        """

        :param index: bonus index
        :return: true if succeeded, otherwise false
        """
        if not 0 <= index < self.get_itemized_bonus_size():
            return False

        status = self._bonus__statuses[index]
        if status != Status.LOCKED:
            return True if status == Status.UNLOCKED else False
        account = self._bonus__accounts[index]
        amount_bonused = self._bonus__amounts_bonused[index]
        if not self._get_score_token().unlock(account, amount_bonused):
            return False
        self._bonus__statuses[index] = Status.UNLOCKED
        self.EventBonusStatusChanged(index, Status.UNLOCKED)
        return True

    def _unlock_airdropped(self, index: int) -> bool:
        """

        :param index: airdrop index
        :return: true if succeeded, otherwise false
        """
        if not 0 <= index < self.get_itemized_airdrop_size():
            return False

        status = self._airdrop__statuses[index]
        if status != Status.LOCKED:
            return True if status == Status.UNLOCKED else False
        account = self._airdrop__accounts[index]
        amount_bonused = self._airdrop__amounts_airdropped[index]
        if not self._get_score_token().unlock(account, amount_bonused, True):
            return False
        self._airdrop__statuses[index] = Status.UNLOCKED
        self.EventAirdropStatusChanged(index, Status.UNLOCKED)
        return True

    def _increase_amount_raised(self, amount: int):
        """

        :param amount: icx amount in loops
        :return: none
        """
        self._context__amount_raised.set(self._context__amount_raised.get() + amount)

    def _decrease_amount_raised(self, amount: int):
        """

        :param amount: icx amount in loops
        :return: none
        """
        self._context__amount_raised.set(self._context__amount_raised.get() - amount)

    def _increase_amount_distributed(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_distributed.set(self._context__amount_distributed.get() + amount)

    def _decrease_amount_distributed(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_distributed.set(self._context__amount_distributed.get() - amount)

    def _increase_amount_bonused(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_bonused.set(self._context__amount_bonused.get() + amount)

    def _decrease_amount_bonused(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_bonused.set(self._context__amount_bonused.get() - amount)

    def _increase_amount_airdropped(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_airdropped.set(self._context__amount_airdropped.get() + amount)

    def _decrease_amount_airdropped(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._context__amount_airdropped.set(self._context__amount_airdropped.get() - amount)

    def _increase_amount_withdrew(self, amount: int):
        """

        :param amount: icx amount in loops
        :return: none
        """
        self._context__amount_withdrew.set(self._context__amount_withdrew.get() + amount)

    def _decrease_amount_withdrew(self, amount: int):
        """

        :param amount: icx amount in loops
        :return: none
        """
        self._context__amount_withdrew.set(self._context__amount_withdrew.get() - amount)

    def _increase_acc_amount_accepted(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: icx amount in loops
        :return: none
        """
        self._acc_distr__amounts_accepted_dict[account] = self._acc_distr__amounts_accepted_dict[account] + amount

    def _decrease_acc_amount_accepted(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: icx amount in loops
        :return: none
        """
        self._acc_distr__amounts_accepted_dict[account] = self._acc_distr__amounts_accepted_dict[account] - amount

    def _increase_acc_amount_distributed(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return:
        """
        self._acc_distr__amounts_distributed_dict[account] = self._acc_distr__amounts_distributed_dict[account] + amount

    def _decrease_acc_amount_distributed(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return: none
        """
        self._acc_distr__amounts_distributed_dict[account] = self._acc_distr__amounts_distributed_dict[account] - amount

    def _increase_acc_amount_bonused(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return: none
        """
        self._acc_distr__amounts_bonused_dict[account] = self._acc_distr__amounts_bonused_dict[account] + amount

    def _decrease_acc_amount_bonused(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return: none
        """
        self._acc_distr__amounts_bonused_dict[account] = self._acc_distr__amounts_bonused_dict[account] - amount

    def _increase_acc_amount_airdropped(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return: none
        """
        current_amount = self._acc_airdrop__amounts_airdropped_dict[account]
        self._acc_airdrop__amounts_airdropped_dict[account] = current_amount + amount

    def _decrease_acc_amount_airdropped(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: token amount in decimals
        :return: none
        """
        current_amount = self._acc_airdrop__amounts_airdropped_dict[account]
        self._acc_airdrop__amounts_airdropped_dict[account] = current_amount - amount

    # ==================================================================================================================
    # IBrokerApis
    # ==================================================================================================================

    @external(readonly=True)
    def get_max_iteration(self) -> int:
        """

        :return: max iteration
        """
        return MAX_ITERATION

    @external(readonly=True)
    def information(self) -> dict:
        """

        :return:
            • score_version
            • name
            • score_cap (in loops, 1 icx = 1000000000000000000 loop)
            • exchange_rate (in millions)
            • start (timestamp in microseconds)
            • end (timestamp in microseconds)
            • account_min_cap (in loops, 1 icx = 1000000000000000000 loop)
            • account_max_cap (in loops, 1 icx = 1000000000000000000 loop)
            • deactivated
            • amount_raised
            • count_of_investors
            • register_deactivated
        """
        return {
            'score_version': self.__SCORE_VERSION,
            'name': self._context__name.get(),
            'score_cap': self._context__score_cap.get(),
            'exchange_rate': self._context__exchange_rate.get(),
            'start': self._context__start.get(),
            'end': self._context__end.get(),
            'account_min_cap': self._context__account_min_cap.get(),
            'account_max_cap': self._context__account_max_cap.get(),
            'deactivated': self._context__deactivation.get(),
            'amount_raised': self._context__amount_raised.get(),
            'count_of_investors': self.get_investor_count(),
            'register_deactivated': self._register__deactivation.get()
        }

    @external(readonly=True)
    def get_exchange_rate(self) -> int:
        """

        :return: exchange rate (in millions)
        """
        return self._context__exchange_rate.get()

    @external
    def set_name(self, name: str):
        """

        :param name: broker name
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._context__name.set(name)

    @external(readonly=True)
    def get_deactivation(self) -> bool:
        """

        :return: true if deactivated, otherwise false
        """
        return self._context__deactivation.get()

    @external
    def deactivate(self, deactivation: bool):
        """

        :param deactivation: deactivating if true, otherwise activating
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._context__deactivation.set(deactivation)
        self.EventBrokerDeactivated(deactivation)

    @external(readonly=True)
    def get_remaining_cap(self) -> int:
        """

        :return: remaining cap(score_cap - amount_raised) in loops
        """
        score_cap = self._context__score_cap.get()
        amount_raised = self._context__amount_raised.get()

        return 0 if score_cap == amount_raised else score_cap - amount_raised

    @external(readonly=True)
    def get_amount_raised(self) -> int:
        """

        :return: amount raised in loops
        """
        return self._context__amount_raised.get()

    @external(readonly=True)
    def get_itemized_distribution_size(self) -> int:
        """

        :return: itemized distribution
        """
        return len(self._distr__accounts)

    @external(readonly=True)
    def get_itemized_distribution(self, indexes: str) -> dict:
        """

        :param indexes: distribution indexes (comma separated)
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • account
                • amount_requested (icx amount in loops)
                • amount_accepted (icx amount in loops)
                • amount_distributed (token amount in decimals)
                • status (0:LOCKED, 1:REFUNDED, 2:UNLOCKED)
        """
        success = False
        itemized_data = []
        if indexes is not None:
            idxes = indexes.split(',')
            idxes_size = len(idxes)
            itemized_size = self.get_itemized_distribution_size()
            if idxes_size <= self.get_max_iteration():
                for i in range(idxes_size):
                    idx = int(idxes[i].strip())
                    if idx < itemized_size:
                        itemized_data.append({
                            'index': idx,
                            'txhash': self._distr__hashes.get(idx),
                            'timestamp': self._distr__timestamps.get(idx),
                            'account': self._distr__accounts.get(idx),
                            'amount_requested': self._distr__amounts_requested.get(idx),
                            'amount_accepted': self._distr__amounts_accepted.get(idx),
                            'amount_distributed': self._distr__amounts_distributed.get(idx),
                            'status': self._distr__statuses.get(idx)
                        })
                success = True
        return {
            'success': success,
            'data': itemized_data
        }

    @external(readonly=True)
    def get_itemized_bonus_size(self) -> int:
        """

        :return: itemized bonus size
        """
        return len(self._bonus__accounts)

    @external(readonly=True)
    def get_itemized_bonus(self, indexes: str) -> dict:
        """

        :param indexes: bonus index
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • account
                • bonus_rate (in millions)
                • amount (token amount in decimals)
                • amount_bonused (token amount in decimals)
                • status (0:LOCKED, 2:UNLOCKED, 3:DISPOSSESSED)
        """
        success = False
        itemized_data = []
        if indexes is not None:
            idxes = indexes.split(',')
            idxes_size = len(idxes)
            itemized_size = self.get_itemized_bonus_size()
            if idxes_size <= self.get_max_iteration():
                for i in range(idxes_size):
                    idx = int(idxes[i].strip())
                    if idx < itemized_size:
                        itemized_data.append({
                            'index': idx,
                            'txhash': self._bonus__hashes.get(idx),
                            'timestamp': self._bonus__timestamps.get(idx),
                            'account': self._bonus__accounts.get(idx),
                            'bonus_rate': self._bonus__rates.get(idx),
                            'amount': self._bonus__amounts_held.get(idx),
                            'amount_bonused': self._bonus__amounts_bonused.get(idx),
                            'status': self._bonus__statuses.get(idx)
                        })
                success = True
        return {
            'success': success,
            'data': itemized_data
        }

    @external(readonly=True)
    def get_itemized_airdrop_size(self) -> int:
        """

        :return: itemized airdrop size
        """
        return len(self._airdrop__accounts)

    @external(readonly=True)
    def get_itemized_airdrop(self, indexes: str) -> dict:
        """

        :param indexes: airdrop index (comma separated)
        :return: dict
            • success (boolean)
            • data (optional: dict)
                • index
                • txhash
                • timestamp (in microseconds)
                • account
                • amount_airdropped (token amount in decimals)
                • status (0:LOCKED, 2:UNLOCKED, 3:DISPOSSESSED)
        """
        success = False
        itemized_data = []
        if indexes is not None:
            idxes = indexes.split(',')
            idxes_size = len(idxes)
            itemized_size = self.get_itemized_airdrop_size()
            if idxes_size <= self.get_max_iteration():
                for i in range(idxes_size):
                    idx = int(idxes[i].strip())
                    if idx < itemized_size:
                        itemized_data.append({
                            'index': idx,
                            'txhash': self._airdrop__hashes.get(idx),
                            'timestamp': self._airdrop__timestamps.get(idx),
                            'account': self._airdrop__accounts.get(idx),
                            'amount_airdropped': self._airdrop__amounts_airdropped.get(idx),
                            'status': self._airdrop__statuses.get(idx)
                        })
                success = True
        return {
            'success': success,
            'data': itemized_data
        }

    @external
    def refund(self, indexes: str):
        """

        :param indexes: distribution indexes (comma separated)
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(indexes is not None)

        idxes = indexes.split(',')
        self._precondition(len(idxes) <= self.get_max_iteration())

        idxes_failed = []
        for i in range(len(idxes)):
            idx = int(idxes[i].strip())
            if not self._refund(idx):
                idxes_failed.append(idx)
        if len(idxes_failed) > 0:
            self.EventRefunded(','.join([str(idx) for idx in idxes_failed]))

    @external
    def unlock_distributed(self, indexes: str):
        """
        • A.K.A. UNLOCK
        :param indexes: distribution indexes (comma separated)
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(indexes is not None)

        idxes = indexes.split(',')
        idxes_size = len(idxes)
        self._precondition(idxes_size <= self.get_max_iteration())

        Logger.info(f"unlock_distributed start ssssss({idxes_size}): {idxes[0]} ~ {idxes[-1]}")
        idxes_failed = []
        for i in range(idxes_size):
            idx = int(idxes[i].strip())
            if not self._unlock_distributed(idx):
                idxes_failed.append(idx)
        if len(idxes_failed) > 0:
            self.EventUnlocked(Scope.DISTRIBUTION, ','.join([str(idx) for idx in idxes_failed]))
        Logger.info(f"unlock_distributed end ssssss({idxes_size}):   {idxes[0]} ~ {idxes[-1]}")

    @external
    def unlock_bonused(self, indexes: str):
        """

        :param indexes: bonus indexes (comma separated)
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(indexes is not None)

        idxes = indexes.split(',')
        idxes_size = len(idxes)
        self._precondition(idxes_size <= self.get_max_iteration())

        idxes_failed = []
        for i in range(idxes_size):
            idx = int(idxes[i].strip())
            if not self._unlock_bonused(idx):
                idxes_failed.append(idx)
        if len(idxes_failed) > 0:
            self.EventUnlocked(Scope.BONUS, ','.join([str(idx) for idx in idxes_failed]))

    @external
    def unlock_airdropped(self, indexes: str):
        """

        :param indexes: airdrop indexes (comma separated)
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(indexes is not None)

        idxes = indexes.split(',')
        idxes_size = len(idxes)
        self._precondition(idxes_size <= self.get_max_iteration())

        idxes_failed = []
        for i in range(idxes_size):
            idx = int(idxes[i].strip())
            if not self._unlock_airdropped(idx):
                idxes_failed.append(idx)
        if len(idxes_failed) > 0:
            self.EventUnlocked(Scope.AIRDROP, ','.join([str(idx) for idx in idxes_failed]))

    @external
    def bonus(self, bonus_rate: int, count: int):
        """

        :param bonus_rate: bonus rate in millions
        :param count: count from bonus_offset
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(count <= self.get_max_iteration())
        self._precondition(not self._on_campaign())
        score = self._get_score_token()
        offset = self._context__bonus_offset.get()
        for i in range(count):
            if offset >= len(self._acc_distr__accounts):
                break
            account = self._acc_distr__accounts[offset]
            amount_held = self._acc_distr__amounts_distributed_dict[account]
            if amount_held > 0:
                amount_bonused = self._get_rated_amount(amount_held, bonus_rate)
                if not score.distribute(account, amount_bonused, b'distribute.bonused'):
                    break
                index = self._append_bonus(account, self.tx.hash, bonus_rate, amount_held, amount_bonused)
                self._increase_amount_bonused(amount_bonused)
                self._increase_acc_amount_bonused(account, amount_bonused)
                self.EventBonused(account, amount_held, bonus_rate, amount_bonused, index)
                offset += 1
        self._context__bonus_offset.set(offset)

    @external(readonly=True)
    def get_current_bonus_offset(self) -> int:
        """

        :return: current bonus offset
        """
        return self._context__bonus_offset.get()

    @external
    def reset_bonus_offset(self, offset: int=0):
        """

        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(0 <= offset <= len(self._acc_distr__accounts))
        self._context__bonus_offset.set(offset)

        self.EventResetBonusOffset(offset)

    @external(readonly=True)
    def get_bonus_pending_count(self) -> int:
        """

        :return: bonus pending(remained) count
        """

        remains = len(self._acc_distr__accounts) - self._context__bonus_offset.get()
        return 0 if remains <= 0 else remains

    @external
    def airdrop(self, accounts: str, amount: int):
        """

        :param accounts: account addresses (comma separated)
        :param amount: token amount in decimals
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(accounts is not None and amount > 0)
        split_accounts = accounts.split(',')
        accounts_size = len(split_accounts)
        self._precondition(accounts_size <= self.get_max_iteration())
        score = self._get_score_token()
        for i in range(accounts_size):
            account = Address.from_string(split_accounts[i].strip())
            self._precondition(score.distribute(account, amount, b'airdropped'))
            if not self._acc_airdrop__accounts_dict[account]:
                self._acc_airdrop__accounts.put(account)
            self._increase_acc_amount_airdropped(account, amount)
            self._increase_amount_airdropped(amount)
            index = self._append_airdrop(account, self.tx.hash, amount)
            self.EventAirdropped(account, amount, index)

    @external
    def dispossess_broker_tokens(self, amount: int):
        """

        :param amount: token amount in decimals
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        score = self._get_score_token()
        self._precondition(0 < amount <= score.get_free_balance(self.address))
        score.transfer(self.owner, amount, b'dispossess broker tokens')
        self.EventTokenDispossessed(self.owner, amount)

    @external
    def dispossess_bonused_tokens(self, index: int):
        """

        :param index: bonus index
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(0 <= index < self.get_itemized_bonus_size())
        self._precondition(self._bonus__statuses.get(index) == Status.LOCKED)
        account = self._bonus__accounts.get(index)
        amount = self._bonus__amounts_bonused.get(index)
        self._decrease_amount_bonused(amount)
        self._decrease_acc_amount_bonused(account, amount)
        self._bonus__statuses[index] = Status.DISPOSSESSED
        self._get_score_token().dispossess(account, amount)
        self.EventBonusStatusChanged(index, Status.DISPOSSESSED)

    @external
    def dispossess_airdropped_tokens(self, index: int):
        """

        :param index: airdrop index
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(0 <= index < self.get_itemized_airdrop_size())
        self._precondition(self._airdrop__statuses.get(index) == Status.LOCKED)
        account = self._airdrop__accounts.get(index)
        amount = self._airdrop__amounts_airdropped.get(index)
        self._decrease_amount_airdropped(amount)
        self._decrease_acc_amount_airdropped(account, amount)
        self._airdrop__statuses[index] = Status.DISPOSSESSED
        self._get_score_token().dispossess(account, amount)
        self.EventAirdropStatusChanged(index, Status.DISPOSSESSED)

    @external
    def withdraw(self, account: Address, amount: int):
        """

        :param account: account address
        :param amount: icx amount in loops
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
    #   self._precondition(self.now() > self._context__end.get())  # NOTE: CONFIRMED BY PLANNER
        self._precondition(0 < amount <= self.icx.get_balance(self.address))
        self.icx.transfer(account, amount)
        self._increase_amount_withdrew(amount)
        self.EventWithdrew(account, amount)

    @external(readonly=True)
    def get_amount_withdrew(self) -> int:
        """

        :return: amount withdrew in loops
        """
        return self._context__amount_withdrew.get()

    @external(readonly=True)
    def get_investor_count(self) -> int:
        """

        :return: count of investors
        """
        return len(self._acc_distr__accounts)

    @external(readonly=True)
    def get_investor(self, account: Address) -> dict:
        """

        :param account: account address
        :return: dict
            • amount_accepted (icx in loops)
            • amount_distributed (token in decimals)
            • amount_bonused (token in decimals)
        """
        if self._acc_distr__accounts_dict[account]:
            return {
                'amount_accepted': self._acc_distr__amounts_accepted_dict[account],
                'amount_distributed': self._acc_distr__amounts_distributed_dict[account],
                'amount_bonused': self._acc_distr__amounts_bonused_dict[account]
            }
        return dict()

    @external(readonly=True)
    def get_investors(self, offset: int, count: int) -> dict:
        """

        :param offset: zero based start index
        :param count: count
        :return: dict
            • success (boolean)
            • data (optional: array)
        """

        success = False
        accounts = []
        count_of_investors = len(self._acc_distr__accounts)
        if 0 < count <= self.get_max_iteration():
            if 0 <= offset < count_of_investors:
                if offset + count > count_of_investors:
                    count = count_of_investors - offset
                for i in range(count):
                    accounts.append(self._acc_distr__accounts[offset + i])
                success = True
        return {
            'success': success,
            'data': accounts
        }


    @external(readonly=True)
    def get_register_deactivation(self) -> bool:
        """
        • REGISTER: A.K.A. WHITELIST
        :return: true if register deactivated, otherwise false
        """
        return self._register__deactivation.get()

    @external
    def deactivate_register(self, deactivation: bool):
        """

        :param deactivation: deactivating if true, otherwise activating
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._register__deactivation.set(deactivation)

        self.EventRegisterDeactivated(deactivation)

    @external(readonly=True)
    def get_register_size(self) -> int:
        """

        :return: count of registered account
        """
        return len(self._register__accounts)

    @external(readonly=True)
    def find_in_register(self, account: Address) -> dict:
        """

        :param account: account address
        :return: dict
            • account (optional: account address)
            • min_cap (optional: minimum investable icx amounts in loops)
            • max_cap (optional: maximum investable icx amounts in loops)
        """
        if self._register__accounts_dict[account]:
            return {
                'account': account,
                'min_cap': self._register__min_caps_dict[account],
                'max_cap': self._register__max_caps_dict[account]
            }
        return dict()

    @external(readonly=True)
    def get_accounts_in_register(self, offset: int, count: int) -> dict:
        """

        :param offset: zero based start offset
        :param count: count
        :return: dict
            • success (boolean)
            • data (optional: array)
                • dict
                    • account
                    • min_cap
                    • max_cap
        """
        success = False
        accounts = []
        count_of_accounts = len(self._register__accounts)
        if 0 < count <= self.get_max_iteration():
            if 0 <= offset < count_of_accounts:
                if offset + count > count_of_accounts:
                    count = count_of_accounts - offset
                for i in range(count):
                    idx = offset + i
                    account = self._register__accounts[idx]
                    accounts.append({
                        'account': account,
                        'min_cap': self._register__min_caps_dict[account],
                        'max_cap': self._register__max_caps_dict[account]
                    })
                success = True
        return {
            'success': success,
            'accounts': accounts
        }

    @external
    def put_accounts_to_register(self, conditions: str):
        """
        •
        :param conditions: comma and pipe separated conditions(account|min|max,...), e.g. hx0…01|0|1,hx0…02|0|1, ...
        :return: none
        """
        self._precondition(self.msg.sender == self.owner)
        self._precondition(self.get_remaining_cap() > 0 and self.now() <= self._context__end.get())
        self._precondition(conditions is not None)
        split_conditions = conditions.split(',')  # e.g. 'hx0…01|0|1,hx0…02|0|1,………'
        split_conditions_size = len(split_conditions)
        self._precondition(split_conditions_size <= self.get_max_iteration())

        for i in range(split_conditions_size):
            condition = split_conditions[i].split('|')  # e.g. 'hx0…01|0|1'
            condition_size = len(condition)
            self._precondition(condition_size == 3)
            account = Address.from_string(condition[0].strip())
            min_cap = int(condition[1].strip())
            max_cap = int(condition[2].strip())
            self._precondition(0 <= min_cap <= max_cap)
            if not self._register__accounts_dict[account]:
                self._register__accounts.put(account)
                self._register__accounts_dict[account] = True
            self._register__min_caps_dict[account] = min_cap
            self._register__max_caps_dict[account] = max_cap
            self.EventAccountRegistered(account, min_cap, max_cap)

    # ==================================================================================================================
    # EVENT
    # ==================================================================================================================

    @eventlog(indexed=1)
    def EventBrokerDeactivated(self, deactivation: bool):
        pass

    @eventlog(indexed=1)
    def EventRegisterDeactivated(self, deactivation: bool):
        pass

    @eventlog(indexed=1)
    def EventAccountRegistered(self, account: Address, mincap: int, maxcap: int):
        pass

    @eventlog(indexed=1)
    def EventDistributed(self, account: Address, amount: int, accepted: int, distributed: int, index: int):
        pass

    @eventlog(indexed=1)
    def EventBonused(self, account: Address, amount: int, bonus_rate: int, bonused: int, index: int):
        pass

    @eventlog(indexed=1)
    def EventAirdropped(self, account: Address, amount: int, index: int):
        pass

    @eventlog(indexed=2)
    def EventDistributionStatusChanged(self, index: int, status: int):
        pass

    @eventlog(indexed=2)
    def EventBonusStatusChanged(self, index: int, status: int):
        pass

    @eventlog(indexed=2)
    def EventAirdropStatusChanged(self, index: int, status: int):
        pass

    @eventlog(indexed=1)
    def EventRefunded(self, failed_indexes: str):
        pass

    @eventlog(indexed=1)
    def EventUnlocked(self, scope: int, failed_indexes: str):
        """

        :param scope: 0:DISTRIBUTION, 1:BONUS, 2:AIRDROP
        :param failed_indexes: failed indexes (comma separated)
        :return: none
        """
        pass

    @eventlog
    def EventResetBonusOffset(self, offset: int):
        pass

    @eventlog(indexed=1)
    def EventWithdrew(self, account: Address, amount: int):
        pass

    @eventlog(indexed=1)
    def EventTokenDispossessed(self, address: Address, amount: int):
        pass

    # ==================================================================================================================
    # EOF
    # ==================================================================================================================
