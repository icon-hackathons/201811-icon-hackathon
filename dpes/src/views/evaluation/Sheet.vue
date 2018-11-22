<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/profile/ProfileHeader.vue'
import ProfileProject from '@/views/profile/ProfileProject.vue'
import ProfileSelfEval from '@/views/profile/ProfileSelfEval.vue'

export default {
  name: 'Sheet',
  components: {
    Breadcrumb,
    ProfileHeader,
    ProfileProject,
    ProfileSelfEval,
  },
};
</script>

<template>
<!-- eslint-disable max-len -->
<div class="mb-5 pb-5 text-body" style="height:100%;">

  <Breadcrumb organization="ICONLoop" title="평가 시트 작성하기" workspace=" > ICONLoop 1Q 상반기 전사 성과 평가" group=" > 비즈니스기획팀" remaintime="남은 시간 3일 17:39:58" />

  <ProfileHeader />

  <section class="container">
    <div class="row mb-4 mt-4">

      <div class="offset-md-1 col-md-10 offset-md-1">
        <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active text-body" id="pills-eval-tab" data-toggle="pill" href="#pills-eval" role="tab" aria-controls="pills-eval" aria-selected="true">
              XXX님 평가하기
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

                            ddd
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
                            5점 별점
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
                            <label class="font-weight-bold" for="">2.1 평가대상자의 평소 업무의 질은 어땠나요?</label>
                            ㅇㅇ
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
                            ㅇㅇㅇㅇ
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
                            ㅇㅇㅇ
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
                            ㅇㅇㅇ
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
                            ㅇㅇㅇ
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
                            ㅇㅇㅇ
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
                            ㅇㅇㅇ
                          </div>
                        </div>
                      </div>

                      <div class="form-group mt-3">
                        <div class="row">
                          <div class="col-lg-1 mx-auto">
                            <span class="font-weight-bold h6 text-muted">3.2.</span>
                          </div>
                          <div class="col-lg-11">
                            <label class="font-weight-bold" for="">평가대상자는 팀원에게 얼마나 협조적이었나요?</label>
                            ㅇㅇㅇ
                          </div>
                        </div>
                      </div>

                    </div>

                  </div>
                </div>
              </div>

            </div>

            <div class="tab-pane fade show text-left" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
              <ProfileSelfEval />

            </div>
            <div class="tab-pane fade" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">
              <ProfileProject />
            </div>
          </div>

          <div class="row mt-5 mt-5 pb-5">
            <div class="col-md-12">
              <button type="submit" class="btn btn-dark btn-lg btn-block">제출하기</button>
              <router-link :to="{name: 'auditstarted'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">Audit(개발용)</router-link>
            </div>
          </div>

        </form>

      </div>

    </div>
  </section>

</div>
</template>
