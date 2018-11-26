<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue'
import AT from '@/store/action-types';
import DpesScoreAPI from '@/api/DpesScoreAPI';
import { IconAmount, IconConverter } from 'icon-sdk-js';

export default {
  name: 'AuditStarted',
  components: {
    Breadcrumb,
  },
  computed: {
    ...mapState({
      child: state => state.EvaluationLogin.child,
    }),
  },
  watch: {
    child: function(child) {
      if (child.hasOwnProperty('childAddress') && child.hasOwnProperty('childLevel')) {
        this.$router.push('/evaluation/audit');
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
  }
};
</script>


<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">
  <Breadcrumb
    organization=""
    title="승인심사 시작하기"
    workspace=""
    remaintime="" />
  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">승인심사를 위한 비밀 계정 인증하기</h2>
        <p class="text-muted mt-1">
          승인 심사를 위해 비밀 계정을 불러와주세요.
        </p>
      </div>
    </div>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">
          <div class="card border-0 rounded text-left p-5">
              <div class="row">
                <div class="col-md-12 text-center">
                  <p>
                    비밀 계정을 불러와주세요.
                    <br />지갑 열기를 실행해 ICONex에서 계정을 불러옵니다.
                  </p>
                  <div class="text-center">
                     <button @click="childLogIn" tag="button" class="btn btn-block btn-lg btn-dark">계정 가져오기</button>
                  </div>
                  <div class="small text-center mt-3">그룹 리더, 그룹 팀원 관계 없이 자동적으로 내용이 반영됩니다.</div>

                </div>
              </div>

          </div>
        </div>

      </div>

  </section>
</div>
</template>
