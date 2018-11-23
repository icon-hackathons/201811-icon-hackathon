<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue';
import AT from '@/store/action-types';

export default {
  name: 'GetWallet',
  components: {
    Breadcrumb,
  },
  data: function () {
    return {
      childAddress: '',
      switchButton: false,
    };
  },
  computed: {
    ...mapState({
      child: state => state.EvaluationLogin.child,
    }),
  },
  watch: {
    child: function(child) {
      if (child.hasOwnProperty('childAddress') && child.hasOwnProperty('childLevel')) {
        this.switchButton = true;
      }
    },
  },
  methods: {
    ...mapActions([
      AT.EVALUATION_LOGIN.CHILD_LOG_IN,
    ]),
    childLogIn: function () {
      this[AT.EVALUATION_LOGIN.CHILD_LOG_IN]();
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
        <h2 class="font-weight-extra-bold mt-5 pt-3">비밀 계정 불러오기</h2>
        <p class="text-muted mt-1">
          온전히 블록체인 상에서 계정 주소에 기반하여 평가를 수행합니다. 그 누구도 알지 못 하는 비밀 계정을 불러와주세요.
          회원가입 때 사용하셨던 공개된 지갑 주소로 평가를 수행해서는 안됩니다.
        </p>
      </div>
    </div>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">
          <div class="card border-0 rounded text-left p-5">
            <p>
              먼저, 인증된 비밀 계정을 불러와주세요.<br />
              지갑 열기를 실행해 ICONex에서 계정 주소를 가져옵니다.<br />
              아직 비밀 계정 인증을 마치지 못 하셨다면, <router-link class="text-info" :to="{name: 'getauth'}">여기</router-link>를 클릭하세요.
            </p>
              <div class="row">
                <div class="col-md-8 mt-3">
                  <input :value="child.childAddress" type="text" class="form-control form-control-lg" placeholder="계정 주소..." disabled>
                </div>
                <div v-if="!switchButton" class="col-md-4 mt-3">
                  <button @click="childLogIn" tag="button" class="btn btn-lg btn-dark btn-block">지갑주소 가져오기</button>
                </div>
                <div v-else class="col-md-4 mt-3">
                  <router-link :to="{name: 'workspacelist'}" tag="button" class="btn btn-lg btn-dark btn-block">평가하기</router-link>
                </div>
              </div>
              <div class="small text-center mt-3">
                주의 - 반드시 타인에게 알려지지 않은 익명의 비밀 계정을 활용해주셔야 합니다. 회원가입 시 사용했던 주소와 달라야 합니다.
              </div>
          </div>
        </div>
      </div>

  </section>
</div>
</template>
