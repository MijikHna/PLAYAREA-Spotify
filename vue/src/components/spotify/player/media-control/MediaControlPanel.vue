<template>
  <div class="min-h-full flex flex-wrap justify-between">
    <PlaybackControl class="min-w-full player" />
    <MediaInfoDisplay class="min-w-full visualizer" />
    <TimeLineSlider class="min-w-full track-slider" />
  </div>
</template>

<script setup lang="ts">
  import TimeLineSlider from "./TimeLineSlider.vue";
  import PlaybackControl from "./PlaybackControl.vue";
  import MediaInfoDisplay from "./MediaInfoDisplay.vue";
</script>

<style scoped>
  .player {
    height: 10%;
  }

  .visualizer {
    height: 80%;
    overflow-y: auto;
  }

  .track-slider {
    height: 10%;
  }
</style>
