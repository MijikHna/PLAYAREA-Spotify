<template>
  <div class="grid m-0 p-2">
    <Artist :artist="artist" v-for="(artist, index) in artists.items" :key="index" class="col-12 md:col-6 lg:col-3" />
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue';

import Artist from './Artist.vue';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// data 
const artists: Ref<any> = ref<any>([]);

onMounted(async () => {
  await getUserArtists();
});

// methods
const getUserArtists = async () => {
  try {
    const response = await SpotifyHttpService.http.get('me/following?type=artist');

    if (response.status !== 200) throw new Error('Could not get albums');
    artists.value = response.data.artists;
  } catch (error) {
    console.error(error);
  }
}
</script>
