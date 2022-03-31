<template>
  <div class="border">
    <div>{{ track.name }}</div>
    <div>{{ track.duration }}</div>
  </div>
</template>

<script lang="ts">
import { ITrack } from "@/interfaces/spotify/spotifyInterfaces";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "Track",
  props: {
    track: {
      type: Object as PropType<ITrack>,
    },
  },
});
</script>

<style scoped></style>