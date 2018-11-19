<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'GetAuth',
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
        <h2 class="font-weight-extra-bold mt-5 pt-3">평가용 계정 인증하기</h2>

        <p class="text-muted mt-1">
          그룹 공용 계정에 접근하여, 평가용 계정을 인증해주세요.
        </p>

      </div>
    </div>


      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
            <div class="row">
              <div class="col-md-1">
                <span class="h3 font-weight-extra-bold">1. </span>
              </div>
              <div class="col-md-10">
                <p>
                  먼저, 평가용 계정을 불러와주세요.
                  <br />평가용 계정은 회원가입 시 사용했던 공개용 계정과 다른 익명의 계정이여야 합니다.
                  <br />지갑 열기를 실행해 ICONex에서 계정 주소를 가져옵니다.
                </p>
              </div>

            </div>

              <div class="row">
                <div class="col-md-8 mt-3">
                  <input type="text" class="form-control form-control-lg" placeholder="계정 주소..." disabled>
                </div>
                <div class="col-md-4 mt-3">
                  <router-link :to="{name: 'workspacelist'}" tag="button" class="btn btn-lg btn-dark">지갑주소 가져오기</router-link>
                </div>
              </div>
              <div class="small text-center mt-3">
                주의 - 반드시 타인에게 알려지지 않은 익명의 평가용 계정을 활용해주셔야 합니다. 회원가입 시 사용했던 주소와 달라야 합니다.
              </div>


              <div class="row mt-5">
                <div class="col-md-1">
                  <span class="h3 font-weight-extra-bold">2. </span>
                </div>
                <div class="col-md-10">
                  <p>
                    먼저, 평가용 계정을 불러와주세요.
                    <br />평가용 계정은 회원가입 시 사용했던 공개용 계정과 다른 익명의 계정이여야 합니다.
                    <br />지갑 열기를 실행해 ICONex에서 계정 주소를 가져옵니다.
                  </p>
                </div>

              </div>

                <div class="row">
                  <div class="col-md-8 mt-3">
                    <input type="text" class="form-control form-control-lg" placeholder="계정 주소..." disabled>
                  </div>
                  <div class="col-md-4 mt-3">
                    <router-link :to="{name: 'workspacelist'}" tag="button" class="btn btn-lg btn-dark">그룹 공용 계정 가져오기</router-link>
                  </div>
                </div>
                <div class="small text-center mt-3">
                  그룹 공용 계정 어쩌고 저쩌고
                </div>

          </div>
        </div>



      </div>

  </section>
</div>
</template>
