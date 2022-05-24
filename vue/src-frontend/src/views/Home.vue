<template>
  <div class="row m-0">
    <div
      class="col-md-6 col-lg-4"
      v-for="(app, index) in apps"
      :key="index"
    >
      <Card class="m-2">
        <template #header>
          <img
            class="image-size mt-2"
            :alt="`${app.name} icon`"
            :src="app.image"
          />
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

<script lang="ts">
import { App } from "@/interfaces/baseInterfaces";

import spotifyImgUrl from "@/assets/images/spotify-icon.png";
import excelImgUrl from "@/assets/images/excel-icon.png";

import { defineComponent } from "vue";
import { useRouter, Router } from 'vue-router'

import Card from "primevue/card";
import Button from "primevue/button";

export default defineComponent({
  name: "Home",
  components: { Card, Button },
  setup(){
    const router: Router = useRouter();

    const apps: App[] = [
      {
        name: "Spotify",
        url: "/spotify/player",
        image: spotifyImgUrl,
      },
      {
        name: "Excel",
        url: "/excel",
        image: excelImgUrl,
      },
    ]

    const goTo = function(url: string){
      router.push({path: url});
    }

    return {
      //attr
      apps,
      //metthods
      goTo
    };
  },
});
</script>

<style scoped>
.image-size {
  max-width: 100px;
  max-height: 100px;
}</style>