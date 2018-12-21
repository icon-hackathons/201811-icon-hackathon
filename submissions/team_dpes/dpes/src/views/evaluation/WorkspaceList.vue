<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ServerAPI from '@/api/ServerAPI';
import WorkspaceCard from '@/views/evaluation/WorkspaceCard.vue'

export default {
  name: 'WorkspaceList',
  components: {
    Breadcrumb,
    WorkspaceCard,
  },
  created: async function() {
    const workspaceList = await ServerAPI.getWorkspaceList();
    console.log(workspaceList)
    this.workspaceList = workspaceList;
  },
  data: function () {
    return {
      workspaceList: []
    }
  }
};
</script>

<template>
<div style="height:100%;">
  <Breadcrumb
    organization="ICONLoop"
    title="워크스페이스 선택하기"
    workspace=""
    remaintime="" />
  <section class="jumbotron mb-0 p-4 border bg-light">
    <div class="row">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <div class="input-group">
          <input type="text" class="form-control" placeholder="Search..." aria-label="Recipient's username" aria-describedby="button-addon2">
          <div class="input-group-append">
            <button class="btn btn-secondary" type="button" id="button-addon2">검색하기</button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="container">
    <div class="row mb-4 mt-4">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <div class="row mb-2">
          <div class="col-md text-left">
            <h5>총 {{workspaceList.length}}개의 연결된 워크스페이스를 찾았습니다</h5>
          </div>
        </div>
        <div class="row">
          <!-- 카드 시작 -->
          <div v-for="(address, i) in workspaceList" v-bind:key="i">
            <WorkspaceCard :key="i" :projectAddress="address" />
          </div>
          <!-- 카드 끝 -->
        </div>
        <div class="row" style="margin-top:30px;">
        </div>
        <div class="row" style="margin-top:30px;">
        </div>
      </div>
    </div>
  </section>
</div>
</template>
