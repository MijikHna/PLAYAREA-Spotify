<template>
  <div class="my-1">
    <div class="d-flex justify-content-end">
      <Button v-if="!loggedIn" icon="pi pi-lock" label="Login" class="p-button-sm" @click="loginToSpotify">
        Login To Spotify
      </Button>
      <Button v-if="loggedIn" icon="pi pi-lock" label="Login" class="p-button-sm" @click="logoutFromSpotify">
        Logout From Spotify
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, SpotifyState } from "vue";
import { computed, ComputedRef } from "@vue/reactivity";

import { storeToRefs } from "pinia";
import { AxiosResponse } from "axios";

import Button from "primevue/button";
import { useToast } from "primevue/usetoast";
import { ToastServiceMethods } from "primevue/toastservice";

import { BackendHttpService } from "@/services/BackendHttpService";
import { useSpotifyStore } from "@/store/spotify";


//global
const spotifyStore = useSpotifyStore();
const toast: ToastServiceMethods = useToast();
const { loggedIn, spotifyPlayer }: Partial<SpotifyState> = storeToRefs(spotifyStore);

//data
// methods
const loginToSpotify = async function (): Promise<void> {
  // TODO: try-catch + Toaster
  const response = await BackendHttpService.http.get('/spotify/login')
  console.log(response.data);

  if (response.status === 200) window.location.href = response.data.url;
};

const logoutFromSpotify = async function (): Promise<void> {
  try {
    const response: AxiosResponse =
      await BackendHttpService.http.delete('/spotify/logout');

    if (response.status === 202) {
      loggedIn.value = false;
      spotifyPlayer.value.disconnect();

      spotifyStore.resetSpotifyPlayer();

      BackendHttpService.http.defaults.headers.common["Authorization"] = "";

      toast.add({
        severity: "success",
        summary: `Spotify Logout`,
        detail: `You has been logged out from Spotify`,
        life: 5000,
      });
    }
  } catch (e) {
    console.error(e);

    toast.add({
      severity: "error",
      summary: `Spotify Logout`,
      detail: `You hasn't been logged out from Spotify`,
      life: 5000,
    });
  }
};
</script>

<style>
@keyframes p-progress-spinner-color {

  100%,
  0% {
    stroke: #ffa700;
  }

  40% {
    stroke: #ffa700;
  }

  66% {
    stroke: #ffa700;
  }

  80%,
  90% {
    stroke: #ffa700;
  }
}
</style>
