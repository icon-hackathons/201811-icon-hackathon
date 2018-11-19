<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/ProfileHeader.vue'

export default {
  name: 'EvProfile',
  components: {
    Breadcrumb,
    ProfileHeader
  },
  props: {
		max: { type: Number, required: false, default: 5 },
		value: { type: Number, required: false, default: 0 },
		name: { type: String, required: false, default: "rating" },
		char: { type: String, required: false, default: "★" },
		inactiveChar: { type: String, required: false, default: null },
		readonly: { type: Boolean, required: false, default: false },
		activeColor: { type: String, required: false, default: "#FD0" },
		inactiveColor: { type: String, required: false, default: "#999" },
		shadowColor: { type: String, required: false, default: false },
		hoverColor: { type: String, required: false, default: "#FD0" },
	},
	computed: {
		ratingChars() {
			return Array.from(this.char)
		},
		inactiveRatingChars() {
			/* Default to ratingChars if no inactive characters have been provided */
			return this.inactiveChar
				? Array.from(this.inactiveChar)
				: this.ratingChars
		},
		notouch() {
			/* For iPhone specifically but really any touch device, there is no true hover state, disabled any pseudo-hover activity. */
			return !("ontouchstart" in document.documentElement)
		},
		mapCssProps() {
			return {
				"--active-color": this.activeColor,
				"--inactive-color": this.inactiveColor,
				"--shadow-color": this.shadowColor,
				"--hover-color": this.hoverColor,
			}
		},
	},
	methods: {
		updateInput(v) {
			this.$emit("input", parseInt(v, 10))
		},
		getActiveLabel(x) {
			const s = this.ratingChars
			return s[Math.min(s.length - 1, x - 1)]
		},
		getInactiveLabel(x) {
			const s = this.inactiveRatingChars
			return s[Math.min(s.length - 1, x - 1)]
		},
	},
};
</script>


<style>
.vue-stars {
	display: inline-flex;
	flex-flow: row nowrap;
	align-items: flex-start center;
	line-height: 1em;
  font-size: 30px;
}
.vue-stars label {
	display: block;
	padding: 0.125em;
	width: 1.2em;
	text-align: center;
	color: #fd0;
	text-shadow: 0 0 0.3em #ff0;
}
.vue-stars input,
.vue-stars label .inactive,
.vue-stars input:checked ~ label .active,
.vue-stars.notouch:not(.readonly):hover label .inactive,
.vue-stars.notouch:not(.readonly) label:hover ~ label .active {
	display: none;
}
.vue-stars input:checked ~ label .inactive,
.vue-stars.notouch:not(.readonly):hover label .active,
.vue-stars.notouch:not(.readonly) label:hover ~ label .inactive {
	display: inline;
}
.vue-stars.notouch:not(.readonly):hover label {
	color: #dd0;
	text-shadow: 0 0 0.3em #ff0;
}
input:checked ~ label,
.vue-stars.notouch:not(.readonly) label:hover ~ label {
	color: #999;
	text-shadow: none;
}
@supports (color: var(--prop)) {
	.vue-stars label {
		color: var(--active-color);
		text-shadow: 0 0 0.3em var(--shadow-color);
	}
	.vue-stars.notouch:not(.readonly):hover label {
		color: var(--hover-color);
		text-shadow: 0 0 0.3em var(--shadow-color);
	}
	.vue-stars input:checked ~ label,
	.vue-stars.notouch:not(.readonly) label:hover ~ label {
		color: var(--inactive-color);
	}
}
</style>


<template>
<div class="mb-5 pb-5" style="height:100%;">

  <Breadcrumb organization="ICONLoop" title="평가 대상자 프로필 살펴보기" workspace=" > ICONLoop 1Q 상반기 전사 성과 평가" remaintime="남은 시간 3일 17:39:58" />

  <ProfileHeader />

  <section class="container text-body">

    <div class="row mb-4 mt-4">

      <div class="offset-md-1 col-md-10 offset-md-1">
        <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active text-body" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab" aria-controls="pills-home" aria-selected="true">자가 평가</a>
          </li>

          <li class="nav-item">
            <a class="nav-link text-body" id="pills-contact-tab" data-toggle="pill" href="#pills-contact" role="tab" aria-controls="pills-contact" aria-selected="false">최근 참가 프로젝트</a>
          </li>
        </ul>
        <div class="tab-content" id="pills-tabContent">
          <!-- 패널 1 -->
          <div class="tab-pane fade show active text-left" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여
                        ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                      <p style="font-size:13px;">
                        5
                      </p>
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다. ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                        ABC와 BCD, EFG를 AGFGREFWEFEWF하여 ERGERGERFWEF하게 ERGERG했습니다.
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
                      <p style="font-size:13px;">

                      </p>
                    </div>
                  </div>
                </div>

                <div class="card" style="">

                  <div class="vue-stars"
                      :class="{readonly:readonly,notouch:notouch}"
                      ref="ratingEl"
                      :style="mapCssProps"
                      >
                      <input type="radio" :id="name+'0'" :checked="value===0" :name="name" value="0">
                      <template v-for="x in max">
                        <label :for="name+x" :key="'l'+x">
                          <span class="active"><slot name="activeLabel">{{ getActiveLabel(x) }}</slot></span>
                          <span class="inactive"><slot name="inactiveLabel">{{ getInactiveLabel(x) }}</slot></span>
                        </label><input
                          :key="'i'+x"
                          type="radio"
                          @change="updateInput($event.target.value)"
                          :checked="value===x"
                          :id="name+x"
                          :name="name"
                          :disabled="readonly"
                          :value="x">
                      </template>
                    </div>


                </div>

              </div>

            </div>

          </div>

          <!-- 패널 2 -->
          <div class="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">
            <div class="row">

              <div class="col-md-4">

                <div class="card" style="width: 18rem;">
                  <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
                  <div class="card-body">
                    <h5 class="card-title mb-0">P-Rep 선출 프로젝트</h5>

                    <div class="mt-4 mb-3">
                      <div class="text-muted small">
                        함께 참여한 사람
                      </div>
                      <div class="mt-2">
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <span class="ml-2 text-muted small">+3</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <div class="col-md-4">

                <div class="card" style="width: 18rem;">
                  <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
                  <div class="card-body">
                    <h5 class="card-title mb-0">스마일게이트 프로젝트</h5>

                    <div class="mt-4 mb-3">
                      <div class="text-muted small">
                        함께 참여한 사람
                      </div>
                      <div class="mt-2">
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <span class="ml-2 text-muted small">+3</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <div class="col-md-4">

                <div class="card" style="width: 18rem;">
                  <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
                  <div class="card-body">
                    <h5 class="card-title mb-0">IISS 프로젝트</h5>

                    <div class="mt-4 mb-3">
                      <div class="text-muted small">
                        함께 참여한 사람
                      </div>
                      <div class="mt-2">
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <span class="ml-2 text-muted small">+3</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <div class="col-md-4">

                <div class="card" style="width: 18rem;">
                  <img class="card-img-top" src="../../assets/img_sample.jpg" alt="Card image cap" style="height:150px;">
                  <div class="card-body">
                    <h5 class="card-title mb-0">Decampus 프로젝트</h5>

                    <div class="mt-4 mb-3">
                      <div class="text-muted small">
                        함께 참여한 사람
                      </div>
                      <div class="mt-2">
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
                        <span class="ml-2 text-muted small">+3</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

            </div>
          </div>

        </div>
        <div class="row mt-5">
          <div class="col-md">
            <router-link :to="{name: 'sheet'}" tag="button" class="btn btn-dark btn btn-block btn-lg">평가 시트 작성하기</router-link>
          </div>
        </div>

      </div>

    </div>
  </section>



</div>
</template>
