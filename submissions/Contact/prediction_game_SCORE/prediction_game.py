from iconservice import *

ICX = 10 ** 18


class PredictionState:
    ON_VOTING = "on_voting"
    ON_COUNTING = "on_counting"
    ENDED = "ended"


VOTING_PERIOD = 500
COUNTING_PERIOD = 500
REQUIRED_ICX = 21000 * ICX


class Prediction:
    def __init__(self,
                 maker: Address,
                 subject: str,
                 items: str,
                 description: str,
                 required_icx: int = REQUIRED_ICX):
        # immutable data
        self.maker = str(maker)
        self.subject = subject
        self.items = items
        self.description = description
        self.required_icx = required_icx

    @classmethod
    def from_bytes(cls, buf: bytes):
        json_data = json_loads(buf.decode())
        return cls(
            maker=json_data['maker'],
            subject=json_data['subject'],
            items=json_data['items'],
            description=json_data['description'],
            required_icx=json_data['required_icx']
        )

    def to_bytes(self):
        prediction_dict = self.__dict__
        return json_dumps(prediction_dict).encode()


class PredictionGame(IconScoreBase):
    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._predictions = ArrayDB('predictions', db, value_type=bytes)

        self._prediction_state = DictDB('prediction_state', db, value_type=str)
        self._prediction_deposited_icx = DictDB('prediction_deposited_icx', db, value_type=int)
        self._prediction_expire_block_height = DictDB('prediction_expire_block_height', db, value_type=int)
        self._prediction_total_voted_count = DictDB('prediction_total_voted_count', db, value_type=int)

        self._prediction_address_hashed_vote = DictDB('prediction_address_hashed_vote', db, value_type=str, depth=2)
        self._prediction_voter_list = DictDB('prediction_voter_list', db, value_type=str)

        self._prediction_voted_count_by_item = DictDB('prediction_voted_count_by_item', db, value_type=int, depth=2)
        self._prediction_voter_list_by_item = DictDB('prediction_voter_list_by_item', db, value_type=str, depth=2)
        self._prediction_address_open = DictDB('prediction_address_open', db, value_type=bool, depth=2)

        # for front, record reward data
        self._prediction_winner_reward = DictDB('prediction_winner_reward', db, value_type=int)
        self._prediction_creator_incentive = DictDB('prediction_creator_incentive', db, value_type=int)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def generatePrediction(self, _subject: str, _items: str, _description: str, _requiredIcx: int = REQUIRED_ICX):
        # required_icx is will be deprecated ( as this is constant data)
        # add check logic
        new_prediction = Prediction(self.msg.sender, _subject, _items, _description, _requiredIcx)
        new_prediction_num = len(self._predictions)
        self._prediction_state[new_prediction_num] = PredictionState.ON_VOTING
        self._prediction_expire_block_height[new_prediction_num] = self.block_height + VOTING_PERIOD
        self._predictions.put(new_prediction.to_bytes())

    @payable
    def fallback(self):
        revert("you cannot send icx to this score without invest to prediction")

    @payable
    @external
    def votePrediction(self, _predictionNum: int, _hashedVote: str):
        if self._prediction_state[_predictionNum] != PredictionState.ON_VOTING:
            revert("you cannot vote to this prediction as state is not 'on_voting'")
        if self._prediction_expire_block_height[_predictionNum] < self.block_height:
            revert("exceed expire date")
        if _predictionNum < 0 or _predictionNum >= len(self._predictions):
            revert("not existed prediction")
        if self.msg.value != 1 * ICX:
            revert("you can invest only 1 icx")
        if self._prediction_address_hashed_vote[_predictionNum][self.msg.sender] != "":
            revert("you have already voted to this prediction")
        # should be modified (as naive check)
        if len(_hashedVote) != 64:
            revert("invalid hash data")

        self._prediction_total_voted_count[_predictionNum] += 1
        self._prediction_deposited_icx[_predictionNum] += 1 * ICX

        prediction = Prediction.from_bytes(self._predictions[_predictionNum])
        if self._prediction_total_voted_count[_predictionNum] == 1:
            self._prediction_voter_list[_predictionNum] = str(self.msg.sender)
        else:
            self._prediction_voter_list[_predictionNum] += f',{str(self.msg.sender)}'

        self._prediction_address_hashed_vote[_predictionNum][self.msg.sender] = _hashedVote

        if self._prediction_deposited_icx[_predictionNum] == prediction.required_icx:
            self._prediction_state[_predictionNum] = PredictionState.ON_COUNTING
            self._prediction_expire_block_height[_predictionNum] += COUNTING_PERIOD

    @external
    def validateVote(self, _predictionNum: int, _item: str, _nonce: int):
        if self._prediction_state[_predictionNum] != PredictionState.ON_COUNTING:
            revert("you cannot validate vote as this prediction state is not 'on_counting'")
        if self._prediction_expire_block_height[_predictionNum] < self.block_height:
            revert("exceed expire date")
        # check if he has already validated or not
        if self._prediction_address_open[_predictionNum][self.msg.sender]:
            revert("you have already validated vote")

        serialize_vote_info = str(self.address) + str(self.msg.sender) + _item + str(_nonce)

        vote_hash = sha3_256(serialize_vote_info.encode())
        if vote_hash.hex() == self._prediction_address_hashed_vote[_predictionNum][self.msg.sender]:
            self._prediction_address_open[_predictionNum][self.msg.sender] = True
            self._prediction_voted_count_by_item[_predictionNum][_item] += 1
            if self._prediction_voted_count_by_item[_predictionNum][_item] == 1:
                self._prediction_voter_list_by_item[_predictionNum][_item] = str(self.msg.sender)
            else:
                self._prediction_voter_list_by_item[_predictionNum][_item] += f",{str(self.msg.sender)}"
        else:
            revert("hash data dose not match. check the  ")

        prediction = Prediction.from_bytes(self._predictions[_predictionNum])
        items = prediction.items.split(',')
        total_validated_vote = 0
        for _item in items:
            total_validated_vote += self._prediction_voted_count_by_item[_predictionNum][_item]
        if total_validated_vote == self._prediction_total_voted_count[_predictionNum]:
            self._distribute_icx(_predictionNum, Address.from_string(prediction.maker), items)
            self._prediction_state[_predictionNum] = PredictionState.ENDED

    @external
    def changePredictionState(self, _predictionNum: int):
        # anyone can call this method
        # requirement: exceed expire block height.
        # on_voting -> on_counting
        # on_counting -> ended
        if self._prediction_expire_block_height[_predictionNum] >= self.block_height:
            revert("still in period")

        if self._prediction_state[_predictionNum] == PredictionState.ON_VOTING:
            self._prediction_state[_predictionNum] = PredictionState.ON_COUNTING
            self._prediction_expire_block_height[_predictionNum] = self.block_height + COUNTING_PERIOD
            return

        if self._prediction_state[_predictionNum] == PredictionState.ON_COUNTING:
            prediction = Prediction.from_bytes(self._predictions[_predictionNum])
            items = prediction.items.split(',')

            self._distribute_icx(_predictionNum, Address.from_string(prediction.maker), items)
            self._prediction_state[_predictionNum] = PredictionState.ENDED
            return

    def _distribute_icx(self, prediction_num: int, prediction_creator: Address, items: list):
        # after prediction is ended distribute_money
        # v1 = only two items exist
        first_item_vote_count = self._prediction_voted_count_by_item[prediction_num][items[0]]
        second_item_vote_count = self._prediction_voted_count_by_item[prediction_num][items[1]]
        reward_per_voter, creator_incentive = self._calculate_reward_and_fee(prediction_num, items)

        if creator_incentive != 0:
            self.icx.transfer(prediction_creator, creator_incentive)
            # record creator's incentive
            self._prediction_creator_incentive[prediction_num] = creator_incentive

        if first_item_vote_count == second_item_vote_count:
            voter_list: list = self._prediction_voter_list[prediction_num].split(',')
            for voter in voter_list:
                voter = Address.from_string(voter)
                self.icx.transfer(voter, reward_per_voter)
                # record winner reward
                self._prediction_winner_reward[prediction_num] = reward_per_voter
            return

        final_reward_pre_voter = 1 * ICX + reward_per_voter
        if first_item_vote_count > second_item_vote_count:
            winners: list = self._prediction_voter_list_by_item[prediction_num][items[0]].split(',')
            for winner in winners:
                winner = Address.from_string(winner)
                self.icx.transfer(winner, final_reward_pre_voter)
        else:
            winners: list = self._prediction_voter_list_by_item[prediction_num][items[1]].split(',')
            for winner in winners:
                winner = Address.from_string(winner)
                self.icx.transfer(winner, final_reward_pre_voter)
        # record winner reward
        self._prediction_winner_reward[prediction_num] = final_reward_pre_voter

    def _calculate_reward_and_fee(self, prediction_num: int, items: list) -> tuple:
        total_vote_count = self._prediction_total_voted_count[prediction_num]
        first_item_vote_count = self._prediction_voted_count_by_item[prediction_num][items[0]]
        second_item_vote_count = self._prediction_voted_count_by_item[prediction_num][items[1]]

        if first_item_vote_count == second_item_vote_count:
            taker_count = total_vote_count
            giver_count = total_vote_count
        elif first_item_vote_count > second_item_vote_count:
            taker_count = first_item_vote_count
            giver_count = total_vote_count - first_item_vote_count
        else:
            taker_count = second_item_vote_count
            giver_count = total_vote_count - second_item_vote_count

        total_reward = giver_count * ICX
        creator_incentive = self._calculate_creator_incentive(total_vote_count, total_reward)
        total_reward -= creator_incentive

        reward_per_voter = int(total_reward / taker_count)

        return reward_per_voter, creator_incentive

    @staticmethod
    def _calculate_creator_incentive(total_vote_count: int, total_reward: int):
        if total_vote_count >= 100:
            return int(total_reward * 0.1)
        if total_vote_count >= 50:
            return int(total_reward * 0.05)
        if total_vote_count >= 5:
            return int(total_reward * 0.01)
        return 0

    def _make_prediction_info(self, prediction_num: int) -> dict:
        serialized_prediction = self._predictions[prediction_num]
        prediction = Prediction.from_bytes(serialized_prediction)
        prediction_dict = prediction.__dict__
        prediction_dict["state"] = self._prediction_state[prediction_num]
        prediction_dict["deposited_icx"] = self._prediction_deposited_icx[prediction_num]
        prediction_dict["expire_date"] = self._prediction_expire_block_height[prediction_num]
        prediction_dict["total_voted_count"] = self._prediction_total_voted_count[prediction_num]
        prediction_dict["voter_list"] = self._prediction_voter_list[prediction_num]
        prediction_dict["prediction_num"] = prediction_num
        return prediction_dict

    @external(readonly=True)
    def getVoteCountOfEachItem(self, _predictionNum: int, _items: str) -> dict:
        return_data = {}
        _items = _items.split(',')
        for item in _items:
            return_data[item] = self._prediction_voted_count_by_item[_predictionNum][item]
        return return_data

    @external(readonly=True)
    def getAddressValidationInfo(self, _predictionNum: int, _address: Address) -> bool:
        return self._prediction_address_open[_predictionNum][_address]

    @external(readonly=True)
    def getVoteHashByAddress(self, _predictionNum: int, _address: Address) -> str:
        return self._prediction_address_hashed_vote[_predictionNum][_address]

    @external(readonly=True)
    def getPrediction(self, _predictionNum: int) -> dict:
        return self._make_prediction_info(_predictionNum)

    @external(readonly=True)
    def getPredictions(self) -> list:
        prediction_list = []
        for idx in range(len(self._predictions)):
            prediction_list.append(self._make_prediction_info(idx))
        return prediction_list

    @external(readonly=True)
    def getPredictionsByOwner(self, _address: Address) -> list:
        prediction_list = []
        for idx, prediction in enumerate(self._predictions):
            prediction = Prediction.from_bytes(prediction)
            if prediction.maker == str(_address):
                prediction_list.append(self._make_prediction_info(idx))
        return prediction_list

    @external(readonly=True)
    def getPredictionsByVoter(self, _address: Address) -> list:
        prediction_list = []
        prediction_count = len(self._predictions)
        for idx in range(prediction_count):
            if str(_address) in self._prediction_voter_list[idx]:
                prediction_list.append(self._make_prediction_info(idx))
        return prediction_list

    @external(readonly=True)
    def getPredictionsByState(self, _state: str) -> list:
        prediction_list = []
        for idx, prediction in enumerate(self._predictions):
            if self._prediction_state[idx] == _state:
                prediction_list.append(self._make_prediction_info(idx))
        return prediction_list

    @external(readonly=True)
    def getWinnerRewardPerVoter(self, _predictionNum: int) -> int:
        return self._prediction_winner_reward[_predictionNum]

    @external(readonly=True)
    def getCreatorIncentive(self, _predictionNum: int) -> int:
        return self._prediction_creator_incentive[_predictionNum]