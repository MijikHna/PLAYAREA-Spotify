<template>
 <div class="border-end">
    <Track v-for="(track, index) in tracks" :key="index" :track="track" />
  </div>
</template>

<script lang="ts">
import { ITrack } from "@/interfaces/spotify/spotifyInterfaces";
import Track from "@/components/Spotify/Track.vue";

import { defineComponent } from "vue";

export default defineComponent({
  name: "TrackList",
  components: {
    Track,
  },
  setup(){
    const tracks: ITrack[] = [
      {
        name: "test001",
        duration: "1.00",
      },
      {
        name: "test002",
        duration: "2.00",
      },
    ]

    return {
      tracks,
    }
  }
});
</script>

<style scoped></style>