<template>
  <div class="col-md-4">
    <div v-if="loading" style="width: 18rem;"></div>
    <div v-else class="card" style="width: 18rem;">
      <img class="card-img-top" :src="getRandomImg()" alt="Card image cap" style="height:150px;">
      <div class="card-body">
        <h5 class="card-title">{{ projectName }}</h5>
        <div class="row mb-2">
          <div class="col-md-12 mt-2">
          <h6 class="card-text font-weight-bold">{{ prizeAmount }} ICX</h6>
          <h6 class="card-text text-muted small">총 리워드 풀 예치금</h6>
          </div>
          <div class="col-md-12 mt-3">
          <h6 class="card-text font-weight-bold">{{ convertedDistance }}</h6> <!-- 3일 17:39:58 -->
          <h6 class="card-text text-muted small">남은 시간</h6>
          </div>
          <div class="col-md-12 mt-3">
          <h6 class="card-text font-weight-bold">145명</h6>
          <h6 class="card-text text-muted small">평가 대상자</h6>
          </div>
        </div>
        <div>
           <!-- <router-link :to="{name: 'grouplist'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">부서 조회</router-link> -->
            <button @click.prevent="submit" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">부서 조회</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import AT from '@/store/action-types';
import DpesProjectAPI from '@/api/DpesProjectAPI';
import { IconAmount, IconConverter } from 'icon-sdk-js';

export default {
  name: 'WorkspaceCard',
  props: ['projectAddress'],
  data: function () {
    return {
      timer: '',
      loading: true,
      projectName: '',
      dueDate: 0,
      prizeAmount: 0,
      imgKey: Math.floor(Math.random() * 2) + 1,
    };
  },
  computed: {
    ...mapState({
      workspace: state => state.Workspace.workspace,
    }),
    prizeAmountICX: function () {
      return this.message.split('').reverse().join('')
    },
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
    const projectInfo = await DpesProjectAPI.getProjectInfo(this.projectAddress);
    console.log(projectInfo)
    this.projectName = projectInfo.name;
    this.dueDate = parseInt(projectInfo.due_date, 16) - ((new Date()).getTime() * 1000);
    this.prizeAmount = Number(IconAmount.of(projectInfo.prize_amount, IconAmount.Unit.LOOP).convertUnit(IconAmount.Unit.ICX).value);
    this.loading = false;
  },
  watch: {
    loading: function (val) {
      if (!val) {
        this.startTimer();
        this.timer = setInterval(this.startTimer, 1000);
      }
    },
    workspace: function (val) {
      if (val.hasOwnProperty('projectName')) {
        this.$router.push('/evaluation/grouplist');
      }
    }
  },
  methods: {
    ...mapActions([
      AT.WORKSPACE.GET_WORKSPACE,
    ]),
    submit: function () {
      this[AT.WORKSPACE.GET_WORKSPACE](this.projectAddress);
    },
    startTimer: function () {
      this.dueDate = this.dueDate - 1000000
    },
    getRandomImg() {
      return require(`../../assets/card-top-bg${this.imgKey}.jpg`);
    }
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer);
  }
};
</script>
