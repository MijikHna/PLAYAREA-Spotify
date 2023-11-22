<template>
  <div class="grid m-0 p-2">
    <Album :album="album" v-for="(album, index) in albums.items" :key="index" class="col-12 md:col-6 lg:col-4" />
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue';

import Album from './Album.vue';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// data 
const albums: Ref<any> = ref<any>([]);

onMounted(async () => {
  await getAlbums();
});

// methods
const getAlbums = async () => {
  try {
    const response = await SpotifyHttpService.http.get('me/albums');

    if (response.status !== 200) throw new Error('Could not get albums');
    albums.value = response.data;
  } catch (error) {
    console.error(error);
  }
}
</script>
