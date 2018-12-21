# 2018 Ultimate ICON - team Contact

## Prediction Game
This is a simple majority game. players can play as either giving questions or picking up an answer.

## Rules of this game
1. when having even result, everyone gets refunded their deposit after the question giver gets his(or her) incentive.
2. when more people choose an answer, the majority shares the deposit of the minority after the question giver gets his(or her) incentive.

## Goal of this game
1. when giving a question, one should try to get the even result, so that he(or she) would be the only one who gets incentive.
2. when picking an answer, one should try to guess the answer which the majority select. But one should try to choose an answer which is chosen slightly more people to maximize one's incentive.
## Step of this game
1. A player gives a question.
2. Players select their answer; at this stage, people cannot know the answer of other, since the answer is hashed.
3. After the answering stage, players verify their answer; at this stage, people verifiy their answer, and they get another hashed answer. SCORE compares those 2 hash(one from step2 and the other from step3), and if they match, then SCORE counts it as a valid score.
4. After verifying stage, SCORE calculates the incentive and sends it to winners.
## Incentives
when the number of majority is A, the number of minority is B, the number of people who gives up to verify their choice is C, and the amount of deposit per a game is d,
1. question giver's incentive when there is a winner = (B+C) * d * x / 100
2. question giver's incentive when there is no winner = (A+B+C) * d * x / 100
3. participant's incentive when there is a winner = (B+C) * d / A
4. when there is no winner, participants will get refunded after deducting the question giver's incentive.
5. x=1%(when less then 50 people participate), 3%(when more than 50 and less than 100 people participate), or 5%(when more than 100 people participate)

## Tutorial
This section describes how to run and manage the prediction game.

### deploy

Deploy PredictionGame SCORE. after deploying the PredictionGame SCORE, anyone can participate in the prediction game by generating questions and voting to questions.

When deploying SCORE, there is no parameter to input.

### generatePrediction

Generate a question. After this method to be executed and recorded to the blockchain, players can select an answer of a question for a period of time (this period is called `VOTING_PERIOD` and calculated using block height). The answers about questions can be set up to two (e.g. red or blue, left or right).

#### example

```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "",
    "value": "0x0",
    "stepLimit": "0x3000000000000",
    "timestamp": "0x573117f1d6568",
    "nid": "0x3",
    "nonce": "0x1",
    "to": "cx527fc74c42c8ae7fc2fea7a87790e94c0ef3b9aa",
    "dataType": "call",
    "data": {
      "method": "generatePrediction",
      "params": {
        "subject": "red or blue",
        "items": "red,blue",
        "description": "example question"
      }
    }
  },
  "id": 1
}
```

### votePrediction

Select an answer of a generated question. Anyone can select an answer to a question. When selecting an answer, players have to deposit 1ICX for a participation fee (This fee is used as distributing incentive for question creator and winner).

When selecting an answer to a question, input hashed data for concealing it to others. The below is the rule of generating hash data.

1) serializing data

score Address(string type) + voter Address(string type) + item(string type) + nonce(int type)

````python
# serialized_data = cx8e903f7d755e037a71b312cb2ef46285596ea0f0hx812400b607d6b2e1b274faf576b9a2fd59bc8f2dred0
serialized_data = "cx8e903f7d755e037a71b312cb2ef46285596ea0f0" + "hx812400b607d6b2e1b274faf576b9a2fd59bc8f2d" + "red" + str(0)
````

2) hashing data

Encode the serialized data and hashing it using sha3.

```python
# hashed_data = 74d31a749094b0ef98f82b1a1a0ffa34896b2dc0e65c526e32c9889c06231885
hashed_data = sha3_256(serialized_data.encode()).hex()
```

As an answer is recorded in the form of hash, no one can verify the others answer.

#### example

```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "",
    "value": "0x0",
    "stepLimit": "0x3000000000000",
    "timestamp": "0x573117f1d6568",
    "nid": "0x3",
    "nonce": "0x1",
    "to": "cx527fc74c42c8ae7fc2fea7a87790e94c0ef3b9aa",
    "dataType": "call",
    "data": {
      "method": "votePrediction",
      "params": {"prediction_num": "0x00", "hashed_vote": "74d31a749094b0ef98f82b1a1a0ffa34896b2dc0e65c526e32c9889c06231885"}
    }
  },
  "id": 1
}
```

### validateVote

If the answering period(stage) expires, a question goes into the counting period(verifying stage). In this period, players who have selected an answer to this questions can disclose an answer he have chosen. The process of disclosure is simple. By inputting the answer(item) he selected and the nonce data which was used to generate the hash data as a parameter, players can disclose their answer(SCORE make hash data using inputted parameters, and compare with the recorded hash data). If players do not disclose their answer, that answer becomes invalid and the 1 ICX which user deposited is given to the winner and the question creator.

#### example

```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "",
    "value": "0x0",
    "stepLimit": "0x3000000000000",
    "timestamp": "0x573117f1d6568",
    "nid": "0x3",
    "nonce": "0x1",
    "to": "cx527fc74c42c8ae7fc2fea7a87790e94c0ef3b9aa",
    "dataType": "call",
    "data": {
      "method": "validateVote",
      "params": {"prediction_num": "0x0", "item": "red", "nonce":"0x0"}
    }
  },
  "id": 1
}
```

### changePredictionState

Change a state of a question. a question has three states ```voting_period```, ```counting_period``` and ```ended```. on voting and counting period, players can change a state of a question if period time(calculated using block height) has expired. 

If the maximum number of votes of a question are fulfilled before exceeding the ```voting period```, automatically go to the ```counting period```.

If all votes of a question are disclosed before exceeding ```counting period```, automatically go to the ```ended```.

#### example

```json
{
  "jsonrpc": "2.0",
  "method": "icx_sendTransaction",
  "params": {
    "version": "0x3",
    "from": "",
    "value": "0x0",
    "stepLimit": "0x3000000000000",
    "timestamp": "0x573117f1d6568",
    "nid": "0x3",
    "nonce": "0x1",
    "to": "cx527fc74c42c8ae7fc2fea7a87790e94c0ef3b9aa",
    "dataType": "call",
    "data": {
      "method": "changePredictionState",
      "params": {"prediction_num": "0x0"}
    }
  },
  "id": 1
}
```

### methods (read-only)

Below is the list of read-only methods. By calling these methods, you can get information from the prediction game.

#### getPredictions

Returns a list of predictions.

```python
@external(readonly=True)
def getPredictions(self) -> list:
```

#### getPredictionsByState

Returns a list of predictions by state.

```python
@external(readonly=True)
def getPredictionsByState(self, _state: str) -> list:
```

#### getVoteCountOfEachItem

Returns each answer's total selected count of a question.

```python
@external(readonly=True)
def getVoteCountOfEachItem(self, _predictionNum: int, _items: str) -> dict:
```

#### getWinnerRewardPerVoter

Returns a winner reward per voter of a question.

```python
@external(readonly=True)
def getWinnerRewardPerVoter(self, _predictionNum: int) -> int:
```

#### getCreatorIncentive

Returns a creator incentive of a question.

```python
@external(readonly=True)
def getCreatorIncentive(self, _predictionNum: int) -> int:
```
