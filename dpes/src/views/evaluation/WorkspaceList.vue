<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'WorkspaceList',
  components: {
    Breadcrumb,
  },
};
</script>

<template>
<div style="height:100%;">

  <Breadcrumb
    organization="ICONLoop"
    title="워크스페이스 선택하기"
    workspace=""
    remaintime="" />

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
            <h5>총 5개의 연결된 워크스페이스를 찾았습니다</h5>
          </div>
        </div>

        <div class="row">

          <!-- 카드 시작 -->
          <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
              <div class="card-body">
                <h5 class="card-title">아이콘루프 1Q 전사 성과 평가</h5>

                <div class="row mb-2">

                  <div class="col-md-12 mt-2">
                    <h6 class="card-text font-weight-bold">6,000,000 ICX</h6>
                    <h6 class="card-text text-muted small">총 리워드 풀 예치금</h6>
                  </div>
                  <div class="col-md-12 mt-3">
                    <h6 class="card-text font-weight-bold">3일 17:39:58</h6>
                    <h6 class="card-text text-muted small">남은 시간</h6>
                  </div>
                  <div class="col-md-12 mt-3">
                    <h6 class="card-text font-weight-bold">145명</h6>
                    <h6 class="card-text text-muted small">평가 대상자</h6>
                  </div>

                </div>

                <div>
                  <router-link :to="{name: 'grouplist'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">부서 조회</router-link>
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
