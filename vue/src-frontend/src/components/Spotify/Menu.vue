<template>
  <div class="my-1">
    <div class="d-flex justify-content-end">
      <Button
        v-if="!spotifyAuthSuccess"
        icon="pi pi-lock"
        label="Login"
        class="p-button-sm"
        @click="loginToSpotify"
      >
        <ProgressSpinner
          v-if="loginInToSpotify"
          strokeWidth="8"
          style="width: 20px; height: 20px"
          class="me-2"
        />
        Login To Spotify
      </Button>
      <Button
        v-if="spotifyAuthSuccess"
        icon="pi pi-lock"
        label="Login"
        class="p-button-sm"
        @click="logoutFromSpotify"
      >
        Logout From Spotify
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from "vue";
import { computed, ComputedRef } from "@vue/reactivity";

import { useSpotifyStore } from "@/store/spotify";

import Button from "primevue/button";
import ProgressSpinner from "primevue/progressspinner";
import { useToast } from "primevue/usetoast";
import { ToastServiceMethods } from "primevue/toastservice";

import { AxiosResponse } from "axios";

import { BackendHttpService } from "@/services/BackendHttpService";

//global
const spotifyStore = useSpotifyStore();
const toast: ToastServiceMethods = useToast();

//data
const loginInToSpotify: Ref<boolean> = ref<boolean>(false);

// computed
const spotifyAuthSuccess: ComputedRef<boolean> = computed(
  () => spotifyStore.spotifyAuthSuccess,
);

// methods
const loginToSpotify = async function (): Promise<void> {
  // TODO: try-catch + Toaster
  loginInToSpotify.value = true;

  const response = await BackendHttpService.loginToSpotify();

  if (response.status === 200) {
    window.location.href = response.data.url;

    loginInToSpotify.value = false;
    return;
  }

  loginInToSpotify.value = false;
};

const logoutFromSpotify = async function (): Promise<void> {
  try {
    const response: AxiosResponse =
      await BackendHttpService.logOutFromSpotify();

    if (response.status === 202) {
      spotifyStore.spotifyPlayer.disconnect();

      spotifyStore.resetSpotifyPlayer();

      toast.add({
        severity: "success",
        summary: `Spotify Logout`,
        detail: `You has been logged out from Spotify`,
        life: 5000,
      });
    }
  } catch (e) {
    toast.add({
      severity: "error",
      summary: `Spotify Logout`,
      detail: `You hasn;t been logged out from Spotify`,
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
