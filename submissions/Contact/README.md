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


