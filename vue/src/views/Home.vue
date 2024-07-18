<template>
  <div class="min-w-full min-h-full m-0 p-2 flex justify-center">
    <div class="grid grid-cols-1 grid-rows-1">

      <Card class="self-center">
        <template #header >
          <div class="flex justify-center">
            <img class="image-size mt-2 justify-center" alt="Spotify icon" :src="spotifyImgUrl" />
          </div>
        </template>
        <template #title> Spotify </template>
        <template #content>
          Here you can explore the Spotify application.<br />
          Try it out!!!
        </template>
        <template #footer>
          <Button icon="pi pi-sign-in" label="Login to Spotify" @click="loginToSpotify" />
          <!-- <Button icon="pi pi-sign-in" label="Login to Spotify" @click="loginToSpotify" /> -->
        </template>
      </Card>
    </div>
    </div>
</template>

<script setup lang="ts">
import { Router, useRouter } from "vue-router";

import Button from "primevue/button";
import Card from "primevue/card";

import { useToast } from "primevue/usetoast";
import { ToastServiceMethods } from "primevue/toastservice";

import spotifyImgUrl from "@/assets/images/spotify-icon.png";

import { BackendHttpService } from "@/services/BackendHttpService";

// global data
const toast: ToastServiceMethods = useToast();

const loginToSpotify = async function (): Promise<void> {
  try {
    const response = await BackendHttpService.http.get("/spotify/login");

    if (response.status === 200) window.location.href = response.data.url;
  } catch (error) {
    toast.add({
      severity: "error",
      summary: "Spotify Login",
      detail: "An error occurred while trying to login to Spotify",
      life: 5000,
    });
  }
};

</script>

<style scoped>
.image-size {
  max-width: 100px;
  max-height: 100px;
}
</style>
