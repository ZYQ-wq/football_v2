<template>
  <div class="commentary-panel">
    <div v-for="(line, idx) in lines" :key="idx">{{ line }}</div>
  </div>
</template>

<script>
export default {
  props: ['lines']
}
</script>

<style>
.commentary-panel {
  border: 1px solid #ccc;
  height: 400px;
  overflow-y: auto;
  padding: 10px;
  background: #f8f8f8;
  font-family: sans-serif;
}
</style>