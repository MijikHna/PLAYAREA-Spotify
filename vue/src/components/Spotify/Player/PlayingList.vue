<template>
  <div class="flex flex-column p2-3">
    <div class="col-12 border-white">
      <Track v-if="currentTrack" :track="currentTrack" class="surface-500"/>
    </div>

    <div class="col-12">
      <Track v-for="(track, index) in nextTracks" :key="index" :track="track" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "@vue/reactivity";

import { useSpotifyStore } from "@/store/spotify";

import Track from "@/components/Spotify/Track.vue";

const spotifyStore = useSpotifyStore();

// computed
const currentTrack = computed(() => spotifyStore.currentTrack);
const nextTracks = computed(() => spotifyStore.nextTracks);
</script>
