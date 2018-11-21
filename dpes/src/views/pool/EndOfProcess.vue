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

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
            <div>
              끝
            </div>

            <router-link :to="{name: 'index'}" tag="button" class="btn btn-secondary mt-4">시작하기</router-link>

          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
