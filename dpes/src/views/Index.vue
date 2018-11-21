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
          <h1 class="font-weight-extra-bold" style="font-size:45px;">세계 최초의 <br />완전한 탈중앙화 성과 평가 시스템</h1>
          <p class="h5">누가 나를 평가했는지 알 수 없으며, 인센티브의 지급을 100% 알 수 있습니다. 당신의 평판을 관리하고, 인센티브를 수령하세요.</p>
          <div class="pt-3">
            <router-link :to="{name: 'getstarted'}" tag="button" class="btn btn-light" style="padding:13px;">즉시 평가하기</router-link>
            <button type="button" class="btn btn-outline-light" style="margin-left:10px;padding:13px;">자세히 알아보기</button>
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
          <p class="h5">Our planning experience helps you explore what’s possible,whether it’s traditional milestones or unconventional choices.After linking to your accounts, we’ll apply our financial expertise andthe relevant external data to help optimize your finances.All
            without ever requiring you to talk to anyone.
          </p>

          <div class="row mt-5 mb-5">
            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-1.jpg" alt="Card image cap">
                <div class="">
                  <h5 class="mt-5">익명성</h5>
                  <p class="mt-4">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-3.jpg" alt="Card image cap">
                <div class="mt-5">
                  <h5 class="">투명성</h5>
                  <p class="mt-4">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                </div>
              </div>
            </div>

            <div class="col-lg-4 mt-2">
              <div class="">
                <img class="mx-auto mt-4" style="height:100px; width:100px;" src="../assets/index-icon-2.jpg" alt="Card image cap">
                <div class="mt-5">
                  <h5 class="">불변성</h5>
                  <p class="mt-4">This card has supporting text below as a natural lead-in to additional content.</p>
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
          <p class="h5">Our planning experience helps you explore what’s possible,whether it’s traditional milestones or unconventional choices.After linking to your accounts, we’ll apply our financial expertise andthe relevant external data to help optimize your finances.All
            without ever requiring you to talk to anyone.
          </p>
        </div>
      </div>
    </div>

  </section>

  <section class="jumbotron jumbotron-wide bg-white text-body">

    <div class="container">
      <div class="row">
        <div class="offset-md-1 col-md-10 offset-md-1">
          <h2 class="font-weight-extra-bold">말! 말! 말!</h2>
          <hr class="my-hr bg-dark" />
          <p>
            <div class="card-columns">

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">너무나 좋아요</h5>
                  <p class="card-text">익명평가 짱</p>
                  <p class="card-text"><small class="text-muted">비즈니스기획팀</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">한번 쓰면 못 벗어날 맛</h5>
                  <p class="card-text">중독되버렸어</p>
                  <p class="card-text"><small class="text-muted">개발 1팀</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">사랑합니다 DPES!</h5>
                  <p class="card-text">영원히 고고</p>
                  <p class="card-text"><small class="text-muted">비즈니스기획팀</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">한번 쓰면 못 벗어날 맛</h5>
                  <p class="card-text">중독되버렸어</p>
                  <p class="card-text"><small class="text-muted">컨설팅팀</small></p>
                </div>
              </div>

              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">한번 쓰면 못 벗어날 맛</h5>
                  <p class="card-text">중독되버렸어</p>
                  <p class="card-text"><small class="text-muted">글로벌팀</small></p>
                </div>
              </div>
              <div class="card p-4">
                <img class="card-img-top thumbnail round" src="../assets/img_sample.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">한번 쓰면 못 벗어날 맛</h5>
                  <p class="card-text">중독되버렸어</p>
                  <p class="card-text"><small class="text-muted">법무팀</small></p>
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
          <p class="h5">Our planning experience helps you explore what’s possible,whether it’s traditional milestones or unconventional choices.After linking to your accounts, we’ll apply our financial expertise andthe relevant external data to help optimize your finances.All
            without ever requiring you to talk to anyone.
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
