from iconservice import *

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
	def check_child_exist(self, child_address: Address) -> bool:
		"""
		:param child_address: child address
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
	def get_child_level(self, child_address: Address) -> int:
		"""
		:param child_address: child address
		:return: int
		"""
		pass

	@abstractmethod
	def create_parent_dict(self, formatted_json: str) -> None:
		"""
		:param formatted_json: parent json array (e.g. '[{"address":"address_1", "limit":10}, {...}]')
			• address
			• parent_name
			• limit
			• parent_level (team, oracle)
		:return: None
		"""
		pass
	
	@abstractmethod
	def sign_up(self, child_address: Address, is_leader: int) -> None:
		"""
		:param 
			child_address: child address
			is_leader: whether leader of team or not (0x0, 0x1)
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
	def audit_vote(self, _project_address: Address) -> None:
		"""
		:param project_address: project cx address
		"""
		pass
	
	@abstractmethod
	def get_team_count(self) -> int:
		"""
		:return: team count
		"""
		pass
	
	@abstractmethod
	def distribute_prize(self, project_address: Address, prize_amount: int, formatted_score_and_gainer_dict: str) -> None:
		"""
		:param 
			project_address: project cx address
			formatted_score_and_gainer_dict: score list, gainer list included
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
	def get_project_info(self) -> dict:
		pass
	@interface
	def audit_vote(self, leader_address: Address) -> None:
		pass
	@interface
	def _get_team_member_score_and_gainer_list(self, formatted_member_list: str) -> dict:
		pass
	@interface
	def close_vote(self, project_address: Address) -> None:
		pass
	
class Error():
	def __init__(self, message):
		self.message = message
	def throw(self) -> dict:
		return {
			'error': message
		}

# ==================================================================================================================
#	constants
# ==================================================================================================================

TAG = 'DpesScore'
ICX = 10 ** 18

class UserGrade():
	A = 1
	B = 2
	C = 3
	D = 4
	E = 5

class ParentLevel():
	TEAM = 1
	ORACLE = 2

class ChildLevel():
	MEMBER = 1
	LEADER = 2
	ORACLE = 3

class ProjectStatus():
	ACTIVE = 1
	AUDIT = 2
	CLOSE = 3

# ==================================================================================================================
#	main source
# ==================================================================================================================

class DpesScore(IconScoreBase, IDpesScore):

	_USER_TOTAL_PRIZE_DICT = "_USER_TOTAL_PRIZE_DICT"
	_USER_TOTAL_SCORE_DICT = "_USER_TOTAL_SCORE_DICT"
	_USER_HISTORY_DICT = "_USER_HISTORY_DICT"
	_REVIEWER_WHITELIST_PARENT_DICT = '_REVIEWER_WHITELIST_PARENT_DICT'
	_REVIEWER_WHITELIST_CHILD_DICT = '_REVIEWER_WHITELIST_CHILD_DICT'
	
	_TEAM_COUNT = '_TEAM_COUNT'
	_PROJECT_WHITELIST = '_PROJECT_WHITELIST'
	_PROJECT_COUNT = '_PROJECT_COUNT'

	def __init__(self, db: IconScoreDatabase) -> None:
		super().__init__(db)
		self._user_total_prize_dict = DictDB(self._USER_TOTAL_PRIZE_DICT, db, value_type=int)
		self._user_total_score_dict = DictDB(self._USER_TOTAL_SCORE_DICT, db, value_type=int)
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
		self._team_count = VarDB(self._TEAM_COUNT, db, value_type=int)
		self._project_count = VarDB(self._PROJECT_COUNT, db, value_type=int)
		self._project_whitelist = DictDB(self._PROJECT_WHITELIST, db, value_type=bool)
	
	def on_install(self) -> None:
		super().on_install()
		self._team_count.set(0)
		self._project_count.set(0)

	def on_update(self) -> None:
		super().on_update()

	@external(readonly=True)
	def get_user_info(self, _user_address: Address) -> dict:
		_project_count = self._project_count.get()
		if _project_count == 0:
			return {
				'balance': 0,
				'grade': 0
			}
		_balance = self._user_total_prize_dict[_user_address]
		_grade = round(self._user_total_score_dict[_user_address] / _project_count)
		return {
			'balance': _balance,
			'grade': _grade
		}

	@external(readonly=True)
	def check_parent_exist(self, _parent_address: Address) -> bool:
		return False if not self._reviewer_whitelist_parent_dict[_parent_address]['name'] else True
	
	@external(readonly=True)
	def check_child_exist(self, _child_address: Address) -> bool:
		return False if not self._reviewer_whitelist_child_dict[_child_address]['parent_address'] else True

	@external(readonly=True)
	def get_parent_level(self, _parent_address: Address) -> int:
		_parent_level = self._reviewer_whitelist_parent_dict[_parent_address]['parent_level']
		return 0 if not _parent_level else self._hex_to_int(_parent_level)

	@external(readonly=True)
	def get_child_level(self, _child_address: Address) -> int:
		_child_level = self._reviewer_whitelist_child_dict[_child_address]['child_level']
		return 0 if not _child_level else self._hex_to_int(_child_level)
	
	@external(readonly=True)
	def get_team_count(self) -> int:
		return self._team_count.get()

	@external
	def create_parent_dict(self, _formatted_json: str):
		self._precondition(self.msg.sender == self.owner, 'not owner')
		_decoded_data = json_loads(_formatted_json)
		_decoded_data_size = len(_decoded_data)
		for i in range(_decoded_data_size):
			_address = Address.from_string(_decoded_data[i]['address'])
			_limit = _decoded_data[i]['limit']
			_name = _decoded_data[i]['name']
			_parent_level = _decoded_data[i]['parent_level']

			self._reviewer_whitelist_parent_dict[_address]['limit'] = _limit
			self._reviewer_whitelist_parent_dict[_address]['name'] = _name
			self._reviewer_whitelist_parent_dict[_address]['parent_level'] = _parent_level
			self._reviewer_whitelist_parent_dict[_address]['member'] = json_dumps(list())
			if self._hex_to_int(_parent_level) is ParentLevel.TEAM:
				self._reviewer_whitelist_parent_dict[_address]['leader'] = ''
				_team_count = self._team_count.get() + 1
				self._team_count.set(_team_count)
			
			self._transfer(_address, 3 * ICX)

	@external
	def sign_up(self, _child_address: Address, _is_leader: int):
		_parent_address = self.msg.sender
		_is_leader_bool = False if _is_leader == 0 else True 
		_parent_level = self.get_parent_level(_parent_address)
		self._precondition(_child_address.is_contract is False, 'child address is not wallet address')
		self._precondition(self.check_parent_exist(_parent_address), 'parent address not exist')
		
		if _parent_level is ParentLevel.TEAM and _is_leader_bool is True:
			self._precondition(self._reviewer_whitelist_parent_dict[_parent_address]['leader'] == '', 'leader is already exist')
			self._reviewer_whitelist_parent_dict[_parent_address]['leader'] = str(_child_address)
			self._reviewer_whitelist_child_dict[_child_address]['parent_address'] = str(_parent_address)
			self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.LEADER)
		else:
			self._precondition(len(json_loads(self._reviewer_whitelist_parent_dict[_parent_address]['member'])) < self._hex_to_int(self._reviewer_whitelist_parent_dict[_parent_address]['limit']), 'member num is over the limit')
			member_arr = json_loads(self._reviewer_whitelist_parent_dict[_parent_address]['member'])
			member_arr.append(str(_child_address))
			self._reviewer_whitelist_parent_dict[_parent_address]['member'] = json_dumps(member_arr)
			self._reviewer_whitelist_child_dict[_child_address]['parent_address'] = str(_parent_address)
			if _parent_level is ParentLevel.TEAM:
				self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.MEMBER)
			else:
				self._reviewer_whitelist_child_dict[_child_address]['child_level'] = str(ChildLevel.ORACLE)
		
		self._transfer(_child_address, 1 * ICX)

	@external
	def close_vote(self, _project_address: Address):
		self._precondition(self.msg.sender == self.owner, 'not owner')
		self._precondition(self._project_whitelist[_project_address] == False, 'you already closed vote on this project')
		self._project_whitelist[_project_address] = True
		_score = self._get_project_score(_project_address)
		_score.close_vote()
	
	@external
	def audit_vote(self, _project_address: Address):
		self._precondition(self._reviewer_whitelist_child_dict[self.msg.sender]['child_level'] == str(ChildLevel.LEADER), 'not leader')

		_score = self._get_project_score(_project_address)
		_score.audit_vote(self.msg.sender)
	
	@external
	def distribute_prize(self, _project_address: Address, _prize_amount: int, _formatted_score_and_gainer_dict: str):
		self._precondition(self._project_whitelist[self.msg.sender], 'not whitelisted project')
		_team_score_and_gainer_dict = json_loads(_formatted_score_and_gainer_dict)
		
		_score_list = _team_score_and_gainer_dict['score']
		_gainer_list = _team_score_and_gainer_dict['gainer']
		for i in range(len(_score_list)):
			# save project score in history and grade
			_user_address = Address.from_string(_score_list[i]['user_address'])
			_score = _score_list[i]['score']
			self._user_history_dict[_user_address][_project_address] = _score
			self._user_total_score_dict[_user_address] += _score

		for i in range(len(_gainer_list)):
			_gainer_address = Address.from_string(_gainer_list[i])
			self._user_total_prize_dict[_gainer_address] += _prize_amount
			self._transfer(_gainer_address, _prize_amount)
		
		_new_project_count = self._project_count.get() + 1
		self._project_count.set(_new_project_count)

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
		self._precondition(0 < _value <= score_balance, 'transfer failed')
		self.icx.transfer(_to, _value)

	# ==================================================================================================================
	# static method
	# ==================================================================================================================

	@staticmethod
	def _hex_to_int(a: str) -> int:
		return int(a, 16)