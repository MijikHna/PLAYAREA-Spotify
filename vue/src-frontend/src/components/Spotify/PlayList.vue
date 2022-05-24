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
import { watch } from 'vue';
import { computed, ComputedRef } from "@vue/reactivity";
import { Store, useStore } from "vuex";

import Track from "@/components/Spotify/Track.vue";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";

// global
const store: Store<any> = useStore();

// computed
const playerActive = computed(() => store.state.spotify.thisPlayerActive); // doestn't work properly
const spotifyPlayer = computed(() => store.state.spotify.spotifyPlayer);
const playList: ComputedRef<any> = computed(() => store.state.spotify.playList);

// watchers
watch (
  playerActive,
  async (newValue: boolean) => {
    if (!newValue) {
      return;
    }

    const currentState =  await spotifyPlayer.value.getCurrentState();
    console.log(currentState.context);
    if (currentState.context.uri.match(new RegExp('spotify:playlist.*'))){

      const responsePlaylist = await SpotifyHttpService.getCurrentPlaylist(currentState.context.uri.split(':')[2]);

      console.log(responsePlaylist);
      store.commit('setPlayList', responsePlaylist)
    }
  }
);
</script>