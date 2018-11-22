<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">리워드 풀에 인센티브용 ICX 예치하기</h2>

        <p class="text-muted mt-1">
          리워드 풀에 인센티브용 ICX를 예치하여, 조직원들에게 인센티브를 분배하세요.
        </p>

      </div>
    </div>

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">예치할 리워드 풀 크기</label>
              <input type="text" class="form-control" placeholder="리워드풀의 크기를 입력해주세요">
              <small class="form-text text-muted">총 인센티브의 규모를 고려하여 예치할 리워드 풀의 ICX 양을 결정해주세요.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">사용자당 인센티브 크기</label>
              <input type="text" class="form-control" placeholder="개별 사용자 인센티브의 크기를 입력해주세요">
              <small class="form-text text-muted">개별 사용자가 받을 수 있는 인센티브의 양을 결정해주세요</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">리워드 풀 컨트랙트 생성</label>
              <div class="input-group mt-1 mb-1">
                <input type="text" class="form-control" placeholder="hx0erbfh477" style="" disabled>
                <div class="input-group-append">
                  <button class="btn btn-outline-secondary" type="button" id="button-addon2">컨트랙트 생성</button>
                </div>
              </div>
              <small class="form-text text-muted">생성한 리워드 풀 컨트랙트 주소입니다.</small>
            </div>

            <button class="btn btn-outline-danger mt-4">ICX 전송</button>
            <router-link :to="{name: 'setchargepool'}" tag="button" class="btn btn-dark mt-4">다음으로</router-link>

          </div>
        </div>
      </div>
    </form>

  </section>
</div>
</template>
