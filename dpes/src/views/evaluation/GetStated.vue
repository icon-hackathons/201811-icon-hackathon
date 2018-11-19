<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'GetStarted',
  components: {
    Breadcrumb,
  },
};
</script>

<template>
<div style="height:100%;">

  <Breadcrumb
    organization=""
    title="평가 시작하기"
    workspace=""
    remaintime="" />

  <section class="container text-body">
    <div class="row mb-5 mt-3">

      <div class="offset-md-1 col-md-10 offset-md-1">

        <div class="row mt-5 pt-5 pb-5 mb-2">
          <div class="offset-md-2 col-md-8 offset-md-2 text-center">
            <h2 class="font-weight-bold">DPES에 오신 것을 환영합니다.
              <br />평가를 시작해주세요!</h2>
            <div class="mt-4 h5 text-muted">
              완전히 탈중앙화된 성과 평가 시스템에서 당신의 동료를 객관적으로 평가해주세요.
              별도의 로그인 없이 블록체인 계정만으로 익명화 된 평가를 수행할 수 있습니다.
            </div>
            <div class="h6 text-muted mt-5 mb-5 text-center">
              <span class="h4 text-body">Step 1.</span>먼저, 당신의 평가용 계정을 인증해주세요.
              <br />지갑 열기를 실행해 ICONex 상에서 계정 주소를 가져옵니다.


              <form class="text-center mt-4">
                <div class="form-group row">
                  <div class="col-md-10 mt-3">
                    <input type="text" class="form-control form-control-lg" placeholder="계정 주소..." disabled>
                  </div>
                  <div class="col-md-1 mt-3">
                    <router-link :to="{name: 'workspacelist'}" tag="button" class="btn btn-lg btn-dark">지갑 열기</router-link>
                  </div>
                </div>
                <div class="small mt-2">
                  주의 - 반드시 알려지지 않은 익명의 평가용 계정을 활용해주세요.
                </div>
              </form>

            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

</div>
</template>
