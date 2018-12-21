<script>
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/profile/ProfileHeader.vue'
import ProfileProject from '@/views/profile/ProfileProject.vue'
import ProfileSelfEval from '@/views/profile/ProfileSelfEval.vue'
import Star from '@/views/common/Star.vue'
import AT from '@/store/action-types';

export default {
  name: 'Sheet',
  components: {
    Breadcrumb,
    ProfileHeader,
    ProfileProject,
    ProfileSelfEval,
    Star,
  },
  data: function () {
    return {
      dueDate: 0,
      timer: '',
      review: {}
    }
  },
  created: function() {
    this.dueDate = this.workspace.dueDate;
    this.startTimer();
    this.timer = setInterval(this.startTimer, 1000);
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer);
  },
  methods: {
    ...mapActions([
      AT.EVALUATION.VOTE,
    ]),
    startTimer: function () {
      this.dueDate = this.dueDate - 1000000;
    },
    onClickedStar: function (e) {
      this.review = Object.assign({}, this.review, {
        [e.name]: Number(e.value),
      });
      console.log(this.review)
    },
    vote: function () {
      const formattedJson = this.formatReview();
      this[AT.EVALUATION.VOTE]({
        userAddress: this.profile.walletAddress || 'hx1234123412341234123412341234123412341234',
        childAddress: this.childAddress || 'hx0fc2c4a745db84455de35d4a102ce7b8b8ee9cbb',
        projectAddress: this.workspace.projectAddress || '',
        formattedJson,
      });
    },
    formatReview: function () {
      const keyArr = Object.keys(this.review).sort();
      const result = keyArr.map((key) => {
        const type = (this.review[key] === 'Y' || this.review[key] === 'N') ? 'bool' : 'int'
        const value = type === 'bool' ? (this.review[key] === 'Y' ? 1 : 0) : this.review[key]
        return {
          type: type,
          value: '0x' + value
        }
      })
      console.log(JSON.stringify(result))
      const escaped = JSON.stringify(result)
      console.log(escaped)
      return escaped
    },
    handleRadio: function (v) {
      console.log(v)
      this.review = Object.assign({}, this.review, {
        '4_3': v
      });
    }
  },
  computed: {
    ...mapState({
      workspace: state => state.Workspace.workspace,
      profile: state => state.Profile.profile,
      childAddress: state => state.EvaluationLogin.child.childAddress,

    }),
    convertedDistance: function () {
      const days = Math.floor(this.dueDate / (1000000 * 60 * 60 * 24));
      const hours = Math.floor((this.dueDate % (1000000 * 60 * 60 * 24)) / (1000000 * 60 * 60));
      const hoursStr = hours >= 10 ? hours : '0' + hours;
      const minutes = Math.floor((this.dueDate % (1000000 * 60 * 60)) / (1000000 * 60));
      const minutesStr = minutes >= 10 ? minutes : '0' + minutes;
      const seconds = Math.floor((this.dueDate % (1000000 * 60)) / 1000000);
      const secondsStr = seconds >= 10 ? seconds : '0' + seconds;
      return `${days}일 ${hoursStr}:${minutesStr}:${secondsStr}`;
    }
  },
};
</script>

<template>
<!-- eslint-disable max-len -->
<div class="mb-5 pb-5 text-body" style="height:100%;">
  <Breadcrumb
    organization="ICONLoop"
    title="평가 시트 작성하기"
    :workspace="` > ${workspace.projectName}`"
    group=" > 비즈니스기획팀"
    :remaintime="`남은 시간 ${convertedDistance}`" />
  <ProfileHeader />
  <section class="container">
    <div class="row mb-4 mt-4">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active text-body" id="pills-eval-tab" data-toggle="pill" href="#pills-eval" role="tab" aria-controls="pills-eval" aria-selected="true">
              {{profile.name}} 님 평가하기
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-body" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab" aria-controls="pills-home" aria-selected="true">자가 평가</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-body" id="pills-contact-tab" data-toggle="pill" href="#pills-contact" role="tab" aria-controls="pills-contact" aria-selected="false">최근 참가 프로젝트</a>
          </li>
        </ul>
        <form>
          <div class="tab-content" id="pills-tabContent">
            <div class="tab-pane fade show active text-left" id="pills-eval" role="tabpanel" aria-labelledby="pills-eval-tab">
              <div class="row mt-0">
                <div class="col-md-12">
                  <div class="card border-0 rounded text-left">
                    <div class="mt-0">
                      <div class="h5 mt-3 font-weight-bold">
                        1. 평가대상자의 팀 내 기여도는?
                      </div>
                      <hr />
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">1.1.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 본인의 역할에 걸맞는 역량을 발휘했나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'1_1'" :value="review['1_1']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">1.2.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자가 맡은 역할이 팀의 성공에 얼만큼 기여했나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'1_2'" :value="review['1_2']" ></Star>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="mt-5">
                      <div class="h5 mt-3 font-weight-bold">
                        2. 평가대상자의 업무 역량은?
                      </div>
                      <hr />
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">2.1.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 평소 업무의 질은 어땠나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'2_1'" :value="review['2_1']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">2.2.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 평소 일정 준수 정도는 어땠나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'2_2'" :value="review['2_2']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">2.3.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 협업 및 커뮤니케이션 능력은 어땠나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'2_3'" :value="review['2_3']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">2.4.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 배울 점이 많은 사람인가요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'2_4'" :value="review['2_4']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">2.5.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 자기만의 강점 영역이 분명히 있나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'2_5'" :value="review['2_5']" ></Star>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="mt-5">
                      <div class="h5 mt-3 font-weight-bold">
                        3. 평가대상자의 업무 태도는?
                      </div>
                      <hr />
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.1.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 얼마나 주도적 혹은 적극적으로 일하였나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'3_1'" :value="review['3_1']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.2.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 얼마나 책임감을 가지고 일하였나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'3_2'" :value="review['3_2']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.3.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 팀원에게 얼마나 협조적이었나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'3_3'" :value="review['3_3']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.4.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 도덕성/윤리의식은 어떠했나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'3_4'" :value="review['3_4']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.5.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 근태는 어떠했나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'3_5'" :value="review['3_5']" ></Star>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="mt-5">
                      <div class="h5 mt-3 font-weight-bold">
                        4. 평가대상자에 대한 향후 기대는?
                      </div>
                      <hr />
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">4.1.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 역량 및 태도가 다른 프로젝트에서도 발휘/기여될 수 있을 것이라고 보나요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'4_1'" :value="review['4_1']"></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">4.2.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자의 향후 회사의 성장에 핵심적인 역할을 할 인물인가요?</label>
                            <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'4_2'" :value="review['4_2']" ></Star>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">4.3.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">앞으로도 같이 일하고 싶나요?</label>
                            <!-- <Star :style="{ position: 'absolute', right: '8px'}" @clicked="onClickedStar" :name="'4_3'" :value="review['4_3']" ></Star> -->
                            <div data-toggle="buttons" class="mt-3 float-right btn-group btn-group-toggle" style="width: 21%;">
                              <label @click="handleRadio('Y')" class="btn btn-secondary active" style="width: 100%;">
                                <input data-value="Y" type="radio" name="options" id="option1" autocomplete="off" checked="checked">네
                              </label>
                              <label @click="handleRadio('N')" class="btn btn-secondary" style="width: 100%;">
                                <input data-value="N" type="radio" name="options" id="option3" autocomplete="off">아니오
                              </label>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">4.4.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">대상자에게 도움이 되는 피드백을 전달해주세요.</label>
                            <div class="form-group">

  <textarea class="form-control" id="exampleFormControlTextarea1" rows="5" placeholder="대상자의 성장에 도움을 주세요!"></textarea>
</div>


                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade show text-left" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
              <ProfileSelfEval :profile="profile" />
            </div>
            <div class="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">
              <ProfileProject />
            </div>
          </div>
          <div class="row mt-5 mt-5 pb-5">
            <div class="col-md-12">
              <button @click.prevent="vote" type="submit" class="btn btn-dark btn-lg btn-block">제출하기</button>
              <router-link :to="{name: 'auditstarted'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">Audit(개발용)</router-link>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</div>
</template>
