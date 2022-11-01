<template>
  <div class="container px-3 playlist-height">
    <div class="row" v-if="playerActive && playList">
      <Track
        v-for="(trackItem, index) in playList.tracks.items"
        :track="trackItem.track"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch } from "vue";
import { computed, ComputedRef } from "@vue/reactivity";

import { useSpotifyStore } from "@/store/spotify";

import Track from "@/components/Spotify/Track.vue";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";

// global
const spotifyStore = useSpotifyStore();

// computed
const playerActive = computed(() => spotifyStore.playerActive); // doestn't work properly
const spotifyPlayer = computed(() => spotifyStore.spotifyPlayer);
const playList: ComputedRef<any> = computed(() => spotifyStore.playList);

// watchers
watch(playerActive, async (newValue: boolean) => {
  if (!newValue) {
    return;
  }

  const currentState = await spotifyPlayer.value.getCurrentState();
  console.log(currentState.context);
  if (currentState.context.uri.match(new RegExp("spotify:playlist.*"))) {
    const responsePlaylist = await SpotifyHttpService.getCurrentPlaylist(
      currentState.context.uri.split(":")[2],
    );

    console.log(responsePlaylist);
    spotifyStore.playList = responsePlaylist;
  }
});
</script>
