<template>
  <ul class="m-0 p-0 list-none rounded p-2 flex flex-col gap-2 w-full">
    <MediaQuickInfo v-if="currentTrack" :track="currentTrack" class="bg-blue-500" />
    <MediaQuickInfo v-for="(track, index) in nextTracks" :key="index" :track="track" />
  </ul>
</template>

<script setup lang="ts">
  import { computed } from "@vue/reactivity";

  import { useSpotifyStore } from "@/store/spotify";

  import MediaQuickInfo from "./MediaQuickInfo.vue";

  const spotifyStore = useSpotifyStore();

  // computed
  const currentTrack = computed(() => spotifyStore.player.currentTrack);
  const nextTracks = computed(() => spotifyStore.player.nextTracks);
</script>
