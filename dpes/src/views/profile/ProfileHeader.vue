<template>
<!-- eslint-disable max-len -->
  <section class="jumbotron mb-0 p-4 bg-light text-body">
    <div class="row">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <div class="row">
          <div class="col-md-4">
            <img class="thumbnail round" :src="getImgUrl(profile.img)" alt="Card image cap" style="">
          </div>
          <div class="col-md-8 text-left">
            <h3 class="font-weight-bold mb-0">{{`${profile['name']}`}}</h3>
            <span class="text-muted" style="font-size:15px;">{{ profile['team'] }}</span>
            <div class="row mt-3">
              <div class="col-md-3">
                <span class="h5 font-weight-bold">123</span><span class="text-muted ml-2" style="font-size:15px;">평가자 수</span>
              </div>
              <div class="col-md-3">
                <span class="h5 font-weight-bold">{{ parseInt(profile['balance'], 16) }}</span><span class="text-muted ml-2" style="font-size:15px;">진행률</span>
              </div>
              <div class="col-md-3">
                <span class="h5 font-weight-bold"> {{ parseInt(profile['grade'], 16) }}</span><span class="text-muted ml-2" style="font-size:15px;">평균 점수</span>
              </div>
            </div>
            <div class="row mt-4">
              <div class="col-md">
                <h6 class="text-muted">
                  {{ profile['introduction'] }}
                </h6>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import AT from '@/store/action-types';

export default {
  name: 'ProfileHeader',
  props: [
    'profile'
  ],
  methods: {
    getImgUrl(pic) {
      return require('../../assets/' + pic);
    }
  },
};
</script>
