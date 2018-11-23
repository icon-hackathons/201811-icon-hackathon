<script>
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue';
import AuditCard from '@/views/evaluation/AuditCard.vue';
import AT from '@/store/action-types';
import DpesScoreAPI from '@/api/DpesScoreAPI';

export default {
  name: 'Audit',
  components: {
    Breadcrumb,
    AuditCard,
  },
  computed: {
    ...mapState({
      loading: state => state.Audit.loading,
      reviewResult: state => state.Audit.reviewResult,
      projectAddress: state => state.Workspace.workspace.projectAddress
    }),
    aver1() {
      return (parseInt(this.reviewResult[0][0].score, 16) + parseInt(this.reviewResult[0][1].score, 16)) / 2
    },
    aver2() {
      return (parseInt(this.reviewResult[1][0].score, 16) + parseInt(this.reviewResult[1][1].score, 16)) / 2
    },
  },
  methods: {
    ...mapActions([
      AT.AUDIT.GET_REVIEW_RESULT,
    ]),
    async auditVote() {
        const result = await DpesScoreAPI.auditVote({
            projectAddress: this.projectAddress || 'cx48b7224207fac3a8c2903c2ceefd9c25b1239f76',
            childAddress: 'hx908f59b7ea6bbbc6b2fcfc629d7cacdb22db6432'
        });
        if (result) {
            this.$route.push('/evaluation/auditdone');
        }
    }
  },
  created: function() {
    this[AT.AUDIT.GET_REVIEW_RESULT]({
      projectAddress: this.projectAddress || 'cx48b7224207fac3a8c2903c2ceefd9c25b1239f76'
    });
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
<div v-if="loading"></div>
<div v-else class="pb-5 text-body h-100 bg-white">
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
          <a class="nav-link rounded p-3" data-toggle="pill" href="#v-pills-dy" role="tab">
            <img src="../../assets/img_sample.jpg" class="rounded-circle" style="width:30px; height:30px;" />
            <span class="ml-3">김진현</span>
          </a>
          <a class="nav-link rounded p-3" data-toggle="pill" href="#v-pills-teng" role="tab">
            <img src="../../assets/img_sample.jpg" class="rounded-circle" style="width:30px; height:30px;" />
            <span class="ml-3">하봉안</span>
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
                    name="김진현"
                    address=""
                    :value="aver1"
                  />
                  <AuditCard
                    name="하봉안"
                    address=""
                    :value="aver2"
                  />
                </div>
              </div>

          </div>
          <!-- Overview 탭-->

          <!-- 동적 멤버별 탭 -->
          <div class="tab-pane fade show" id="v-pills-dy" role="tabpanel">

            <div class="row">
              <div class="col-md-12">

                <h6 class="text-left font-weight-bold mb-4 mt-2">김진현님을 평가한 익명 주소
                    <span class="float-right">평균 점수
                    <span class="ml-2">{{ aver1 }}</span>
                  </span>
                </h6>

                <!-- 카드 -->
                <AuditCard
                  name=""
                  :address="reviewResult[0][0].from"
                  :value="parseInt(reviewResult[0][0].score, 16)"
                />
                <AuditCard
                  name=""
                  :address="reviewResult[0][1].from"
                  :value="parseInt(reviewResult[0][1].score, 16)"
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

                <h6 class="text-left font-weight-bold mb-4 mt-2">하봉안님을 평가한 익명 주소
                  <span class="float-right">평균 점수
                    <span class="ml-2">{{ aver2 }}</span>
                  </span>
                </h6>

                <!-- 카드 -->
                <AuditCard
                  name=""
                  :address="reviewResult[1][0].from"
                  :value="parseInt(reviewResult[1][0].score, 16)"
                />
                <AuditCard
                  name=""
                  :address="reviewResult[1][1].from"
                  :value="parseInt(reviewResult[1][1].score, 16)"
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
        <button @click="auditVote" tag="button" class="btn btn-secondary btn btn-block" style="margin-top:150px;margin-bottom:100px;">승인</button>
      </div>
      <div class="col-md-6">
        <router-link :to="{name: 'sheet'}" tag="button" class="btn btn-secondary btn btn-block" style="margin-top:150px;margin-bottom:100px;">거부</router-link>
      </div>
    </div>

  </section>

</div>
</template>
