<template>
  <Splitter class="spotify-player-height rounded-0">
    <SplitterPanel class="current-playing" :size="30" :minSize="10">
        <TrackList />
    </SplitterPanel>
    <SplitterPanel class="current-playlist" :size="70" :minSize="50">
      <Control />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
import { computed, onMounted } from "vue";
import { Store, useStore } from 'vuex';

import Splitter from "primevue/splitter";
import SplitterPanel from "primevue/splitterpanel";

import { ToastServiceMethods } from "primevue/toastservice";
import { useToast } from "primevue/usetoast";

import { ITrack, ITrackList } from "@/interfaces/spotifyInterfaces";
import { BackendHttpService } from "@/services/BackendHttpService";

import Control from "@/components/Spotify/Control.vue";
import TrackList from "@/components/Spotify/TrackList.vue";

import { AxiosResponse } from "axios";

//global
const store: Store<any> = useStore()
const toast: ToastServiceMethods = useToast();
 //computed
const spotifyAuthSuccess = computed(() => store.getters.getSpotifyAuthSuccess);
let spotifyPlayerSDKDOMElem: HTMLElement|null = computed(() => store.state.spotify.spotifyPlayerSDKDOMElem);
let spotifyPlayer: any = computed(() => store.state.spotify.spotifyPlayer);
let currentTrack: ITrack = computed(() => store.state.spotify.currentTrack);
let trackList: ITrackList = computed(() => store.state.spotify.trackList);

onMounted(async () => {
  await initSpotifyPlayer();
});

const initSpotifyPlayer = async function(){
  if (spotifyPlayer.value) {
    return;
  }

  let tokenResponse: AxiosResponse;
  try {
    tokenResponse  = await BackendHttpService.getSavedSpotifyToken();

    if (tokenResponse.status === 200){
      store.commit('setSpotifyAuthSuccess', true);
    }
  }catch(e){
    return;
  }

  const spotifyPlayerSDKDOMElemTemp = document.createElement("script");
  spotifyPlayerSDKDOMElemTemp.setAttribute(
    "src",
    "https://sdk.scdn.co/spotify-player.js"
  );
  spotifyPlayerSDKDOMElemTemp.setAttribute("defer", "true");
  document.head.appendChild(spotifyPlayerSDKDOMElemTemp);
  store.commit("setSpotifyPlayerDOMElem", spotifyPlayerSDKDOMElemTemp);

  window.onSpotifyWebPlaybackSDKReady = () => {
    const spotifyPlayerTemp = new window.Spotify.Player({
      name: "Playarea2 Web Playback SDK",
      getOAuthToken: async (cb) => {
        const response = await BackendHttpService.getSavedSpotifyToken()
        cb(response.data.token);
      },
      volume: 0.5,
    });

    spotifyPlayerTemp.addListener("ready", ({ device_id }) => {
      toast.add({
        severity: 'success',
        summary: 'Spotify Player',
        detail: 'Spotify Player is ready',
        life: 5000,
      });
    });

    spotifyPlayerTemp.addListener("not_ready", ({ device_id }) => {
      // Toaster Message
      console.log("Device ID has gone offline");
    });

    spotifyPlayerTemp.addListener(
      'player_state_changed',
      (
        // {track_window: {current_track, next_tracks } = null}
        state: any = null
      ) => {
        console.log(state)

        if (state === null) {
          store.commit('setPlayList', null);
          store.commit('setPlayingContext', null);
          store.commit("setThisPlayerActive", false);
          store.commit('setCurrentTrack', null);
          store.commit('setNextTracks', null);

          return;
        }

        // if (!state?.track_window?.current_track || !state.track_window.next_tracks) {
        //   return;
        // }

        store.commit("setThisPlayerActive", true);
        store.commit('setCurrentTrack', state.track_window.current_track);
        store.commit('setNextTracks', state.track_window.next_tracks);
        store.commit('setPlayingContext', state);
      }
    );

    spotifyPlayerTemp.connect();

    store.commit("setSpotifyPlayer", spotifyPlayerTemp);
  };
}
</script>

<style scoped lang="css">
::v-deep(.tabmenudemo-content) {
    padding: 2rem 1rem;
}
.current-playing {
  overflow-y: auto;
  max-height: 25%;
}

.current-playlist {
  overflow-y: auto;
  max-height: 25%;
}
</style>
