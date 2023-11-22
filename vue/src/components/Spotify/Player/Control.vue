<template>
  <div class="min-h-full flex flex-wrap align-content-between">
    <PlayerBar class="flex min-w-full player" />
    <Visualizer class="flex min-w-full visualizer" />
    <TrackSlider class='flex min-w-full track-slider' />
  </div>
</template>

<script setup lang="ts">
import PlayerBar from "./PlayerBar.vue";
import TrackSlider from "./TrackSlider.vue";
import Visualizer from "./Visualizer.vue";

</script>

<style scoped>
.player {
  /* position: absolute; */
  height: 10%;
}

.visualizer {
  /* position: absolute; */
  height: 80%;
  max-height: calc(100vh - 56px - 40px - 42px - 46px - 34px - 50px - 26px - 14px);
  overflow-y: auto;
}

.track-slider {
  /* position: absolute; */
  height: 10%;
}
</style>
