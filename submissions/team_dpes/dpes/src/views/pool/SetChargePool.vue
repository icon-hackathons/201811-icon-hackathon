<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">차지 풀에 사용료 ICX 예치하기</h2>

        <p class="text-muted mt-1">
          차지 풀에 사용료로 지불할 ICX를 예치하여, 컨트랙트 기간을 설정해주세요.
        </p>

      </div>
    </div>

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">기간</label>
              <input type="text" class="form-control" placeholder="원하시는 평가 기간을 입력해주세요.">
              <small class="form-text text-muted">평가 기간은 일 단위로 계산됩니다.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">인원</label>
              <input type="text" class="form-control" placeholder="40" disabled>
              <small class="form-text text-muted">매핑 된 인원은 자동으로 추가됩니다.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">예치할 차지 풀 크기</label>
              <input type="text" class="form-control" placeholder="1,300" disabled>
              <small class="form-text text-muted">
                예상되는 총 차지 풀의 금액입니다. 차지 풀의 금액은 (총 인원 * 10 ICX + 기간 * 100 ICX)로 산출됩니다.</small>
            </div>

            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">차지 풀 컨트랙트 생성</label>
              <div class="input-group mt-1 mb-1">
                <input type="text" class="form-control" placeholder="hx0erbfh477" style="" disabled>
                <div class="input-group-append">
                  <button class="btn btn-outline-secondary" type="button" id="button-addon2">컨트랙트 생성</button>
                </div>
              </div>
              <small class="form-text text-muted">생성한 차지 풀 컨트랙트 주소입니다.</small>
            </div>

            <button class="btn btn-outline-danger mt-4">ICX 전송</button>
            <router-link :to="{name: 'endofprocess'}" tag="button" class="btn btn-dark mt-4">다음으로</router-link>

          </div>
        </div>
      </div>
    </form>

  </section>
</div>
</template>
