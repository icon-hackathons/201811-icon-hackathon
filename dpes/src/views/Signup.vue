<template>
<div>
  <section style="background-color:gray;height:1300px;">
    <div class="container" style="">
      <div class="row" style="padding-top:60px;text-align:left;">
        <div class="col-md text-white" style="background-color:#00294A !important;padding:60px;border-radius: 10px 0px 0px 10px;">
          <h1>Decentralized Performance Evaluation System</h1>
          <p>DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다.DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다.DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다.DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다.DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다. DPES는 죽입니다. 최고입니다. 세상에서 제일 좋습니다.
          </p>
        </div>
        <div class="col-md" style="background-color:white !important;padding:60px;border-radius: 0px 10px 10px 0px;">

          <form>
            <div class="form-group">
              <p>
                <h6>회원의 유형 선택</h6>
                <div class="btn-group btn-group-toggle" data-toggle="buttons" style="width:100%;">
                  <label class="btn btn-secondary active" style="width:100%;"><input type="radio" name="options" id="option1" autocomplete="off" checked>일반 회원</label>
                  <label class="btn btn-secondary" style="width:100%;"><input type="radio" name="options" id="option3" autocomplete="off">관리자</label>
                </div>
              </p>
            </div>

            <div class="form-group">
              <p>
                <h6>이메일 주소</h6>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
              </p>
            </div>

            <div class="form-group">
              <p>
                <h6>비밀번호</h6>
                <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
              </p>
            </div>

            <p>
              <a class="" href=""><span class="">이미 계정이 있으신가요?</span></a>
            </p>

            <router-link :to="{name: 'create_profile'}" tag="button" class="btn btn-secondary">제출하기</router-link>
          </form>

        </div>
      </div>
    </div>
  </section>
</div>
</template>
