<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'AuditStarted',
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
                    <router-link :to="{name: 'audit'}" tag="button" class="btn btn-block btn-lg btn-dark">계정 가져오기</router-link>
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
