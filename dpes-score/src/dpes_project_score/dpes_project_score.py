from iconservice import *

# ==================================================================================================================
#	interface
# ==================================================================================================================

class IDpes(InterfaceScore):
	@interface
	def check_child_exist(self, child_address: Address) -> bool:
		pass
	@interface
	def get_child_level(self, child_address: Address) -> int:
		pass
	@interface
	def get_team_count(self) -> int:
		pass	
	@interface
	def distribute_prize(self, project_address: Address, prize_amount: int, formatted_score_and_gainer_dict: str) -> None:
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
WEIGHT_ARR = [
	8,
	6.666,
	6.666,
	6.666,
	6.666,
	8,
	6.666,
	8,
	6.666,
	6.666,
	5.333,
	5.333,
	5.333,
	5.333,
	8
]
WEIGHT_SUM = 100

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

class DpesProjectScore(IconScoreBase):

	_NAME = "_NAME"
	_DESC = "_DESC"
	_PRIZE_AMOUNT = "_PRIZE_AMOUNT"
	_DUE_DATE = "_DUE_DATE"
	_STATUS = "_STATUS"
	_THRESHOLD = "_THRESHOLD"

	_SCORE_DICT = "_SCORE_DICT"
	_TOTAL_SCORE_DICT = "_TOTAL_SCORE_DICT"
	_REVIEW_DICT = "_REVIEW_DICT"
	_MESSAGE_DICT = "_MESSAGE_DICT"

	_USER_ARRAY = "_USER_ARRAY"
	_REVIEWER_DICT = "_REVIEWER_DICT"

	_AUDIT_HISTORY_DICT = "_AUDIT_HISTORY_DICT"
	_AUDIT_COUNT = "_AUDIT_COUNT"

	_DPES_SCORE_ADDRESS = "_DPES_SCORE_ADDRESS"

	def __init__(self, db: IconScoreDatabase) -> None:
		super().__init__(db)
		self._name = VarDB(self._NAME, db, str)
		self._desc = VarDB(self._DESC, db, str)
		self._prize_amount = VarDB(self._PRIZE_AMOUNT, db, int)
		self._due_date = VarDB(self._DUE_DATE, db, int)
		self._threshold = VarDB(self._THRESHOLD, db, int)
		
		self._status = VarDB(self._STATUS, db, int)
		self._score_dict = DictDB(self._SCORE_DICT, db, value_type=int, depth=2)
		self._total_score_dict = DictDB(self._TOTAL_SCORE_DICT, db, value_type=int)
		self._review_dict = DictDB(self._REVIEW_DICT, db, value_type=str, depth=2)
		self._message_dict = DictDB(self._MESSAGE_DICT, db, value_type=str, depth=2)
		
		self._user_array = ArrayDB(self._USER_ARRAY, db, value_type=Address)
		self._reviewer_dict = DictDB(self._REVIEWER_DICT, db, value_type=str)

		self._audit_history_dict = DictDB(self._AUDIT_HISTORY_DICT, db, value_type=bool)
		self._audit_count = VarDB(self._AUDIT_COUNT, db, value_type=int)

		self._dpes_score_address = VarDB(self._DPES_SCORE_ADDRESS, db, Address)

	def on_install(self,
				   name: str,
				   desc: str,
				   prize_amount: int,
				   due_date: int,
				   dpes_score_address: Address,
				   threshold: int
				   ):
		super().on_install()
		self._precondition(due_date >= self.now())
		self._precondition(prize_amount >= 0, 'Prize amount is less than 0')
		self._precondition(dpes_score_address.is_contract, 'Address is not contract')
		self._name.set(name)
		self._desc.set(desc)
		self._prize_amount.set(prize_amount)
		self._due_date.set(due_date)
		self._threshold.set(threshold)
		self._status.set(ProjectStatus.ACTIVE)
		self._audit_count.set(0)
		self._dpes_score_address.set(dpes_score_address)

	def on_update(self,
				   name: str,
				   desc: str,
				   prize_amount: int,
				   due_date: int,
				   dpes_score_address: Address
				   ):
		super().on_update()
		self._name.set(name)
		self._desc.set(desc)
		self._prize_amount.set(prize_amount)
		self._due_date.set(due_date)
		self._dpes_score_address.set(dpes_score_address)
	
	@external(readonly=True)
	def get_project_info(self) -> dict:
		return {
			'name': self._name.get(),
			'desc': self._desc.get(),
			'prize_amount': self._prize_amount.get(),
			'due_date': self._due_date.get(),
			'status': self._status.get()
		}
	
	@external(readonly=True)
	def get_message_list(self, _user_address: Address) -> list:
		_message_list = list()
		_reviewer_list = json_loads(self._reviewer_dict[_user_address])
		for i in range(len(_reviewer_list)):
			_from = Address.from_string(_reviewer_list[i]['from'])
			_message_item = {
				'message': self._message_dict[_user_address][_from],
				'from': _from
			}
			_message_list.append(_message_item)
		return _message_list
	
	@external(readonly=True)
	def get_review_result(self, _user_address: Address) -> list:
		_review_list = list()
		_reviewer_list = json_loads(self._reviewer_dict[_user_address])
		for i in range(len(_reviewer_list)):
			_from = Address.from_string(_reviewer_list[i]['from'])
			_review = json_loads(self._review_dict[_user_address][_from])
			_score = self._score_dict[_user_address][_from]
			_review_list.append({
				'score': _score,
				'review_list': _review,
				'from': _from
			})
		return _review_list
	
	@external
	def vote(
			self, 
			_from: Address, 
			_to: Address,
			_formatted_json: str,
			# 
			# 	type: 'bool',
			# 	value: 1 (0: False, 1: True)
			#
			# 	type: 'int',
			# 	value: 3 (1, 2, 3, 4, 5)
			# 
			_message: str
		):

		self._precondition(self._status.get() == ProjectStatus.ACTIVE, 'project is not active')
		_score = self._get_dpes_score(self._dpes_score_address.get())
		self._precondition(_score.check_child_exist(_from) is True, 'not whitelisted address')
		_from_level = _score.get_child_level(_from)
		self._precondition(_from_level != ChildLevel.LEADER, 'leader address has no permission')
		self._precondition(self._score_dict[_to][_from] != '', 'Already voted')
		
		_total_score = float()
		_answer_array = list()
		_decoded_data = json_loads(_formatted_json)
		_decoded_data_size = len(_decoded_data)
		for i in range(_decoded_data_size):
			_answer_score = 0
			_weight = WEIGHT_ARR[i] 
			if _decoded_data[i]['type'] == 'int':
				_answer_score = self._hex_to_int(_decoded_data[i]['value']) * 20
				_answer_array.append(_answer_score)
				_total_score += round(float(_answer_score) * float(_weight) / float(WEIGHT_SUM))
			else:
				_answer_score = self._hex_to_int(_decoded_data[i]['value']) * 100
				_answer_array.append(_answer_score)
				_total_score += round(float(_answer_score) * float(_weight) / float(WEIGHT_SUM))
		
		if not self._reviewer_dict[_to]:
			self._user_array.put(_to)

		_reviewer_list = list()
		if self._reviewer_dict[_to]:
			_reviewer_list = json_loads(self._reviewer_dict[_to])
		_reviewer_list.append({
			'from': str(_from),
			'from_level': _from_level
		})
		self._reviewer_dict[_to] = json_dumps(_reviewer_list)
		self._score_dict[_to][_from] = int(_total_score)
		self._review_dict[_to][_from] = json_dumps(_answer_array)
		self._message_dict[_to][_from] = _message
	
	@external
	def close_vote(self) -> None:
		self._precondition(self._is_dpes_score(self.msg.sender), 'not called by dpes score')
		self._calculate_score()
		self._status.set(ProjectStatus.AUDIT)
	
	@external
	def audit_vote(self, _leader_address: Address) -> None:
		self._precondition(self._status.get() == ProjectStatus.AUDIT, 'not audit phase')
		self._precondition(self._is_dpes_score(self.msg.sender), 'not called by dpes score')
		self._precondition(self._audit_history_dict[_leader_address] == False, 'already audited')
		self._audit_history_dict[_leader_address] = True
		audit_count = self._audit_count.get() + 1
		self._audit_count.set(audit_count)

		_score = self._get_dpes_score(self._dpes_score_address.get())
		_team_count = _score.get_team_count()

		if self._audit_count.get() >= _team_count:
			_score_and_gainer_dict = self._get_score_and_gainer_list()
			_score.distribute_prize(self.address, self._prize_amount.get(), json_dumps(_score_and_gainer_dict))
			self._status.set(ProjectStatus.CLOSE)

	# ==================================================================================================================
	# local instance method
	# ==================================================================================================================

	def _precondition(self, condition: bool, message: str=None):
		if not condition:
			self.revert(f'PRECONDITION FAILED !!' if message is None else message)

	def _get_dpes_score(self, _dpes_score: Address) -> IDpes:
		self._precondition(_dpes_score.is_contract, '_dpes_score is not contract address')
		return self.create_interface_score(_dpes_score, IDpes)

	def _calculate_score(self) -> None:
		for i in range(len(self._user_array)):
			_user = self._user_array[i]
			_reviewer_list = json_loads(self._reviewer_dict[_user])
			_weight_sum = 0
			_user_total_score = 0
			for v in range(len(_reviewer_list)):
				_reviewer = Address.from_string(_reviewer_list[v]['from'])
				_reviewer_level = _reviewer_list[v]['from_level']
				_reviewer_weight = 1 if _reviewer_level == ChildLevel.ORACLE else 2
				_weight_sum += _reviewer_weight
				_user_total_score += (self._score_dict[_user][_reviewer] * _reviewer_weight)
			_user_total_average_score = round(_user_total_score / _weight_sum)
			self._total_score_dict[_user] = _user_total_average_score

	def _get_score_and_gainer_list(self) -> dict:
		_score_list = list()
		_gainer_list = list()
		for i in range(len(self._user_array)):
			_user_address = self._user_array[i]
			_score = self._total_score_dict[_user_address]
			_score_list.append({
				'user_address': str(_user_address),
				'score': _score
			})
			if (_score > self._hex_to_int(self._threshold)):
				_gainer_list.append(str(_user_address))
		return {
			'score': _score_list,
			'gainer': _gainer_list
		}

	def _is_dpes_score(self, _dpes_address: Address) -> bool:
		return True if _dpes_address == self._dpes_score_address.get() else False

	# ==================================================================================================================
	# static method
	# ==================================================================================================================

	@staticmethod
	def _hex_to_int(a: str) -> int:
		return int(a, 16)