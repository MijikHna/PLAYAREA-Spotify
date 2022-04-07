<template>
  <div class="border border-success">
    <Track
      v-if="currentTrack"
      :track="currentTrack"
    />
  </div>
  <div class="border-end">
    <Track v-for="(track, index) in tracks" :key="index" :track="track" />
  </div>
</template>

<script lang="ts">
import { ITrack } from "@/interfaces/spotifyInterfaces";
import Track from "@/components/Spotify/Track.vue";

import { defineComponent } from "vue";
import { computed } from "@vue/reactivity";
import { Store, useStore } from "vuex";

export default defineComponent({
  name: "TrackList",
  components: {
    Track,
  },
  setup(){
    //global
    const store: Store<any> = useStore();

    //data
    const tracks: ITrack[] = [
      {
        name: "test001",
        duration_ms: 40203,
      },
      {
        name: "test002",
        duration_ms: 100120,
      },
    ]

    const currentTrack = computed(() => {
      return store.state.spotify.currentTrack;
    });

    //computed

    const getCurrenTrack = function(){

    }

    return {
      //data
      tracks,
      currentTrack,
      //methods
    }
  }
});
</script>

<style scoped></style>