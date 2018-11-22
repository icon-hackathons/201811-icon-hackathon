<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'GroupProfileList',
  components: {
    Breadcrumb,
  },
};
</script>

<template>
<div style="height:100%;">

  <Breadcrumb
    organization="ICONLoop"
    title="평가 대상자 선택하기"
    workspace=" > ICONLoop 1Q 상반기 전사 성과 평가"
    remaintime="남은 시간 3일 17:39:58" />

  <section class="jumbotron mb-0 p-4 border bg-light">
    <div class="row">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <div class="input-group">
          <input type="text" class="form-control" placeholder="Search..." aria-label="Recipient's username" aria-describedby="button-addon2">
          <div class="input-group-append">
            <button class="btn btn-secondary" type="button" id="button-addon2">검색하기</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="container">
    <div class="row mb-4 mt-4">

      <div class="offset-md-1 col-md-10 offset-md-1">

        <div class="row mb-2">
          <div class="col-md text-left">
            <h5>총 7명의 대상자를 찾았습니다</h5>
          </div>
        </div>

        <div class="row">

          <!-- 카드 시작 -->
          <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img class="card-img-top p-5 rounded-circle text-center mx-auto" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:200px;width:200px;">
              <div class="card-body">
                <h5 class="card-title">김태영</h5>
                <h6 class="card-subtitle text-muted small">비즈니스기획팀</h6>
                <div class="row mb-2 mt-3">

                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">132</h6>
                    <h6 class="card-text text-muted small">평가자 수</h6>
                  </div>
                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">70</h6>
                    <h6 class="card-text text-muted small">진행률</h6>
                  </div>
                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">89</h6>
                    <h6 class="card-text text-muted small">평균 점수</h6>
                  </div>

                </div>

                <div>
                  <router-link :to="{name: 'sheet'}" tag="button" class="btn btn-secondary btn btn-block mt-3">평가 시트 작성하기</router-link>
                </div>

              </div>
            </div>
          </div>
          <!-- 카드 끝 -->

        </div>

      </div>

    </div>
  </section>

</div>
</template>
