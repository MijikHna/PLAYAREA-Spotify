<template>
  <div class="container px-3">
    <div class="row border border-2 border-success">
      <Track v-if="currentTrack" :track="currentTrack" />
    </div>

    <div class="row">
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
