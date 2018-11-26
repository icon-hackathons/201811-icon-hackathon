<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">
  <Breadcrumb organization="" title="프로필 생성하기" workspace="" group="" remaintime="" />
  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">프로필을 작성하고 자가 평가하기</h2>
        <p class="text-muted mt-1">
          자신의 부서와 지갑 주소, 현재 프로젝트를 간단하게 기입해주세요. 그리고 자기 스스로에 대한 진솔한 평가를 담아, 동료들이 나를 평가할 때 참고할 수 있는 자료를 제공하세요!
        </p>
      </div>
    </div>
    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8">
          <div class="card border-0 rounded text-left p-5">
            <h3 class="font-weight-extra-bold">기본 정보</h3>
            <p class="text-muted small mt-2">
              이 항목은 어쩌고 저쩌고 입니다.이 항목은 어쩌고 저쩌고 입니다.이 항목은 어쩌고 저쩌고 입니다.
            </p>
            <hr />
            <div class="form-group mt-2">
              <label class="font-weight-bold mb-0" for="">프로필 사진</label>
              <small id="" class="form-text text-muted">We'll never share your email with anyone else.</small>
              <div class="text-center">
                <div class="filebox">
                  <label v-if="img" for="ex_file" class="rounded-circle mt-3" :style="{ padding: '0px' }">
                    <img :src="getImgUrl(img)" :style="{ width: '150px', height: '150px' }" />
                  </label>
                  <label v-else for="ex_file" class="rounded-circle mt-3">150x150</label>
                  <input @change="uploadFile($event)" type="file" id="ex_file" name="ex_file" accept=".jpg, .jpeg, .png">
                </div>
              </div>
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold" for="">이름</label>
              <div class="form-row">
                <div class="col">
                  <input v-model="firstName" type="text" class="form-control" placeholder="First name">
                </div>
                <div class="col">
                  <input v-model="lastName" type="text" class="form-control" placeholder="Last name">
                </div>
              </div>
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold mb-0" for="">공개 지갑 주소</label>
              <small id="" class="form-text text-muted mb-3">We'll never share your email with anyone else.</small>
              <input v-model="walletAddress" type="text" class="form-control" id="" placeholder="공개할 지갑 주소 입력...">
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold mb-0" for="">소속 회사</label>
              <small id="" class="form-text text-muted mb-3">We'll never share your email with anyone else.</small>
              <input v-model="company" type="text" class="form-control" id="" placeholder="소속 회사 코드 입력...">
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold mb-0" for="">소속 부서</label>
              <small id="" class="form-text text-muted mb-3">We'll never share your email with anyone else.</small>
              <input v-model="team" type="text" class="form-control" id="" placeholder="소속 부서 코드 입력...">
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold mb-0" for="">직무와 직급</label>
              <small id="" class="form-text text-muted mb-3">We'll never share your email with anyone else.</small>
              <input v-model="position" type="text" class="form-control" id="" placeholder="직무 혹은 직급 입력...">
            </div>
            <div class="form-group mt-3">
              <label class="font-weight-bold mb-0" for="">간략한 자기소개</label>
              <small id="" class="form-text text-muted mb-3">자기 자신에 대해서 간략하게 소개해주세요</small>
              <textarea v-model="introduction" class="form-control" id="" rows="5" placeholder="3줄 이내의 간략한 자기 소개 입력...">
              </textarea>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8">
          <div class="card border-0 rounded text-left p-5">
            <h3 class="font-weight-extra-bold">자기 평가</h3>
            <p class="text-muted small mt-2">
              이 항목은 어쩌고 저쩌고 입니다.이 항목은 어쩌고 저쩌고 입니다.이 항목은 어쩌고 저쩌고 입니다.
            </p>
            <div class="mt-4">
              <div class="h5 mt-3 font-weight-bold">
                1. 무엇을 했나요?
              </div>
              <hr />
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">1.1.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">자신이 참여했던 프로젝트와 프로젝트 내 역할을 말씀해주세요.</label>
                    <textarea v-model="selfReview['1_1']" class="form-control" id="" rows="4" placeholder="예시 - 프로젝트 명, 프로젝트 목표, 맡은 역할 또는 업무 등"></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">1.2.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">기간 내 가장 몰입하여 최선을 다했던 프로젝트/업무는?</label>
                    <textarea v-model="selfReview['1_2']" class="form-control" id="" rows="4" placeholder="예시 - 프로젝트 명, 프로젝트 목표, 맡은 역할 또는 업무 등"></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">1.3.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">자신이 참여했던 프로젝트에서 가장 자랑스러운 성과는 무엇이었나요?</label>
                    <textarea v-model="selfReview['1_3']" class="form-control" id="" rows="4" placeholder="예시 - OOO의 마케팅 채널 활성화를 위해 3개월 간 채널 전략을 수립 및 집행했고, 신규 방문자 유입을 320%(1,100->3,232) 증가시켰습니다."></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">1.4.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">왜/어떻게 그러한 성과할 수 있었다고 생각하시나요?</label>
                    <textarea v-model="selfReview['1_4']" class="form-control" id="" rows="4" placeholder="예시 - 마케팅 트렌드 분석을 통해, OOO 전략을 도출하여, XXX를 수행했기 때문입니다."></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row pt-3">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">1.5.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">해당 프로젝트에서 자신의 기여도를 평가해주세요.</label>
                    <Star @clicked="onClicked_1_5" :name="'star_1_5'" :value="selfReview['1-5']" :style="{ position: 'absolute', top: '-7px', right: '3px'}"></Star>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-5">
              <div class="h5 mt-3 font-weight-bold">
                2. 무엇을 알았나요?
              </div>
              <hr />
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">2.1.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">본인이 했던 프로젝트/업무를 통해 어떤 업무 기술/지식을 얻었나요?</label>
                    <textarea v-model="selfReview['2_1']" class="form-control" id="" rows="4" placeholder="예시 - 콘텐츠 마케팅 KPI 설계 및 트래킹을 하며 Adobe Analytics 활용 역량을 향상시킬 수 있었습니다."></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">2.2.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">본인이 했던 프로젝트를 통해 업무 지식 외 무엇을 배울 수 있었나요?</label>
                    <textarea v-model="selfReview['2_2']" class="form-control" id="" rows="4" placeholder="예시 - 콘텐츠 마케팅을 수행하며 광고대행사와 협업하며 프로젝트 관리 능력도 향상시킬 수 있었습니다."></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">2.3.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">자신 또는 프로젝트에서 아쉽거나 부족했던 점은 무엇인가요?</label>
                    <textarea v-model="selfReview['2_3']" class="form-control" id="" rows="4" placeholder="예시 - 인원 리소스가  충분했었다면, A/B 테스트를 더 적극적으로 하여 최적의 콘텐츠 방식을 찾는데 더 수월했을 것입니다."></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-5">
              <div class="h5 mt-3 font-weight-bold">
                3. 향후 나의 성장 계획은?
              </div>
              <hr />
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">3.1.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">본인이 배운 업무 기술 및 경험을 통해, 향후 회사에 어떻게 기여할 수 있다고 생각하나요?</label>
                    <textarea v-model="selfReview['3_1']" class="form-control" id="" rows="4" placeholder="예시 - 제가 배운 KPI 설계 경험으로, 향후 프로젝트의 지표 선정 및 관리 하는데 조금 더 수월하게 진행 할 수 있을 것입니다."></textarea>
                  </div>
                </div>
              </div>
              <div class="form-group mt-3">
                <div class="row">
                  <div class="col-lg-2 mx-auto">
                    <span class="font-weight-bold h6 text-muted">3.2.</span>
                  </div>
                  <div class="col-lg-10">
                    <label class="font-weight-bold" for="">다음 평가 기간까지 업무와 관련하여 숙달하고 싶은 분야는 무엇인가요?</label>
                    <textarea v-model="selfReview['3_2']" class="form-control" id="" rows="4" placeholder="예시 - 데이터 분석 기술에 관심이 생겨, 통계 지식을 쌓고자 SAS 자격증을 취득할 예정입니다."></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-5">
              <div class="h5 mt-3 font-weight-bold">
                4. 종합하기
              </div>
              <hr />
              <div class="form-group mt-3">
                <label class="font-weight-bold" for="">당신은 지난 평가 기간동안 자기 스스로에게 몇 점을 줄 수 있습니까?</label>
                <Star @clicked="onClicked_4_1" :name="'profile_4_1'" :value="selfReview['4-1']" :style="{ position: 'relative', top: '3px', left: '26px'}"></Star>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-5 mt-5 pb-5">
        <div class="offset-md-2 col-md-8">
          <button @click.prevent="submit" type="submit" class="btn btn-dark btn-lg btn-block">제출하기</button>
        </div>
      </div>
    </form>
  </section>
</div>
</template>

<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import Star from '@/views/common/Star.vue';
import Breadcrumb from '@/views/Breadcrumb.vue';
import AT from '@/store/action-types';

export default {
  name: 'CreateProfile',
  components: {
    Breadcrumb,
    Star,
  },
  data: function () {
    return {
      firstName: 'Jiyoung',
      lastName: 'Lee',
      img: 'profile_1.png',
      walletAddress: 'hx1234123412341234123412341234123412341234',
      company: 'ICONLOOP',
      team: '기획1팀',
      position: '매니저',
      introduction: '전 개발을 잘하는 김진현입니다.',
      selfReview: {
        '1_1': 'ICONex 프로젝트에서 소프트웨어 개발 전반을 담당하였고, 트래커 프론트엔드 개발 보조 및 icon-sdk-js 개발 보조를 담당하였습니다.',
        '1_2': 'ICONex 프로젝트를 최선을 다해 수행하였습니다.',
        '1_3': '자랑스러운 성과는 이것입니다.',
        '1_4': '열심히 해서입니다.',
        '1_5': 0,
        '2_1': '프론트엔드 개발 지식',
        '2_2': '인생을 사는 법',
        '2_3': '시간 참 짧네요',
        '3_1': '좀 더 빨리 개발 가능할듯요',
        '3_2': '데이 트레이딩',
        '4_1': 0,
      },
    };
  },
  computed: {
    ...mapState({
      isSuccess: state => state.ProfileForm.isSuccess,
      userId: state => state.LoginForm.userId,
    }),
  },
  watch: {
    isSuccess: function(isSuccess) {
      console.log(isSuccess)
      if (isSuccess) {
        this.$router.push('/profile');
        this[AT.PROFILE_FORM.RESET]();
      }
    },
  },
  methods: {
    ...mapActions([
      AT.PROFILE_FORM.SUBMIT,
      AT.PROFILE_FORM.RESET,
    ]),
    uploadFile: function (event) {
      const data = event.target.files[0];
      this.img = data.name;
    },
    onClicked_1_5: function (e) {
      this.selfReview = Object.assign({}, this.selfReview, {
        '1_5': Number(e.value),
      });
    },
    onClicked_4_1: function (e) {
      this.selfReview = Object.assign({}, this.selfReview, {
        '4_1': Number(e.value),
      });
    },
    submit: function () {
      console.log(this.firstName, this.lastName);
      this[AT.PROFILE_FORM.SUBMIT]({
        firstName: this.firstName,
        lastName: this.lastName,
        img: this.img,
        walletAddress: this.walletAddress,
        company: this.company,
        team: this.team,
        position: this.position,
        introduction: this.introduction,
        selfReview: {
          '1_1': this.selfReview['1_1'],
          '1_2': this.selfReview['1_2'],
          '1_3': this.selfReview['1_3'],
          '1_4': this.selfReview['1_4'],
          '1_5': this.selfReview['1_5'],
          '2_1': this.selfReview['2_1'],
          '2_2': this.selfReview['2_2'],
          '2_3': this.selfReview['2_3'],
          '3_1': this.selfReview['3_1'],
          '3_2': this.selfReview['3_2'],
          '4_1': this.selfReview['4_1'],
        },
        userId: this.userId,
      });
    },
    getImgUrl(pic) {
      return require('../../assets/' + pic);
    }
  },
};
</script>



