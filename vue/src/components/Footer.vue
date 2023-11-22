<template>
  <footer class="footer mt-auto py-3 footer-bg-color">
    PLAYAREA 2 APP. This App contains following Apps
    <router-link :to="{ name: 'spotify' }">Spotify</router-link>,
    <router-link :to="{ name: 'sheet' }">Sheet</router-link>
  </footer>
</template>

<script setup lang="ts"></script>

<style scoped>
.footer-bg-color {
  background-color: var(--surface-100);
  color: var(--surface-900);
}
</style>
