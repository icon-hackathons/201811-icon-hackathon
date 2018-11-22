<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">공개 회원으로 가입</h2>

        <p class="text-muted mt-1">
          자신의 부서와 지갑 주소, 현재 프로젝트를 간단하게 기입해주세요. 그리고 자기 스스로에 대한 진솔한 평가를 담아, 동료들이 나를 평가할 때 참고할 수 있는 자료를 제공하세요!
        </p>

      </div>
    </div>

    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
            <label class="font-weight-bold mb-0" for="">회원 유형</label>
            <div class="mt-3 btn-group btn-group-toggle" data-toggle="buttons" style="width:100%;">
              <label class="btn btn-secondary active" style="width:100%;"><input type="radio" name="options" id="option1" autocomplete="off" checked>일반 회원</label>
              <label class="btn btn-secondary" style="width:100%;"><input type="radio" name="options" id="option3" autocomplete="off">관리자</label>
            </div>
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">이메일</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
              <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>

            <div class="form-group mt-2">
              <label class="font-weight-bold" for="">비밀번호</label>
              <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>

            <router-link :to="{name: 'create_profile'}" tag="button" class="btn btn-secondary mt-4">가입하기</router-link>

          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
