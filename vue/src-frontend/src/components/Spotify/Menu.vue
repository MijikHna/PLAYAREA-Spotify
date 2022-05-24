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
            v-if="logginInToSpotify"
            strokeWidth="8"
            style="width:20px;height:20px"
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
import { ref, Ref } from 'vue';
import { useStore, Store } from "vuex";
import { computed } from "@vue/reactivity";

import Button from "primevue/button";
import ProgressSpinner from 'primevue/progressspinner';

import { useToast } from 'primevue/usetoast';
import { ToastServiceMethods } from "primevue/toastservice";

import { AxiosResponse } from "axios";

import { BackendHttpService } from "@/services/BackendHttpService";

//global
const store: Store<any> = useStore();
const toast: ToastServiceMethods = useToast();

//data
const logginInToSpotify: Ref<boolean> =  ref<boolean>(false);

// computed
const spotifyAuthSuccess = computed(() => store.getters.getSpotifyAuthSuccess);

// methods
const loginToSpotify = async function(){
  // TODO: try-catch + Toaster
  logginInToSpotify.value = true;


  const response = await BackendHttpService.loginToSpotify();

  if (response.status === 200) {
    window.location.href = response.data.url;

    logginInToSpotify.value = false;
    return;
  }

  logginInToSpotify.value = false;
}

const logoutFromSpotify = async function(): Promise<void> {
  try {
    const response: AxiosResponse = await BackendHttpService.lougOutFromSpotify();


    if (response.status === 202) {
      const spotifyPlayer = store.state.spotify.spotifyPlayer;
      spotifyPlayer.disconnect();

      store.dispatch('resetSpotifyPlayer');

      toast.add({
        severity: 'success',
        summary: `Spotify Logout`,
        detail: `You has been logged out from Spotify`,
        life: 5000,
      });
    }
  }
  catch(e){
    toast.add({
      severity: 'error',
      summary: `Spotify Logout`,
      detail: `You hasn;t been logged out from Spotify`,
      life: 5000,
    });
  }
}
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