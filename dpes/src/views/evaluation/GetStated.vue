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
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <Breadcrumb
    organization=""
    title="평가 시작하기"
    workspace=""
    remaintime="" />

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">DPES에 오신 것을 환영합니다. 평가를 시작해주세요.</h2>

        <p class="text-muted mt-1">
          완전히 탈중앙화된 성과 평가 시스템에서 당신의 동료를 객관적으로 평가해주세요.
          별도의 로그인 없이 블록체인 계정만으로 익명화 된 평가를 수행할 수 있습니다.
        </p>

      </div>
    </div>


      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">

              <div class="row">
                <div class="col-md-6 mt-3">
                  <router-link :to="{name: 'getauth'}" tag="button" class="btn btn-block btn-lg btn-outline-dark" style="height:150px;">비밀 계정 인증하기</router-link>
                </div>
                <div class="col-md-6 mt-3">
                  <router-link :to="{name: 'getwallet'}" tag="button" class="btn btn-block btn-lg btn-dark" style="height:150px;">비밀 평가 시작하기</router-link>
                </div>
              </div>
              <div class="small text-center mt-3">
                아직 비밀 계정을 인증하지 않으셨다면 인증해주세요.
              </div>

          </div>
        </div>
      </div>

  </section>
</div>
</template>
