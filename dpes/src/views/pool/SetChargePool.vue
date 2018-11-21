<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">차지 풀에 사용료 예치하기</h2>

        <p class="text-muted mt-1">
          차지 풀에 사용료를 예치하여, 금액에 따라 기간을 조정해보세요.
        </p>

      </div>
    </div>

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
            <div>
              차지 양
            </div>

            <router-link :to="{name: 'endofprocess'}" tag="button" class="btn btn-secondary mt-4">다음으로</router-link>

          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
