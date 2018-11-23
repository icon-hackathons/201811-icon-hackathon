# DPES(Decentralized Performance Evaluation System)

> - 우주 최초의 완전한 탈중앙화 성과 평가 시스템 DPES
> - ICON SCORE 기술을 적용한 탈중앙화 P2P 성과 평가 시스템으로, 온체인에서 지갑을 통해 수평조직 내에서 조직원 간의 평가를 구현.
> - Front-end: Vue.js + Vue router + Vuex + ICON-sdk-js
> - Back-end: Node.js + ICON SCORE(https://www.icondev.io/gettingStart01.do)
> - Utility: [ICONex](https://chrome.google.com/webstore/detail/iconex/flpiciilemghbmfalicajoolhkkenfel?hl=ko)
> - 개발자: 김진현(couldseeme@icon.foundation), 하봉안(bongan@icon.foundation), 김태영(thinktyk@icon.foundation)

## 핵심 가치

#### Value Proposition: Technology

익명성
>- 공개 계정을 통한 피평가
>- 비밀 계정을 통한 평가
>- 아이덴티티 이중화를 통한 완전한 익명화 실현

투명성
>- 평가의 과정과 그 결과가 완전히 투명하게 공개
>- 평가 결과를 통한 인센티브의 전송이 투명하게 공개

불변성
>- 정보가 공용 블록체인에 저장되어 노드 대한 침입, 조작의 가능성 차단

#### Value Proposition: Product

P2P 다면 평가
>- 실무자, 외부 평가자를 통해 피평가자에 대한 정보를 수집하고, 피드백을 확보할 수 있음
>- 평가 결과의 주된 목적은 보상보다는 개발과 조직 관리
>- 조직원들에 대한 구체적인 데이터를 수집할 수 있고, 평가자 간 성장 자극 효과

평가 신뢰 확보
>- 3자 컨센서스를 통해 다면 평가의 결과를 검증하여, 신뢰성 확보

Token Economy 기반 인센티브/패널티
>- 참여자에게 인센티브를 추구하고, 패널티를 회피하게 하여, 합리적으로 행동하도록 유도
>- 평가를 보다 신중하고 신뢰도 있게 만듬

#### Value Proposition: Business

확정적 트랜잭션
>- 네트워크 활성화에 도움되는 활성 트랜잭션이 확정적으로 발생
>- 활성 트랜잭션 발생 수 =
>- ex) 1분기 인사평가를, 10개의 부서가 있으며, 부서 당 10명이 있는 회사일 경우 = 1 x 10 x 100

수익 창출
>- 워크스페이스 개설 시, 차지풀에 토큰 납입.
>- 매 워크스페이스의 24시간마다 Stake된 ICX를 차감하는 Pricing Model 수립

확장성
>- 성과 평과 시스템을 추상화 된 평가 모델로 활용하여, 성과 평과 이외에 다양한 분야로 활용이 가능

## 구성
> - dpes: Vue.js 기반의 프론트엔드 클라이언트
> - dpes-score : ICON Network에서 작동하는 SCORE 기반의 스마트 컨트랙트

## 개발 설정
의존성 모듈들을 설치한 후 `dev` 스크립트 실행
```bash
npm i # npm install
npm run serve
```
## T-Bears 빌드
[링크](https://github.com/icon-project/t-bears)

## Vue.js 빌드
``` bash
# 의존성 설치
npm install

# 로컬호스트 서버로 핫로드(실시간 미리보기)
npm run dev

# 빌드
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# 유닛테스트 실행
npm run unit

# e2e 테스트 실행
npm run e2e

# 모든 테스트 실행
npm test
```

## 가이드
[ICON SCORE](https://www.icondev.io/gettingStart01.do)
[Vue.js](http://vuejs-templates.github.io/webpack/)
[Vue Loader](https://vue-loader-v14.vuejs.org/)
