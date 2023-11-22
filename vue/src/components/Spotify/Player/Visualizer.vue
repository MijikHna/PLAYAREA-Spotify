<template>
  <div class="flex justify-content-center flex-wrap mt-4" v-if="currentTrack">
    <Card class="flex m-2">
      <template #header>
        <img alt="user header" :src="currentTrack.album.images[0].url" style="height: 250px" />
      </template>
      <template #title> {{ currentTrack.name }} </template>
      <template #content>
        <p class="m-0">
        </p>
      </template>
      <template #footer>
        <Button icon="pi pi-angle-double-right" label="Go to Album" />
      </template>
    </Card>

    <Card class="flex m-2" v-for="(artist, index) in artistsWithInfo" :key="index">
      <template #header>
        <img alt="user header" :src="artist.image" style="width: 250px" />
      </template>
      <template #title> {{ artist.name }} </template>
      <template #content>
        <p class="m-0">
          Genres: <span v-for="(genre, index) in artist.genres" :key="index">{{ genre }},</span> <br />
          Popularity: <span> {{ artist.popularity }} </span> <br />
          Followers: <span> {{ artist.followers }} </span> <br />
        </p>
      </template>
      <template #footer>
        <Button icon="pi pi-angle-double-right" label="Go to Artist" />
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { Ref, ref, watch } from 'vue';
import { storeToRefs } from 'pinia';

import Card from 'primevue/card';
import Button from 'primevue/button';


import { useSpotifyStore, SpotifyState } from '@/store/spotify';
import { SpotifyHttpService } from '@/services/SpotifyHttpService';
// global
const spotifyStore = useSpotifyStore();
const artistsWithInfo: Ref<any[]> = ref([]);
// data 
const { currentTrack, nextTracks } = storeToRefs(spotifyStore);

// computed
watch(
  () => currentTrack?.value?.artists, async (newValue, oldValue) => {
    artistsWithInfo.value = await Promise.all(newValue.map(async (artist: any) => {
      return {
        name: artist.name,
        ...(await getArtistInfo(artist)),
      }
    }));
  },
);

const getArtistInfo = async (artist: any) => {
  try {
    const response = await SpotifyHttpService.http.get(`artists/${artist.uri.split(":")[2]}`);
    return {
      followers: response.data.followers.total,
      genres: response.data.genres,
      popularity: response.data.popularity,
      image: response.data.images[0].url,
    };
  } catch (error) {
    console.log(artist);
    console.log(error);

  }
}

</script>

<style scoped></style>
