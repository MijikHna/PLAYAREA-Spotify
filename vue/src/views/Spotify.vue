<template>
    <router-view v-slot="{ Component }">
      <KeepAlive :include="['Player']">
        <component :is="Component" />
      </KeepAlive>
    </router-view>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { AxiosResponse } from "axios";
import { storeToRefs } from "pinia";


import { useToast } from "primevue/usetoast";
import { ToastServiceMethods } from "primevue/toastservice";
import { useSpotifyStore } from "@/store/spotify";
import { useUserStore } from "@/store/user";

import { useRouter } from "vue-router";

import { BackendHttpService } from "@/services/BackendHttpService";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";
import { onBeforeRouteUpdate } from "vue-router";
import { UtilsService } from "@/services/UtilsService";
import { DecodedUserToken, UserToken } from "@/types/auth.types";

//global
const spotifyStore = useSpotifyStore();
const userStore = useUserStore();
const router = useRouter();

const toast: ToastServiceMethods = useToast();

const { dom, auth, player } = storeToRefs(spotifyStore);
const spotifyWindow: Window = window

// methods
const initSpotifyPlayer = async function () {
  if (dom.value.spotifyPlayer) return;

  let response: AxiosResponse;
  try {
    response = await BackendHttpService.http.get("/spotify/get-token");

  } catch (error) {
    console.error(error);
    return;
  }
  let token: string = response.data.token;

  if (!token) return;

  SpotifyHttpService.http.defaults.headers.common["Authorization"] = `Bearer ${token}`;

  const spotifyPlayerSDKDOMElemTemp = document.createElement("script");

  spotifyPlayerSDKDOMElemTemp.setAttribute("src", "https://sdk.scdn.co/spotify-player.js");
  spotifyPlayerSDKDOMElemTemp.setAttribute("defer", "true");

  document.head.appendChild(spotifyPlayerSDKDOMElemTemp);

  dom.value.spotifyPlayerDOMElem = spotifyPlayerSDKDOMElemTemp;

  spotifyWindow.onSpotifyWebPlaybackSDKReady = () => {
    dom.value.spotifyPlayer = new spotifyWindow.Spotify.Player({
      name: "Playarea2 Web Playback",
      getOAuthToken: async (callback: (token: string) => void) => {
        console.log("Getting OAuth Token");
        const response = await BackendHttpService.http.get("/spotify/get-token");
        if (response.status !== 200) throw new Error("Error getting token");

        callback(response.data.token);
      },
      volume: 0.5,

    });

    dom.value.spotifyPlayer.addListener("ready", ({ device_id }) => {
      auth.value.loggedIn = true;

      toast.add({
        severity: "success",
        summary: "Spotify Player",
        detail: "Spotify Player is ready",
        life: 5000,
      });
    });

    dom.value.spotifyPlayer.addListener("not_ready", ({ device_id }) => {
      // Toaster Message
      console.log("Device ID has gone offline");
    });

    dom.value.spotifyPlayer.addListener(
      "player_state_changed",
      (
        // {track_window: {current_track, next_tracks } = null}
        state: any = null,
      ) => {
        console.log(state);

        if (state === null) {
          player.value.activePlayList = null;
          player.value.playingContext = null;
          player.value.playerActive = false;
          player.value.currentTrack = null;
          player.value.nextTracks = [];

          return;
        }

        //TODO: grab properly current Track: current duration-postion and paused state
        player.value.playerActive = true;
        player.value.currentTrack = state.track_window.current_track;
        player.value.nextTracks = state.track_window.next_tracks;
        player.value.playingContext = state;
      },
    );

    dom.value.spotifyPlayer.addListener('initialization_error', ({ message }) => {
      console.error('init', message);
    });

    dom.value.spotifyPlayer.addListener('authentication_error', async ({ message }) => {
      console.error('auth', message);
    });

    dom.value.spotifyPlayer.addListener('account_error', ({ message }) => {
      console.error('account', message);
    });

    dom.value.spotifyPlayer.connect();
  };
};

onMounted(async () => { 
  await initSpotifyPlayer()

    if (!spotifyStore.auth?.loggedIn) {
    { name: "home" };
    }
    
    if (!userStore.user) {
      const userTokenInfo: DecodedUserToken  = UtilsService.decodeCookieToken("Authorization");

      const profileResponse = await BackendHttpService.http.get(`/users/profile/${userTokenInfo.id}`);

      if (profileResponse.status === 200) {
        userStore.setUser({
          id: userTokenInfo.id,
          email: userTokenInfo.user_identifier,
          profile: profileResponse.data
        });
      }
    
    }

});

  // hooks
onBeforeRouteUpdate(async (to) => {
    // NOTE: maybe also check spotify token
    if (!spotifyStore.auth?.loggedIn) {
      if (to.name === "home") return;
      return router.push({ name: "home" });
    }
    
    if (!userStore.user) {
      const userTokenInfo: DecodedUserToken  = UtilsService.decodeCookieToken("Authorization");

      const profileResponse = await BackendHttpService.http.get(`/users/profile/${userTokenInfo.id}`);

      if (profileResponse.status === 200) {
        userStore.setUser({
          id: userTokenInfo.id,
          email: userTokenInfo.user_identifier,
          profile: profileResponse.data
        });
      }
    
    }
  });


</script>

<style scoped></style>

