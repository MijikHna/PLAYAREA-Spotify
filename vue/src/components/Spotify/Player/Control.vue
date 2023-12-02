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
