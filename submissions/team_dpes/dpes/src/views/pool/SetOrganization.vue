<script>
export default {
  name: 'SetOrganization',
  data: function () {
    return {
      company: 'ICONLOOP',
      adminAddress: 'hxa4c3a78d73bb7287f72801c09298f1a5743b1655'
    }
  }
};
</script>


<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">
  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">조직 생성하기</h2>
        <p class="text-muted mt-1">
          원하시는 조직을 생성하여, 우리 조직의 평가를 시작해보세요!
        </p>
      </div>
    </div>
    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">
          <div class="card border-0 rounded text-left p-5">
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">조직명</label>
              <input v-model="company" type="text" class="form-control" placeholder="조직명을 입력해주세요.">
            </div>
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">조직 관리자의 계정 주소</label>
              <input v-model="adminAddress" type="text" class="form-control" placeholder="조직을 관리하는 계정 주소를 입력해주세요.">
              <small class="form-text text-muted">조직 관리를 수행할 관리자의 계정 주소를 입력해주세요.</small>
            </div>
            <router-link :to="{name: 'setworkspace'}" tag="button" class="btn btn-secondary mt-4">다음으로</router-link>
          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
