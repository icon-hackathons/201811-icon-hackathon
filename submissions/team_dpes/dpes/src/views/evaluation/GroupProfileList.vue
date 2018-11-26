<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import { mapState, mapActions } from 'vuex';
import ServerAPI from '@/api/ServerAPI';
import GroupProfileListCard from '@/views/evaluation/GroupProfileListCard.vue';

export default {
  name: 'GroupProfileList',
  components: {
    Breadcrumb,
    GroupProfileListCard,
  },
  data: function () {
    return {
      dueDate: 0,
      timer: '',
      profileList: [],
      loading: true,
    }
  },
  computed: {
    ...mapState({
      workspace: state => state.Workspace.workspace,
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
  created: async function() {
    const profileList = await ServerAPI.getProfileList();
    this.profileList = profileList.data;
    console.log(this.profileList)
    this.dueDate = this.workspace.dueDate;
    this.startTimer();
    this.timer = setInterval(this.startTimer, 1000);
    this.loading = false;
  },
  methods: {
    startTimer: function () {
      this.dueDate = this.dueDate - 1000000;
    },
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer);
  }
};
</script>

<template>
<div v-if="loading"></div>
<div v-else style="height:100%;">
  <Breadcrumb
    organization="ICONLoop"
    title="평가 대상자 선택하기"
    :workspace="` > ${workspace.projectName}`"
    :remaintime="`남은 시간 ${convertedDistance}`" />
  <section class="jumbotron mb-0 p-4 border bg-light">
    <div class="row">
      <div class="col-md-12">
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
    <div class="row mb-5 pb-5 mt-4">

      <div class="offset-md-1 col-md-10 offset-md-1">

        <div class="row mb-2">
          <div class="col-md text-left">
            <h5>총 {{profileList.length}}명의 대상자를 찾았습니다</h5>
          </div>
        </div>

        <div class="row">

          <!-- 카드 시작 -->
          <div v-for="(user, i) in profileList" v-bind:key="i">
            <GroupProfileListCard :key="i" :user="user" />
          </div>
          <!-- 카드 끝 -->

        </div>

      </div>

    </div>
  </section>

</div>
</template>
