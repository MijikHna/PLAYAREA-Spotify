<template>
  <PlaybackQueueNavigator />
  <Divider align="center">
    <span class="p-tag">Playlist</span>
  </Divider>
  <PlayListNavigator />
</template>

<script setup lang="ts">
  import Divider from "primevue/divider";

  import PlaybackQueueNavigator from "./PlaybackQueueNavigator.vue";
  import PlayListNavigator from "./PlayListNavigator.vue";
</script>
