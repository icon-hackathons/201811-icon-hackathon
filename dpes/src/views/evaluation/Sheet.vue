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

  <Breadcrumb organization="ICONLoop" title="평가 시트 작성하기" workspace=" > ICONLoop 1Q 상반기 전사 성과 평가" group=" > 비즈니스기획팀" remaintime="남은 시간 3일 17:39:58" />

  <ProfileHeader />

  <section class="container">
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
          <div class="tab-pane fade show active text-left" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">

            <div class="row">
              <div class="col-md-12 pt-3 pb-3">
                <h5>타이틀 제목을 입력해주세요</h5>
              </div>

              <div class="col-md-6">

                <div class="card">
                  <div class="card-body">
                    <font-awesome-icon icon="coffee" class="float-right text-warning"></font-awesome-icon>
                    <h6 class="card-subtitle mt-2 mb-3 text-secondary">
                      가장 자랑스러운 업적 2-3개는 무엇이었나요?
                    </h6>
                    <p class="card-text">
                      가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다. 가장 자랑스러운 업적은 A,B,C였다.
                    </p>
                  </div>
                </div>

              </div>

              <div class="col-md-6">

                <div class="card">
                  <div class="card-body">
                    <font-awesome-icon icon="coffee" class="float-right text-warning"></font-awesome-icon>
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
