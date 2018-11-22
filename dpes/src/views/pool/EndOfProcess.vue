<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">모든 설정이 끝났습니다.</h2>
        <p class="text-muted mt-1">
          조직과 워크스페이스가 생성되었습니다. 그룹 평가를 시작하세요.
        </p>
      </div>
    </div>
    <router-link :to="{name: 'index'}" tag="button" class="btn btn-secondary btn-block" style="margin-top:100px; margin-bottom:250px;">시작하기</router-link>
  </section>
</div>
</template>
