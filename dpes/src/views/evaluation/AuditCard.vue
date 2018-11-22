<template>

  <!-- 카드 -->
  <div class="card mt-2">
    <div class="card-body p-4 text-left">
      <span class="ml-3">{{ name }}{{ address }}</span>
      <span class="ml-3 float-right" >
        <span class="font-weight-bold">평가 점수</span>
        <span class="font-weight-light ml-2">{{ value }}</span>
      </span>
    </div>
  </div>
  <!-- 카드 -->

</template>

<script>
export default {
  name: 'AuditCard',
  props: {
    name: String,
    address: String,
    value: Number,
  }
}
</script>
