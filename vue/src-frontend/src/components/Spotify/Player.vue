<template>
  <div class="border h-100">
    <PlayerBar class="player"/>
    <Visualizer class="visualizer" />
  </div>
</template>

<script lang="ts">
import PlayerBar from "./PlayerBar.vue";
import Visualizer from "./Visualizer.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Player",
  components: {
    PlayerBar,
    Visualizer,
  }
});
</script>

<style scoped>
.player{
  height: 10%;
}
.visualizer {
  height: 90%;
}
</style>