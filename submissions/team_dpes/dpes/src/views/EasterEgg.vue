<template>
<div>

  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="mt-3">
          <div class="display-3 mt-5 mb-5">
            당신은 갓종협의 Loop에 빠졌습니다.
          </div>
          <img src="../assets/t-jh.jpg" class="rounded-circle" />
          <div class="mt-5 mb-5 pb-5">
            <div class="row">
              <div class="col-md-6">
                <router-link :to="{name: ''}" tag="button" class="p-3 btn btn-dark btn-block btn-lg">예</router-link>
              </div>
              <div class="col-md-6">
                <router-link :to="{name: ''}" tag="button" class="p-3 btn btn-dark btn-block btn-lg">아니요!</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
