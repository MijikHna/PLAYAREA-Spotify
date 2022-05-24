<template>
  <div class="border h-100">
    <PlayerBar class="player"/>
    <Visualizer class="visualizer" />
    <TrackSlider class='track-slider'/>
  </div>
</template>

<script setup lang="ts">
import PlayerBar from "./PlayerBar.vue";
import Visualizer from "./Visualizer.vue";
import TrackSlider from "./TrackSlider.vue";

</script>

<style scoped>
.player{
  height: 10%;
}
.visualizer {
  height: 80%;
}
.track-slider {
  height: 10%;
}
</style>