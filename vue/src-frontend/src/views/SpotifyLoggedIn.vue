<template>
  <div class="container">
    <div class="row full-height">
      <div class="col d-flex justify-content-center align-items-center">
        <Card>
          <template #header>
            <img
              :src="imagePic"
              alt="Spotify Picture"
              style="max-height: 500px;"
            >
          </template>
          <template #title>
            Spotify Login
          </template>
          <template #content>
            You have successfully logged in to your Spotify account. Enjoy the app!!!
          </template>
          <template #footer>
            <ProgressBar mode="indeterminate"/>
          </template>
        </Card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import spotifyImgUrl from "@/assets/images/spotify.jpg";
import { onMounted } from "vue";

import Card from 'primevue/card';
import ProgressBar from 'primevue/progressbar'
import { Router, useRouter } from "vue-router";

//global
const router: Router = useRouter();

//data
const imagePic = spotifyImgUrl;

onMounted(() => {
  setTimeout(() => {
    router.push({name: 'player'});
  }, 3000);
});
</script>