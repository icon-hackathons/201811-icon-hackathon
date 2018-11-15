from iconservice import *
from enum import IntEnum

# ==================================================================================================================
#	interface
# ==================================================================================================================

class IDpesProjectScore():
    @abstractmethod
    def get_user_info(self, user_address: Address) -> dict:
        """
		:param user_address: user address
        :return: dict
            • balance
            • grade
        """
        pass

class IDpes(InterfaceScore):
    @interface
    def _close_vote(self, project_address: Address) -> None:
        pass
	@interface
    def _close_project(self, project_address: Address) -> None:
        pass
	
class Error():
    def __init__(self, message):
        self.message = message
    def throw(self) -> dict:
        return {
			'error': message
		}

# ==================================================================================================================
#	constants, enum
# ==================================================================================================================

TAG = 'DpesProjectScore'
ICX = 10 ** 18

_USER_GRADE_DICT = "_USER_GRADE_DICT"
_REVIEW_DICT = "_REVIEW_DICT"
_REVIEWER_WHITELIST_PARENT_DICT = '_REVIEWER_WHITELIST_PARENT_DICT'
_REVIEWER_WHITELIST_CHILD_DICT = '_REVIEWER_WHITELIST_CHILD_DICT'

class UserGrade(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
	E = 5

class ParentLevel(IntEnum):
    TEAM = 1
    ORACLE = 2

class ChildLevel(IntEnum):
    MEMBER = 1
	LEADER = 2
    ORACLE = 3

# ==================================================================================================================
#	main source
# ==================================================================================================================

class DpesProjectScore(IconScoreBase, IDpesProjectScore):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._user_grade_dict = DictDB(self._USER_GRADE_DICT, db, value_type=str)
        self._review_dict = DictDB(self._REVIEW_DICT, db, value_type=str)
        self._reviewer_whitelist_parent_dict = DictDB(self._REVIEWER_WHITELIST_PARENT_DICT, db, value_type=str, depth=2)
		self._reviewer_whitelist_child_dict = DictDB(self._REVIEWER_WHITELIST_CHILD_DICT, db, value_type=str, depth=2)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_user_info(self, _user_address: Address) -> dict:
		_balance = self.icx.get_balance(_user_address)
		_grade = _user_grade_dict[_user_address]
		return {
			'balance': _balance,
			'grade': _grade
		}

	@external(readonly=true)
    def check_parent_exist(self, _parent_address: Address) -> bool:
		return self._reviewer_whitelist_parent_dict[_parent_address] != None 

	@external(readonly=true)
    def get_parent_level(self, _parent_address: Address) -> int:
		_parent_db = self._reviewer_whitelist_parent_dict[_parent_address]
		return 0 if _parent_db is None else _parent_db.parent_level

	@external
    def create_parent_dict(self, _formatted_json: str):
		self._precondition(self.msg.sender == self.owner, 'not owner')
		_decoded_data = json_loads(_formatted_json)
		_decoded_data_size = len(_decoded_data)
		for i in range(_decoded_data_size):
			_address = _decoded_data[i].address
			_limit = _decoded_data[i].limit
			_name = _decoded_data[i].name
			_parent_level = _decoded_data[i].parent_level

			self._reviewer_whitelist_parent_dict[address]['limit'] = _limit
			self._reviewer_whitelist_parent_dict[address]['name'] = _name
			self._reviewer_whitelist_parent_dict[address]['parent_level'] = _parent_level
			self._reviewer_whitelist_parent_dict[address]['member'] = json_dumps(list())
			if ParentLevel(_parent_level) is ParentLevel.TEAM
				self._reviewer_whitelist_parent_dict[address]['leader'] = ''

	@external
    def sign_up(self, _child_address: Address, _is_leader: bool = False):
		_parent_address = self.msg.sender
		_parent_level = ParentLevel(get_parent_level(_parent_address))
		self._precondition(_child_address.is_contract is False, 'child address is not wallet address')
		self._precondition(check_parent_exist(_parent_address), 'parent address not exist')
		self._precondition(len(self._reviewer_whitelist_parent_dict[_parent_address]['member']) == self._reviewer_whitelist_parent_dict[_parent_address]['limit'], 'member num is over the limit')
		
		if _parent_level is ParentLevel.TEAM and _is_leader is True:
			self._reviewer_whitelist_parent_dict[_parent_address]['leader'] = _child_address
			self._reviewer_whitelist_child_dict[_child_address]['parent_address'] = _parent_address
			self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.LEADER.value)
		else:
			member_arr = json_loads(self._reviewer_whitelist_parent_dict[_parent_address]['member'])
			member_arr.append(_child_address)
			self._reviewer_whitelist_parent_dict[_parent_address]['member'] = json_dumps(member_arr)
			self._reviewer_whitelist_child_dict[_child_address]['parent_address'] = _parent_address
			if _parent_level is ParentLevel.TEAM:
				self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.MEMBER.value)
			else:
				self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.ORACLE.value)
		
		self._transfer(_child_address, 1 * ICX)

	@external
    def close_vote(self, _project_address: Address):
		self._precondition(self.msg.sender == self.owner, 'not owner')
		_score = self._get_project_score(_project_address)
		_score._close_vote()
	
	@external
    def distribute_icx_and_close_project(self, _project_address: Address):
		self._precondition(self._reviewer_whitelist_child_dict[self.msg.sender]['child_level'] == str(ChildLevel.LEADER.value), 'not leader')
		_score = self._get_project_score(_project_address)
		_prize_amount = _score.get_prize()
		_gainer_list = _score._get_gainer_list()
		for i in range(len(_gainer_list)):
			self._transfer(_gainer_list[i], _prize_amount * ICX)
		_score._close_project()

	@payable
    def fallback(self):
		pass

	# ==================================================================================================================
    # local instance method
    # ==================================================================================================================

	def _precondition(self, condition: bool, message: str=None):
        if not condition:
            self.revert(f'PRECONDITION FAILED !!' if message is None else message)

	def _get_project_score(self, _project_score: Address) -> IDpesProject:
		self._precondition(_project_score.is_contract, '_project_score is not contract address')
        return self.create_interface_score(_project_score, IDpesProject)
	
	def _transfer(self, _to: Address, _value: int):
        score_balance = self.Icx.get_balance(self.address)
        self._precondition(0 < _value <= score_balance)
        self.Icx.transfer(_to, _value)

	# ==================================================================================================================
    # static method (utils)
    # ==================================================================================================================
	
	# @staticmethod
    # def _get_rate(amount: int, rate: int) -> int:
    #     if amount <= 0:
    #         return 0
    #     else:
    #         return int(amount * rate / MILLION)
