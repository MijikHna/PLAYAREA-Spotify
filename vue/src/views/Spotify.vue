<template>
  <div class="col-12 p-0">
    <Menu />
    <div class="flex">
      <TabMenu :model="tabMenuItems" @tabChange="handleTabChange" />
    </div>
    <router-view v-slot="{ Component }">
      <KeepAlive>
        <component :is="Component" />
      </KeepAlive>
    </router-view>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, onMounted } from "vue";
import { AxiosResponse } from "axios";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

import { useToast } from "primevue/usetoast";
import TabMenu, { TabMenuChangeEvent } from 'primevue/tabmenu';
import { ToastServiceMethods } from "primevue/toastservice";
import { useSpotifyStore } from "@/store/spotify";

import { BackendHttpService } from "@/services/BackendHttpService";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";
import { SpotifyTabMenuItem } from "@/types/spotify/app.types";
import { SpotifyWindow } from "@/types/spotify/app.types";

import Menu from "@/components/Spotify/Menu.vue";

//global
const router = useRouter();
const spotifyStore = useSpotifyStore();
const toast: ToastServiceMethods = useToast();

const { loggedIn, spotifyPlayer, spotifyPlayerDOMElem } = storeToRefs(spotifyStore);
const spotifyWindow: SpotifyWindow = window as unknown as SpotifyWindow;
// data

const tabMenuItems: Ref<SpotifyTabMenuItem[]> = ref([
  {
    label: 'Player',
    icon: 'pi pi-volume-up',
    to: 'player',
  },
  {
    label: 'Discover',
    icon: 'pi pi-list',
    to: 'discover',
  },
  {
    label: 'Stats',
    icon: 'pi pi-star',
    to: 'stats',
  }
]);

// methods
const handleTabChange = (e: TabMenuChangeEvent) => {
  router.push({ name: tabMenuItems.value[e.index].to });
}

const initSpotifyPlayer = async function () {
  if (spotifyPlayer.value) return;

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

  spotifyPlayerDOMElem.value = spotifyPlayerSDKDOMElemTemp;

  spotifyWindow.onSpotifyWebPlaybackSDKReady = () => {
    spotifyPlayer.value = new spotifyWindow.Spotify.Player({
      name: "Playarea2 Web Playback",
      getOAuthToken: async (callback: (token: string) => void) => {
        console.log("Getting OAuth Token");
        const response = await BackendHttpService.http.get("/spotify/get-token");
        if (response.status !== 200) throw new Error("Error getting token");

        callback(response.data.token);
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

    spotifyPlayer.value.addListener('initialization_error', ({ message }) => {
      console.error('init', message);
    });

    spotifyPlayer.value.addListener('authentication_error', async ({ message }) => {
      console.error('auth', message);
    });

    spotifyPlayer.value.addListener('account_error', ({ message }) => {
      console.error('account', message);
    });

    spotifyStore.spotifyPlayer.connect();
  };
};

onMounted(async () => await initSpotifyPlayer());
</script>

<style scoped></style>

