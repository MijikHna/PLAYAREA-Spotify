<template>
  <footer class="footer mt-auto py-3 footer-bg-color text-center">
    PLAYAREA Spotify APP. This App contains following Apps
    <router-link class="text-blue-600" :to="{ name: 'home' }">Spotify</router-link>,
  </footer>
</template>

<script setup lang="ts"></script>

<style scoped>
  .footer-bg-color {
    background-color: var(--surface-100);
    color: var(--surface-900);
  }
</style>
