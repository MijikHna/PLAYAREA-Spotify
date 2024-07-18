<template>
  <div class="flex justify-content-center mt-4" v-if="player.currentTrack">
    <ScrollPanel style="width: 100%; height: var(--visualizer-height);" :pt="{
      wrapper: {
        style: { 'border-right': '10px solid var(--surface-ground)' }
      },
      bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
    }">
      <MediaInfo :track="player.currentTrack" />
    </ScrollPanel>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import ScrollPanel from "primevue/scrollpanel";


import { useSpotifyStore } from '@/store/spotify';
import MediaInfo from './MediaInfo.vue';

// global
const spotifyStore = useSpotifyStore();

// data 
const { player } = storeToRefs(spotifyStore);

</script>

<style scoped></style>
