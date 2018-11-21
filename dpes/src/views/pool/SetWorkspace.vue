<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">워크스페이스 생성하기</h2>

        <p class="text-muted mt-1">
          원하시는 워크스페이스를 생성하여, 다양한 목적의 평가를 개설해보세요.
        </p>

      </div>
    </div>

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">워크스페이스명</label>
              <input type="text" class="form-control" placeholder="워크스페이스명을 입력해주세요.">
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">리워드 풀 크기</label>
              <input type="text" class="form-control" placeholder="리워드풀의 크기를 입력해주세요">
              <small class="form-text text-muted">총 인센티브의 규모를 고려하여 리워드 풀의 크기를 결정해주세요.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">인센티브 크기</label>
              <input type="text" class="form-control" placeholder="개별 사용자 인센티브의 크기를 입력해주세요">
              <small class="form-text text-muted">개별 사용자 인센티브의 크기를 입력해주세요.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">등급 기준</label>
              <input type="text" class="form-control" placeholder="리워드풀의 크기를 입력해주세요">
              <small class="form-text text-muted">인센티브 등급의 기준을 설정해주세요.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">소속 그룹 선택</label>
              <div>
                해당 워크스페이스에 소속될 그룹을 선택해주세요.
              </div>
              <small class="form-text text-muted"></small>
            </div>

            <router-link :to="{name: 'SetRewardPool'}" tag="button" class="btn btn-secondary mt-4">다음으로</router-link>

          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
