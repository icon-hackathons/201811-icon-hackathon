<script>
import Breadcrumb from '@/views/Breadcrumb.vue';
import AuditCard from '@/views/evaluation/AuditCard.vue';

export default {
  name: 'Audit',
  components: {
    Breadcrumb,
    AuditCard,
  },
};
</script>

<style>
.nav-link{
  border-bottom:none !important;
}
.flex-column.nav-pills a.nav-link{
  color:black !important;
}
.flex-column.nav-pills .nav-link.active{
  background-color:black !important;
  color:white !important;
}
</style>

<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-white">

  <Breadcrumb
    organization=""
    title="승인심사"
    workspace=""
    remaintime="" />

  <section class="container">

    <div class="row mt-4">
      <div class="col-sm-3 mt-2">
        <div class="nav flex-column nav-pills text-left" id="v-pills-tab" role="tablist" aria-orientation="vertical">
          <a class="nav-link active rounded p-3" data-toggle="pill" href="#v-pills-overview" role="tab">
            <span class="ml-3">전체 보기</span>
          </a>
          <a class="nav-link rounded p-3" data-toggle="pill" href="#v-pills-teng" role="tab">
            <img src="../../assets/img_sample.jpg" class="rounded-circle" style="width:30px; height:30px;" />
            <span class="ml-3">김태영</span>
          </a>
          <a class="nav-link rounded p-3" data-toggle="pill" href="#v-pills-dy" role="tab">
            <img src="../../assets/img_sample.jpg" class="rounded-circle" style="width:30px; height:30px;" />
            <span class="ml-3">동적인 녀석들</span>
          </a>

        </div>
      </div>
      <div class="col-sm-9">
        <div class="tab-content" id="v-pills-tabContent">

          <!-- Overview 탭-->
          <div class="tab-pane fade show active" id="v-pills-overview" role="tabpanel">

              <div class="row">
                <div class="col-md-12">

                  <AuditCard
                    name="김태영"
                    address=""
                    value="50"
                  />

                </div>
              </div>

          </div>
          <!-- Overview 탭-->

          <!-- 동적 멤버별 탭 -->
          <div class="tab-pane fade show" id="v-pills-dy" role="tabpanel">

            <div class="row">
              <div class="col-md-12">

                <h6 class="text-left font-weight-bold mb-4 mt-2">XXX님을 평가한 익명 주소</h6>

                <!-- 카드 -->
                <AuditCard
                  name=""
                  address="hx994988888328"
                  value="20"
                />
                <!-- 카드 -->

              </div>
            </div>

          </div>
          <!-- 동적 멤버별 탭 -->

          <!-- 동적 멤버별 탭 -->
          <div class="tab-pane fade show" id="v-pills-teng" role="tabpanel">

            <div class="row">
              <div class="col-md-12">

                <h6 class="text-left font-weight-bold mb-4 mt-2">XXX님을 평가한 익명 주소
                  <span class="float-right">평균 점수
                    <span class="ml-2">40</span>
                  </span>
                </h6>

                <!-- 카드 -->
                <AuditCard
                  name=""
                  address="hx958277f23rh2rbhb"
                  value="20"
                />
                <!-- 카드 -->

              </div>
            </div>

          </div>
          <!-- 동적 멤버별 탭 -->

        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <router-link :to="{name: 'auditdone'}" tag="button" class="btn btn-secondary btn btn-block" style="margin-top:150px;margin-bottom:100px;">승인</router-link>
      </div>
      <div class="col-md-6">
        <router-link :to="{name: 'sheet'}" tag="button" class="btn btn-secondary btn btn-block" style="margin-top:150px;margin-bottom:100px;">거부</router-link>
      </div>
    </div>

  </section>

</div>
</template>
