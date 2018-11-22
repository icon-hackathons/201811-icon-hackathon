<script>
import Breadcrumb from '@/views/Breadcrumb.vue'
export default {
  name: 'AuditDone',
  components: {
    Breadcrumb,
  },

};

</script>

<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">

  <Breadcrumb
    organization=""
    title="승인심사 결과"
    workspace=""
    remaintime="" />

  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">승인심사</h2>
        <p class="text-muted mt-1">
        </p>

      </div>
    </div>

      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">

          <div class="card border-0 rounded text-left p-5">
              <div class="row">
                <div class="col-md-12 text-center">

                  <div class="text-center">
                    <h1 class="display-3 font-weight-bold">승인</h1>
                  </div>
                  <div class="small text-center mt-3">승인 시 인센티브가 지급됩니다.</div>

                </div>
              </div>

          </div>
        </div>

      </div>

  </section>
</div>
</template>
