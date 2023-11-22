<template>
  <Splitter class="spotify-player-height rounded-0">
    <SplitterPanel class="current-playing" :size="30" :minSize="10">
      <ScrollPanel>
        <PlayingContext />
      </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="current-playlist" :size="70" :minSize="50">
      <Control />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
import { useSpotifyStore } from "@/store/spotify";
import { Ref, SpotifyState, onMounted } from "vue";
import { AxiosResponse } from "axios";

import ScrollPanel from "primevue/scrollpanel";
import Splitter from "primevue/splitter";
import SplitterPanel from "primevue/splitterpanel";

import { ToastServiceMethods } from "primevue/toastservice";
import { useToast } from "primevue/usetoast";

import { BackendHttpService } from "@/services/BackendHttpService";
import { SpotifyWindow } from "@/types/spotify/app.types";

import Control from "@/components/Spotify/Player/Control.vue";
import PlayingContext from "@/components/Spotify/Player/PlayingContext.vue";
import { storeToRefs } from "pinia";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";

//global
const spotifyStore = useSpotifyStore();
const { loggedIn, spotifyPlayer, spotifyPlayerDOMElem }:
  Partial<SpotifyState> = storeToRefs(spotifyStore);
const toast: ToastServiceMethods = useToast();

const spotifyWindow: SpotifyWindow = window as unknown as SpotifyWindow;

onMounted(async () => await initSpotifyPlayer());

const initSpotifyPlayer = async function () {
  if (spotifyPlayer.value) return;

  const spotifyPlayerSDKDOMElemTemp = document.createElement("script");

  spotifyPlayerSDKDOMElemTemp.setAttribute("src", "https://sdk.scdn.co/spotify-player.js");
  spotifyPlayerSDKDOMElemTemp.setAttribute("defer", "true");

  document.head.appendChild(spotifyPlayerSDKDOMElemTemp);

  spotifyPlayerDOMElem.value = spotifyPlayerSDKDOMElemTemp;

  let response: AxiosResponse;
  try {
    response = await BackendHttpService.http.get("/spotify/get-token");
  } catch (error) {
    console.error(error);
    return;
  }
  const token: string = response.data.token;
  SpotifyHttpService.http.defaults.headers.common["Authorization"] = `Bearer ${token}`;

  spotifyWindow.onSpotifyWebPlaybackSDKReady = () => {
    spotifyPlayer.value = new spotifyWindow.Spotify.Player({
      name: "Playarea2 Web Playback",
      getOAuthToken: (callback: (token: string) => void) => {
        console.log("Getting OAuth Token");
        callback(token);
      },
      volume: 0.5,
    });

    spotifyPlayer.value.addListener("ready", ({ device_id }) => {
      loggedIn.value = true;

      toast.add({
        severity: "success",
        summary: "Spotify Player",
        detail: "Spotify Player is ready",
        life: 5000,
      });
    });

    spotifyPlayer.value.addListener("not_ready", ({ device_id }) => {
      // Toaster Message
      console.log("Device ID has gone offline");
    });

    spotifyPlayer.value.addListener(
      "player_state_changed",
      (
        // {track_window: {current_track, next_tracks } = null}
        state: any = null,
      ) => {
        console.log(state);

        if (state === null) {
          spotifyStore.activePlayList = null;
          spotifyStore.playingContext = null;
          spotifyStore.playerActive = false;
          spotifyStore.currentTrack = null;
          spotifyStore.nextTracks = [];

          return;
        }

        //TODO: grab properly current Track: current duration-postion and paused state
        spotifyStore.playerActive = true;
        spotifyStore.currentTrack = state.track_window.current_track;
        spotifyStore.nextTracks = state.track_window.next_tracks;
        spotifyStore.playingContext = state;
      },
    );

    spotifyStore.spotifyPlayer.connect();
  };
};
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

.spotify-player-height {
  min-height: calc(100vh - 56px - 56px - 45px - 44px);
  max-height: calc(100vh - 56px - 56px - 45px - 44px);
}
</style>
