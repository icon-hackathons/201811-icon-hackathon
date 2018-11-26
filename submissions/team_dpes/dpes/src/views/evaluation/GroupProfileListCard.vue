<template>
<div class="col-md-4 mt-3">
  <div class="card" style="width: 16rem;">
    <img class="card-img-top p-5 rounded-circle text-center mx-auto" :src="getImg(user.img)" alt="Card image cap" style="height:200px;width:200px;">
    <div class="card-body">
    <h5 class="card-title">{{ user.name }}</h5>
    <h6 class="card-subtitle text-muted small">{{ user.team }}</h6>
    <div class="row mb-2 mt-3">
        <div class="col-md-4">
        <h6 class="card-text font-weight-bold">132</h6>
        <h6 class="card-text text-muted small">평가자 수</h6>
        </div>
        <div class="col-md-4">
        <h6 class="card-text font-weight-bold">70</h6>
        <h6 class="card-text text-muted small">진행률</h6>
        </div>
        <div class="col-md-4">
        <h6 class="card-text font-weight-bold">{{ parseInt(userInfo.grade, 16) || 0 }}</h6>
        <h6 class="card-text text-muted small">평균 점수</h6>
        </div>
    </div>
    <div>
        <button @click.prevent="submit" tag="button" class="btn btn-secondary btn btn-block mt-3">평가 시트 작성하기</button>
    </div>
    </div>
  </div>
</div>
</template>


<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import AT from '@/store/action-types';
import DpesScoreAPI from '@/api/DpesScoreAPI';
import { IconAmount, IconConverter } from 'icon-sdk-js';

export default {
  name: 'GroupProfileListCard',
  props: ['user'],
  data: function () {
    return {
      userInfo: {}
    };
  },
  computed: {
    ...mapState({
      profile: state => state.Profile.profile,
    }),
  },
  created: async function() {
    const userInfo = await DpesScoreAPI.getUserInfo(this.user.walletAddress);
    this.userInfo = userInfo;
  },
  watch: {
    profile: function(val) {
      console.log(val)
      if (val.hasOwnProperty('selfReview')) {
        this.$router.push('/evaluation/sheet');
      }
    },
  },
  methods: {
    ...mapActions([
      AT.PROFILE.GET_PROFILE,
    ]),
    getImg: function (img) {
      console.log(img)
      return require(`../../assets/${img}`);
    },
    submit: function () {
      this[AT.PROFILE.GET_PROFILE](this.user.id);
    }
  }
};
</script>
