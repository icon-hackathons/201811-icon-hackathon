<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/ProfileHeader.vue'
export default {
  name: 'Profile',
  components: {
    Breadcrumb,
    ProfileHeader
  },
};
</script>

<template>
  <!-- eslint-disable max-len -->
<div class="mb-5 pb-5 text-body h-100">

  <Breadcrumb
    organization=""
    title="프로필 생성하기"
    workspace=""
    group=""
    remaintime="" />

  <ProfileHeader />

</div>
</template>
