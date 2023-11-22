<template>
  <main class="full-view grid m-0">
    <router-view></router-view>
  </main>
  <Toast />
</template>

<script setup lang="ts">
import Toast from 'primevue/toast';
</script>

<style scoped>
.full-view {
  min-height: calc(100vh - 56px - 56px);
}
</style>
