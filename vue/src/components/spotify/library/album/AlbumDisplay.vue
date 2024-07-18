<template>
  <div class="grid grid-cols-5 gap-4">
    <Album 
      :album="album.album" 
      v-for="(album, index) in albums" 
      :key="index" 
    />
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue';

import Album from './Album.vue';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// data 
const albums: Ref<any[]> = ref<any[]>([]);

onMounted(async () => {
  await getAlbums();
});

// methods
const getAlbums = async () => {
  try {
    const response = await SpotifyHttpService.http.get('me/albums');

    if (response.status !== 200) throw new Error('Could not get albums');
    albums.value = response.data.items;
  } catch (error) {
    console.error(error);
  }
}
</script>
