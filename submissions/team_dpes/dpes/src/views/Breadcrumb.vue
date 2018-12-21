<template>
<!-- eslint-disable max-len -->
<section class="jumbotron jumbotron-breadcrumb set-bg">
  <div class="text-white container">
    <div class="row">
      <div class="col-md">
        <h6 class="breadcrumb-state">{{ organization }}{{ workspace }}{{ group }}</h6>
        <h1 class="title">{{ title }}</h1>
        <h6 class="remaintime mt-1">{{ remaintime }}</h6>
      </div>
    </div>
  </div>
</section>
</template>

<!--
breadcrumb-state
- 현재의 Path를 나타낸다
- 조직명 > 워크스페이스명

title
- 액션을 나타낸다
- 1. StartEv.vue; 평가 시작하기
- 2. Workspace.vue; 워크스페이스 선택하기
- 3. Group.vue; 그룹 선택하기
- 4. GroupProfileList; 평가 대상 선택하기
- 5. YourProfile; XXX님의 프로필 살펴보기
- 6. Evaluation; XXX님 평가하기

remaintime
- 시간 표시
- workspace.vue 이후부터 출력
-->
<script>
export default {
  name: 'Breadcrumb',
  props: {
    title: String,
    workspace: String,
    organization: String,
    group:String,
    remaintime: String,
  }
}
</script>
