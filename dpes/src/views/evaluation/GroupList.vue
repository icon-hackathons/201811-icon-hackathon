<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'GroupList',
  components: {
    Breadcrumb,
  },
};
</script>

<template>
<div style="height:100%;">

  <Breadcrumb
    organization="ICONLoop"
    title="그룹 선택하기"
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
            <h5>총 10개의 그룹을 찾았습니다</h5>
          </div>
        </div>

        <div class="row">

          <!-- 카드 시작 -->
          <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
              <div class="card-body">
                <h5 class="card-title">비즈니스기획팀</h5>

                <p class="card-text">
                  <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
                  <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                  <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                  <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                  <span class="ml-2 text-muted small">+3</span>
                </p>

                <div class="row mb-2">

                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">7명</h6>
                    <h6 class="card-text text-muted small">멤버</h6>
                  </div>
                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">70%</h6>
                    <h6 class="card-text text-muted small">평가 진행</h6>
                  </div>
                  <div class="col-md-4">
                    <h6 class="card-text font-weight-bold">7명</h6>
                    <h6 class="card-text text-muted small">멤버</h6>
                  </div>

                </div>

                <div>
                  <router-link :to="{name: 'groupprofilelist'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">멤버 조회</router-link>
                </div>

              </div>
            </div>
          </div>
          <!-- 카드 끝 -->

        </div>

        <div class="row" style="margin-top:30px;">


        </div>

        <div class="row" style="margin-top:30px;">


        </div>


      </div>

    </div>
  </section>



</div>
</template>
