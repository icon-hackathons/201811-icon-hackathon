<template>
  <div class="col-md-3">
    <div class="card mt-4" style="width: 16rem;">
      <img class="card-img-top" :src="getRandomImg()" alt="Card image cap" style="height:150px;">
      <div class="card-body">
        <h5 class="card-title">{{ group.name }}</h5>
        <p class="card-text">
            <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small" />
            <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
            <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
            <img src="../../assets/img_sample.jpg" class="thumbnail rounded-circle small ml-1" />
            <span class="ml-2 text-muted small">+{{ group.count - 4 }}</span>
        </p>
        <div class="row mb-2">
            <div class="col-md-4">
            <h6 class="card-text font-weight-bold">{{ group.count }}명</h6>
            <h6 class="card-text text-muted small">멤버</h6>
            </div>
            <div class="col-md-4">
            <h6 class="card-text font-weight-bold">{{ group.progress }}</h6>
            <h6 class="card-text text-muted small">평가 진행</h6>
            </div>
            <div class="col-md-4">
            <h6 class="card-text font-weight-bold">{{ group.leader }}</h6>
            <h6 class="card-text text-muted small">그룹장</h6>
            </div>
        </div>
        <div>
            <router-link :to="{name: 'groupprofilelist'}" tag="button" class="btn btn-secondary btn btn-block mt-4 mb-2">멤버 조회</router-link>
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
  name: 'GroupCard',
  props: ['group'],
  data: function () {
    return {
      loading: true,
      imgKey: Math.floor(Math.random() * 2) + 1,
    };
  },
  methods: {
    getRandomImg() {
      return require(`../../assets/card-top-bg${this.imgKey}.jpg`);
    }
  },
};
</script>
