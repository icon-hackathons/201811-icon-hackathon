# ICON DICE 

ICON DICE는 스코어로 합의 가능한 RNG(Random number generation)가 도출될 수 있는지에 대한 의문으로 시작한 프로젝트 입니다

> house seed와 player seed를 조합하여 난수생성을 하는 것을 이용해서 개발했습니다.

## blockchain gambling의 가치

  1. 익명성
    기존 카지노와 다르게 별도의 kyc과정이 없으며 지갑만 가지고 누구나 플레이 가능합니다.
  2. 투명성
    결과가 블록체인으로 부터 도출되기 때문에 조작의 위험성이 없습니다.
  3. low house edge
    기존 카지노에 들어가는 비용이 없기 때문에 최소한의 비용을 가지고 운영이 가능해 플레이어들이 정당한 보상을 가져갈 수 있게 해줍니다.

## ICON DICE의  SCORE diagram
![179](https://user-images.githubusercontent.com/45279839/49357852-fb752d80-f713-11e8-92de-a5db289060ff.png)
위 다이어 그램은 이렇게 설명될 수 있습니다:

  1. House seed는 하우스만 알고 player seed는 플레이어만 알 수 있다.
  2. House가 house seed를 조작하지 않았음을 증명해야 한다.
  3. 하우스는 플레이어에게 house seed의 hash 값을 보낸다
  4. House seed가 바뀌면 hash값이 바뀜으로 플레이어는 하우스가 조작하지 않았음을 확인할 수 있다
  5. 하우스는 house seed를 블록체인에 보내고 플레이어는 player seed를 블록체인에 기록한다
  6. 블록체인에서는 house seed와 player seed를 단방향 hash 처리한 값을 100으로 나눈 뒤 나머지에 1을 더해 결과 값을 도출한다 (1~100)
  7. 도출된 값을 기반으로 승패를 결정한다.

## ICON DICE의 Actual flow

이번 프로젝트에서 저희는 세가지 단계를 통해 게임을 진행 할 수 있도록 설계 했습니다.

1. 충전
  컨트랙트로 ICX를 충전합니다.
2. 플레이
  게이지바를 조절하여 게임을 진행합니다.
3. 결과
  게임결과가 도출되며 실제 ICX의 이동을 ICONtracker에서 확인 가능합니다

## Value of ICON DICE

1. Transaction 
  이 게임을 통해서 ICON network는 유의미한 트랜잭션을 발생 시킬 수 있습니다.
  게임당 1번의 tx가 고정적으로 생성이되며 충전과 인출을 통해 또한번의 tx가 발생합니다.
2. Benefit
  또한 house edge가 존재하는 이상 수익은 고정적으로 보장됩니다.
3. 확장성
   ICON DICE는 도출된 SCORE을 변형하여 다양한 확률 게임을 만들어 낼 수 있으며,
   추후 게임을 하는것을 통해 토큰 채굴을 가능하게 만들어 자체적인 TOKEN Economy를 설계 할 수 있는 확장성을 가지고 있습니다.

## How to Build

### Web

Install modules with npm

```bash
> Go to web directory
$ cd web

> Install Modules
$ npm install

> Development
$ npm run dev

> Build & Run
$ npm run build && npm run start
```

### Was

```bash
> Go to was directory
$ cd was

> Build with gradle-wrapper
$ ./gradlew build

> Set wallet key file on same directory as executable jar file (You want to deploy score, score zip file also)

> Run
$ java -jar -Dapp.owner.password={OWNER_WALLET_PASSWORD} -Dapp.file.ownerKey={OWNER_WALLET_FILENAME} build/libs/dice.was-1.0.0.jar
```