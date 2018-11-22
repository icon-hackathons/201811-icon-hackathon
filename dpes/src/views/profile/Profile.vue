<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/profile/ProfileHeader.vue'
import ProfileSelfEval from '@/views/profile/ProfileSelfEval.vue'

export default {
  name: 'Profile',
  components: {
    Breadcrumb,
    ProfileHeader,
    ProfileSelfEval,
  },
};
</script>

<template>
  <!-- eslint-disable max-len -->
<div class="mb-5 pb-5 text-body" style="height:100%;">

  <Breadcrumb
    organization=""
    title="내 정보"
    workspace=""
    group=""
    remaintime="" />

  <ProfileHeader />

  <section class="container">
    <div class="row mb-4 mt-4">
      <div class="offset-md-1 col-md-10 offset-md-1">
        <ProfileSelfEval />
      </div>
    </div>
  </section>

</div>
</template>
