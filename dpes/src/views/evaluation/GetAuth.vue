<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import Star from '@/views/common/Star.vue';
import Breadcrumb from '@/views/Breadcrumb.vue';
import AT from '@/store/action-types';

export default {
  name: 'GetAuth',
  components: {
    Breadcrumb,
    Star,
  },
  data: function () {
    return {
      childAddress: '',
    };
  },
  computed: {
    ...mapState({
      parent: state => state.EvaluationLogin.parent,
      child: state => state.EvaluationLogin.child,
    }),
  },
  watch: {
    child: function(child) {
      if (child.hasOwnProperty('childAddress') && child.hasOwnProperty('childLevel')) {
        this.$router.push('/evaluation/workspacelist');
      }
    },
  },
  methods: {
    ...mapActions([
      AT.EVALUATION_LOGIN.PARENT_LOG_IN,
      AT.EVALUATION_LOGIN.SIGN_UP,
    ]),
    parentLogIn: function () {
      this[AT.EVALUATION_LOGIN.PARENT_LOG_IN]();
    },
    signUp: function () {
      this[AT.EVALUATION_LOGIN.SIGN_UP]({
        parentAddress: this.parent.parentAddress,
        childAddress: this.childAddress,
        isLeader: '0x0',
      });
    },
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
        <h2 class="font-weight-extra-bold mt-5 pt-3">비밀 계정 인증하기</h2>

        <p class="text-muted mt-1">
          그룹 공용 계정으로, 비밀 계정이 해당 그룹에 속해있음을 인증해주세요.
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
                    먼저, 지갑에 그룹 공용 계정을 불러와주세요.
                    <br />지갑 열기를 실행해 ICONex에서 그룹 공용 계정을 불러옵니다.
                  </p>
                </div>
              </div>

                <div class="row">
                  <div class="col-md-12 text-center mt-1">
                    <button @click="parentLogIn" tag="button" class="btn btn-lg btn-dark">그룹 공용 계정 가져오기</button>
                  </div>
                </div>
                <div class="small text-center mt-3">그룹 공용 계정은 그룹 관리자가 알고 있습니다. 그룹 관리자에게 오프체인 상에서 PK를 받아 연결해주세요.</div>

                <div class="row mt-5">
                  <div class="col-md-1">
                    <span class="h3 font-weight-extra-bold">2. </span>
                  </div>
                  <div class="col-md-10">
                    <p>
                      비밀 계정 주소를 기입해주세요.
                      <br />그룹 공용 계정에서 비밀 계정 주소로 트랜잭션을 전송해 인증합니다.
                    </p>
                  </div>

                </div>

                  <div class="row">
                    <div class="col-md-8 mt-3">
                      <input v-model="childAddress" type="text" class="form-control form-control-lg" placeholder="계정 주소 입력...">
                    </div>
                    <div class="col-md-4 mt-3">
                      <button @click="signUp" tag="button" class="btn btn-lg btn-dark">인증하기</button>
                    </div>
                  </div>
                  <div class="small text-center mt-3">
                    주의 - 반드시 타인에게 알려지지 않은 익명의 평가용 계정을 활용해주셔야 합니다. 회원가입 시 사용했던 주소와 달라야 합니다.
                  </div>

          </div>
        </div>

      </div>

  </section>
</div>
</template>
