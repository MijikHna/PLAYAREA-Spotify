<template>
  <div class="container px-3">
    <div class="row border border-2 border-success">
      <Track
        v-if="currentTrack"
        :track="currentTrack"
      />
    </div>

    <div class="row">
      <Track v-for="(track, index) in nextTracks" :key="index" :track="track" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { Store, useStore } from 'vuex';
import { computed } from '@vue/reactivity';

import Track from '@/components/Spotify/Track.vue';

const store: Store<any> = useStore();

// computed
const currentTrack = computed(() => store.state.spotify.currentTrack);
const nextTracks = computed(() =>store.state.spotify.nextTracks);

</script>