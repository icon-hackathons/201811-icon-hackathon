<script>
import { mapState, mapActions } from 'vuex';
import Star from '@/views/common/Star.vue';
import AT from '@/store/action-types';

export default {
  name: 'ProfileSelfEval',
  components: {
    Star,
  },
  props: [
    'profile'
  ]
};
</script>

<template>
  <!-- eslint-disable -->
  <div class="text-left">
    <div class="row">
      <div class="col-md-12">
        <div class="h5 mt-3 font-weight-bold">
          1. 무엇을 했나요?
        </div>
        <hr />
      </div>
      <div class="profile-card card-columns" style="column-count: 2;">
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2 mx-auto">
              <span class="font-weight-bold h6 text-muted">1.1.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">자신이 참여했던 프로젝트와 프로젝트 내 역할을 말씀해주세요.</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['1_1'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">1.2.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">기간 내 가장 몰입하여 최선을 다했던 프로젝트/업무는?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['1_2'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">1.3.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">자신이 참여했던 프로젝트에서 가장 자랑스러운 성과는 무엇이었나요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['1_3'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">1.4.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">왜/어떻게 그러한 성과할 수 있었다고 생각하시나요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['1_4'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">1.5.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">해당 프로젝트에서 자신의 기여도를 평가해주세요.</label>
              <Star :readonly="true" :name="'1_5'" :value="profile['selfReview']['1_5']"></Star>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-md-12">
        <div class="h5 mt-3 font-weight-bold">
          2. 무엇을 알았나요?
        </div>
        <hr />
      </div>
      <div class="profile-card card-columns" style="column-count: 2;">
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">2.1.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">본인이 했던 프로젝트/업무를 통해 어떤 업무 기술/지식을 얻었나요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['2_1'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">2.2.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">본인이 했던 프로젝트를 통해 업무 지식 외 무엇을 배울 수 있었나요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['2_2'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">2.3.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">자신 또는 프로젝트에서 아쉽거나 부족했던 점은 무엇인가요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['2_3'] }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-md-12">
        <div class="h5 mt-3 font-weight-bold">
          3. 향후 나의 성장 계획은?
        </div>
        <hr />
      </div>
      <div class="profile-card card-columns" style="column-count: 2;">
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">3.1.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">본인이 배운 업무 기술 및 경험을 통해, 향후 회사에 어떻게 기여할 수 있다고 생각하나요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['3_1'] }}
              </p>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted">3.2.</span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">다음 평가 기간까지 업무와 관련하여 숙달하고 싶은 분야는 무엇인가요?</label>
              <p style="font-size:13px;">
                {{ profile['selfReview']['3_2'] }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-md-12">
        <div class="h5 mt-3 font-weight-bold">
          4. 종합하기
        </div>
        <hr />
      </div>
      <div class="profile-card card-columns" style="column-count: 2;">
        <div class="card" style="">
          <div class="row">
            <div class="col-lg-2">
              <span class="font-weight-bold h6 text-muted"></span>
            </div>
            <div class="col-lg-10">
              <label class="font-weight-bold" for="">당신은 지난 평가 기간동안 자기 스스로에게 몇 점을 줄 수 있습니까?</label>
            </div>
          </div>
        </div>
        <div class="card" style="">
          <Star :readonly="true" :name="'4_1'" :value="profile['selfReview']['4_1']"></Star>
        </div>
      </div>
    </div>
  </div>
</template>
