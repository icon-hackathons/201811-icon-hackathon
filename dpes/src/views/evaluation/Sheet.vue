<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/ProfileHeader.vue'
export default {
  name: 'Sheet',
  components: {
    Breadcrumb,
    ProfileHeader
  },
};
</script>

<template>
  <!-- eslint-disable max-len -->
<div class="mb-5 pb-5 text-body" style="height:100%;">

  <Breadcrumb
    organization="ICONLoop"
    title="평가 시트 작성하기"
    workspace=" > ICONLoop 1Q 상반기 전사 성과 평가"
    group=" > 비즈니스기획팀"
    remaintime="남은 시간 3일 17:39:58" />

  <ProfileHeader />

  <div class="row pb-5">
    <div class="offset-md-1 col-md-10 offset-md-1">
      <div class="row">

        <div class="col-md-4 mt-3 p-2">
          <div class="title">
            <div class="h6 mt-3 text-left">
              <span class="font-weight-bold">자가 평가</span>
              <router-link :to="{name: ''}" class="text-muted small float-right">자세히 보기</router-link>
            </div>
          </div>


          <div class="row text-left">

            <div class="col-md-12 mt-3">
              <div class="card">
                <div class="card-body">
                  <h6 class="card-subtitle mt-2 mb-3 text-secondary">
                    가장 자랑스러운 업적 2-3개는 무엇이었나요?
                  </h6>
                  <p class="card-text">
                    가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다.
                  </p>
                </div>
              </div>
            </div>
            <div class="col-md-12 mt-3">
              <div class="card">
                <div class="card-body">
                  <h6 class="card-subtitle mt-2 mb-3 text-secondary">
                    가장 자랑스러운 업적 2-3개는 무엇이었나요?
                  </h6>
                  <p class="card-text">
                    가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-12 mt-3">
              <div class="card">
                <div class="card-body">
                  <h6 class="card-subtitle mt-2 mb-3 text-secondary">
                    가장 자랑스러운 업적 2-3개는 무엇이었나요?
                  </h6>
                  <p class="card-text">
                    가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다.
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-12 mt-3">
              <div class="card">
                <div class="card-body">
                  <h6 class="card-subtitle mt-2 mb-3 text-secondary">
                    가장 자랑스러운 업적 2-3개는 무엇이었나요?
                  </h6>
                  <p class="card-text">
                    가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다.
                  </p>
                </div>
              </div>
            </div>

          </div>

        </div>

        <div class="col-md-8 mt-3">
          <div class="title">
            <div class="h6 mt-3 text-left">
              <span class="font-weight-bold">평가 시트 작성</span>
              <router-link :to="{name: ''}" class="text-muted small float-right">자세히 보기</router-link>
            </div>
          </div>

          <div class="row text-left">
            <div class="col-md-12 mt-3">

              <form class="evsheets">
                <div class="category text-muted">
                  1.대상자의 프로젝트/팀 내 기여도는?
                </div>

                <div class="form-group mt-4">
                  <h6>이 사람을 ABCDEFGRGERGRGERGERGR입니까?</h6>

                  <div class="mt-3 form-row">
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio1" id="inlineRadio1" value="option1">
                      <label class="form-check-label" for="inlineRadio1">1</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio1" id="inlineRadio2" value="option2">
                      <label class="form-check-label" for="inlineRadio2">2</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio1" id="inlineRadio3" value="option3">
                      <label class="form-check-label" for="inlineRadio2">3</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio1" id="inlineRadio4" value="option4">
                      <label class="form-check-label" for="inlineRadio2">4</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio1" id="inlineRadio5" value="option5">
                      <label class="form-check-label" for="inlineRadio2">5</label>
                    </div>
                  </div>

                </div>

                <div class="form-group mt-5">
                  <h6>이 사람을 ABCDEFGRGERGRGERGERGR입니까?</h6>

                  <div class="mt-3 form-row">
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio2" id="inlineRadio1" value="option1">
                      <label class="form-check-label" for="inlineRadio1">1</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio2" id="inlineRadio2" value="option2">
                      <label class="form-check-label" for="inlineRadio2">2</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio2" id="inlineRadio3" value="option3">
                      <label class="form-check-label" for="inlineRadio2">3</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio2" id="inlineRadio4" value="option4">
                      <label class="form-check-label" for="inlineRadio2">4</label>
                    </div>
                    <div class="form-check form-check-inline col-md-2">
                      <input class="form-check-input" type="radio" name="radio2" id="inlineRadio5" value="option5">
                      <label class="form-check-label" for="inlineRadio2">5</label>
                    </div>
                  </div>

                </div>

                <button type="submit" class="btn btn-block btn-lg btn-dark mt-5">제출하기</button>
              </form>

            </div>
          </div>

        </div>

      </div>

    </div>
  </div>


</div>
</template>
