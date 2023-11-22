<template>
  <div class="min-w-full m-0 p-2">
    <div class="col-12" v-for="(app, index) in apps" :key="index">
      <Card class="p-m-2">
        <template #header>
          <img class="image-size mt-2" :alt="`${app.name} icon`" :src="app.image" />
        </template>
        <template #title> {{ app.name }}</template>
        <template #content>
          Here you can explore the {{ app.name }} application. <br />
          Try it out!!!
        </template>
        <template #footer>
          <Button icon="pi pi-forward" label="Try" @click="goTo(app.url)" />
        </template>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import Card from "primevue/card";

import { Router, useRouter } from "vue-router";

import { App } from "@/interfaces/baseInterfaces";

import sheetImgUrl from "@/assets/images/sheet-icon.png";
import spotifyImgUrl from "@/assets/images/spotify-icon.png";

const router: Router = useRouter();

const apps: App[] = [
  {
    name: "Spotify",
    url: "/spotify/player",
    image: spotifyImgUrl,
  },
  {
    name: "Sheet",
    url: "/sheet",
    image: sheetImgUrl,
  },
];

const goTo = function (url: string) {
  router.push({ path: url });
};
</script>

<style scoped>
.image-size {
  max-width: 100px;
  max-height: 100px;
}
</style>
