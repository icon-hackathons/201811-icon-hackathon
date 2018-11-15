from iconservice import *
from enum import IntEnum

# ==================================================================================================================
#	interface
# ==================================================================================================================

class IDpesScore():
    @abstractmethod
    def get_user_info(self, user_address: Address) -> dict:
        """
		:param user_address: user address
        :return: dict
            • balance
            • grade
        """
        pass
	
	@abstractmethod
    def check_parent_exist(self, parent_address: Address) -> bool:
        """
		:param parent_address: parent address
        :return: bool
        """
        pass
	
	@abstractmethod
    def get_parent_level(self, parent_address: Address) -> int:
        """
		:param parent_address: parent address
        :return: int
        """
        pass

	@abstractmethod
    def create_parent_dict(self, formatted_json: str) -> None:
        """
		:param formatted_json: parent json array (e.g. '[{"account":"address_1", "amount":10}, {...}]')
			• address
            • parent_name
			• limit
			• parent_level (team, oracle)
        :return: None
        """
        pass
	
	@abstractmethod
    def sign_up(self, child_address: Address, is_leader: bool = False) -> None:
        """
		:param 
			child_address: child address
			is_leader: whether leader of team or not
        :return: None
        """
        pass

    @abstractmethod
    def close_vote(self, project_address: Address) -> None:
        """
        :param project_address: project cx address
        """
        pass
	
	@abstractmethod
    def distribute_prize(self, project_address: Address) -> None:
        """
        :param project_address: project cx address
        """
        pass
	
	@abstractmethod
    def _transfer(self, to: Address, value: int):
		"""
        :param 
			to: wallet address
			value: sending amount of icx
        """
        pass

class IDpesProject(InterfaceScore):
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

TAG = 'DpesScore'
ICX = 10 ** 18

_USER_TOTAL_AVERAGE_SCORE_DICT = "_USER_TOTAL_AVERAGE_SCORE_DICT"
_USER_HISTORY_DICT = "_USER_HISTORY_DICT"
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

class DpesScore(IconScoreBase, IDpesScore):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._user_total_average_score_dict = DictDB(self._USER_TOTAL_AVERAGE_SCORE_DICT, db, value_type=int)
		"""
        :user_address - total average score
        """
        self._user_history_dict = DictDB(self._USER_HISTORY_DICT, db, value_type=int, depth=2)
		"""
        :parent_address 
			:limit
			:name
			:parent_level
			:member
			:leader (TEAM only)
        """
        self._reviewer_whitelist_parent_dict = DictDB(self._REVIEWER_WHITELIST_PARENT_DICT, db, value_type=str, depth=2)
		"""
        :child_address 
			:parent_address
			:child_level
        """
		self._reviewer_whitelist_child_dict = DictDB(self._REVIEWER_WHITELIST_CHILD_DICT, db, value_type=str, depth=2)
		
		# !!! TODO !!! : 끝난 프로젝트 cx 이력 모아두는 배열 만들기  
		self._project_history_arr = Arr

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def get_user_info(self, _user_address: Address) -> dict:
		_balance = self.icx.get_balance(_user_address)
		_grade = self._user_total_average_score_dict[_user_address]
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
    def distribute_prize(self, _project_address: Address):
		self._precondition(self._reviewer_whitelist_child_dict[self.msg.sender]['child_level'] == str(ChildLevel.LEADER.value), 'not leader')
		_score = self._get_project_score(_project_address)
		_prize_amount = _score.get_prize()
		_gainer_list = _score._get_gainer_list() # array of dict (.user_address, .average_score)

		for i in range(len(_gainer_list)):
			# save project score in history and grade
			_user_address = _gainer_list[i].user_address
			_average_score = _gainer_list[i].average_score

			# !!! TODO !!!: 포상금 분배 전 각 db에 이력 저장하는 코드 짜기
			self._user_history_dict[_user_address][_project_address] = _average_score

			# transfer prize
			self._transfer(_user_address, _prize_amount * ICX)
		# _score._close_project()

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
        score_balance = self.icx.get_balance(self.address)
        self._precondition(0 < _value <= score_balance)
        self.icx.transfer(_to, _value)

	# ==================================================================================================================
    # static method (utils)
    # ==================================================================================================================
	
	# @staticmethod
    # def _get_rate(amount: int, rate: int) -> int:
    #     if amount <= 0:
    #         return 0
    #     else:
    #         return int(amount * rate / MILLION)