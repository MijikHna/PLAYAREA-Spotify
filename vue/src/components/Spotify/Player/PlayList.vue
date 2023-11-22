<template>
  <div class="container px-3 playlist-height">
    <div class="row" v-if="playerActive && activePlayList">
      <Track v-for="(trackItem, index) in activePlayList.items" :track="trackItem.track" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, watch } from "vue";
import { storeToRefs } from "pinia";

import { useSpotifyStore } from "@/store/spotify";

import Track from "@/components/Spotify/Track.vue";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";

// global
const spotifyStore = useSpotifyStore();

// store data
const { playerActive, spotifyPlayer, activePlayList } = storeToRefs(spotifyStore);

// watchers
watch(playerActive, async (newValue: boolean) => {
  if (!newValue) return;

  const currentState = await spotifyPlayer.value.getCurrentState();

  if (currentState.context.uri.match(new RegExp("spotify:playlist.*"))) {
    // TODO: try-catch
    const response = await SpotifyHttpService.http.get(`/playlists/${currentState.context.uri.split(":")[2]}/tracks`,
    );

    const responsePlaylist = response.data;

    activePlayList.value = responsePlaylist;
  }
});
</script>
