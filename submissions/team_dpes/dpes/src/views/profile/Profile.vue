<script>
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/profile/ProfileHeader.vue'
import ProfileSelfEval from '@/views/profile/ProfileSelfEval.vue'
import Star from '@/views/common/Star.vue';
import AT from '@/store/action-types';

export default {
  name: 'Profile',
  components: {
    Breadcrumb,
    ProfileHeader,
    ProfileSelfEval,
  },
  computed: {
    ...mapState({
      loading: state => state.Profile.loading,
      userId: state => state.LoginForm.userId,
      profile: state => state.Profile.profile,
    }),
  },
  methods: {
    ...mapActions([
      AT.PROFILE.GET_PROFILE,
      AT.PROFILE.RESET,
    ]),
  },
  created() {
    this[AT.PROFILE.GET_PROFILE](this.userId || 1);
  },
};
</script>

<template>
  <!-- eslint-disable max-len -->
  <div v-if="loading" class="mb-5 pb-5 text-body" style="height:100%;">

  </div>
  <div v-else class="mb-5 pb-5 text-body" style="height:100%;">
    <Breadcrumb
      organization=""
      title="내 정보"
      workspace=""
      group=""
      remaintime="" />
    <ProfileHeader
      :profile="profile" />
    <section class="container">
      <div class="row mb-4 mt-4">
        <div class="offset-md-1 col-md-10 offset-md-1">
          <ProfileSelfEval
            :profile="profile" />
        </div>
      </div>
    </section>
  </div>
</template>
