<script>
/* eslint-disable */
export default {
  name: 'Index',
  data() {
    return {
      indexTopBg: require('../assets/index-top-bg.jpg'),
      indexBottomBg: require('../assets/index-bottom-bg2.jpg'),
    }
  }
};
</script>

<template>
<!-- eslint-disable -->
<div style="height:100%;">
  <section class="jumbotron jumbotron-wide set-bg mb-0" :style="{ 'backgroundImage': 'url(\'' + indexTopBg + '\')' }">
    <div class="text-white container">
      <div class="row">
        <div class=" col-md-8 offset-sm-1 col-sm-10 offset-sm-1" style="text-align:left;">
          <h1 class="font-weight-extra-bold" style="font-size:45px;">우주 최초의 <br />완전한 탈중앙화 성과 평가 시스템</h1>
          <p class="h5">누가 나를 평가했는지 알 수 없으며, 인센티브의 지급을 100% 알 수 있습니다. 당신의 평판을 관리하고, 인센티브를 수령하세요.</p>
          <div class="pt-3">
            <router-link :to="{name: 'getstarted'}" tag="button" class="btn btn-light" style="padding:13px;">즉시 평가하기</router-link>
            <router-link :to="{name: 'easteregg'}" tag="button" class="ml-2 btn btn-outline-light" style="padding:13px;">자세히 알아보기</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="jumbotron jumbotron-wide bg-white text-dark">

    <div class="container">
      <div class="row">
        <div class="offset-md-2 col-md-8 offset-md-2">
          <h2 class="font-weight-extra-bold">가장 객관적인 성과 평가 시스템</h2>
          <hr class="my-hr bg-dark" />
          <p class="h5">DPES는 가장 객관적인 성과 평가 시스템입니다. 개인 혹은 소수의 판단력에 의존하지 않고, 복수의 동등한 팀원들에게 평가를 받을 수 있으며,
            평가 과정은 완전히 탈중앙화되어 100% 신뢰할 수 있습니다. 완전하게 익명화 된 블록체인 위에서 정교한 평가 시트를 채워보세요.
          </p>

          <div class="row mt-5 mb-5">
            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-1.jpg" alt="Card image cap">
                <div class="">
                  <h5 class="mt-5">익명성</h5>
                  <p class="mt-4">
                    오로지 같은 그룹에 속한 인원들만 비밀 계정을 인증 받을 수 있으며,
                    인증된 비밀 계정을 기반으로 완전하게 익명화 된 평가를 수행할 수 있습니다.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-3.jpg" alt="Card image cap">
                <div class="mt-5">
                  <h5 class="">투명성</h5>
                  <p class="mt-4">
                    비밀 계정이 누구를 평가했으며, 몇 명을 평가했는지 명확하게 알 수 있습니다. 평가 과정과 내용은 완전히 공개되며, 인센티브가 지급되는 과정을 선명하게 지켜볼 수 있습니다.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-2.jpg" alt="Card image cap">
                <div class="mt-5">
                  <h5 class="">불변성</h5>
                  <p class="mt-4">
                    평가 내용은 완전히 탈중앙화 된 블록체인 위에 구축되어 있어, 그 누구도 조작할 수 없고, 절대로 변조되지 않습니다. 우리는 이 평가를 100% 신뢰할 수 있습니다.
                  </p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

  </section>

  <section class="jumbotron jumbotron-wide set-bg mb-0" :style="{ 'backgroundImage': 'url(\'' + indexBottomBg + '\')' }">

    <div class="text-white container">
      <div class="row">
        <div class="col-md-6">
        </div>
        <div class="col-md-6">
          <h2 class="font-weight-extra-bold">지금 당장 평가에 참여해보세요!</h2>
          <hr class="my-hr bg-light" />
          <p class="h5">
            동료의 성과를 평가하는 것은 꽤 어려운 일입니다. 그러나, 당신의 진실한 평가는 동료가 더욱 발전할 수 있는 밑거름이 될 수 있습니다.
            지금 당장 비밀 계정을 인증하고, 평가의 트랜잭션을 생성해보세요. 당신이 쏘아올린 트랜잭션 하나가 동료의 미래를 바꿀 수 있습니다.
          </p>
        </div>
      </div>
    </div>

  </section>

  <section class="jumbotron jumbotron-wide bg-white text-body">

    <div class="container">
      <div class="row">
        <div class="offset-md-1 col-md-10 offset-md-1">
          <h2 class="font-weight-extra-bold">사용 고객 후기</h2>
          <hr class="my-hr bg-dark" />
          <p>
            <div class="card-columns">

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-tapp.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">너무나 좋아요</h5>
                  <p class="card-text">익명평가 짱</p>
                  <p class="card-text"><small class="text-muted">DappScott Blockchain Master</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-glory.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">한번 쓰면 못 벗어나는 솔직함의 맛</h5>
                  <p class="card-text">동료 간의 익명 평가는 나에게 성장에 대한 자극을 준다.
                    동료들에게 진정으로 좋은 평가를 받아 획득하는 ICX는 그 어떤 것보다도 짜릿하다.</p>
                  <p class="card-text"><small class="text-muted">임영광 비즈니스기획팀</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-minkim.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">Worth posting on Twitter!</h5>
                  <p class="card-text">오랜만에 발견한 포스팅할만한 DApp. 이 DApp은 블록체인의 특성을 가장 잘 활용하였다!</p>
                  <p class="card-text"><small class="text-muted">Min Kim ICON Council</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-jh.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">함께 느낄 수 있는 앱</h5>
                  <p class="card-text">
                    Con(함께)과 Sense(느끼다)의 콘셉을 잘 구현했네요.</p>
                  <p class="card-text"><small class="text-muted">갓종협 ICON Council</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-hk.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">최고의 동료 평가 시스템</h5>
                  <p class="card-text">DPES는 완전히 익명 평가가 가능하기 때문에 동료에 대해 솔직한 평가를 남길 수 있습니다.
                    또한, 분산화 된 네트워크 내에 위치하고 있기 때문에, 회사의 소유가 아니며, 회사가 내용을 조작할 수도 없어서 신뢰가 가네요.</p>
                  <p class="card-text"><small class="text-muted">신현구 선행기술팀</small></p>
                </div>
              </div>
              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/t-cute.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">다면평가를 위한 획기적인 솔루션</h5>
                  <p class="card-text">다면평가를 절대평가로 수행함으로서 네거티브 평가를 막았고, 여러 장치를 통해 담합 평가를 막은 것이 인상적이다!</p>
                  <p class="card-text"><small class="text-muted">탁형진 인사팀장</small></p>
                </div>
              </div>
            </div>
          </p>
        </div>
      </div>

    </div>

  </section>

  <section class="jumbotron jumbotron-wide bg-dark text-white">

    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h2 class="font-weight-extra-bold">ICON Foundation 출신의<br />창업가들이 이끌다</h2>
          <hr class="my-hr bg-white" />
          <p class="h5">
            이 놀라운 시스템은 과연 누가 구축했을까요?
            DPES는 ICON Network를 이끌던 천재 개발자와 비즈니스맨, 그리고 프로덕트 전문가가 뭉쳤습니다.
            이 창업자들은 블록체인 및 인터넷 산업에서 수많은 웹과 모바일 비즈니스를 전개해왔습니다.
            이제는 새로운 비전과 포부 아래 탈중앙화 된 인터넷의 가치를 구현하려고 합니다.
          </p>
        </div>
        <div class="col-md-6">
          <img src="../assets/index_cofounders.jpg" class="img-fluid" alt="cofounder-image">
        </div>

      </div>

    </div>

  </section>

</div>
</template>
