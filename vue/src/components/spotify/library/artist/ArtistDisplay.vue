<template>
  <div class="grid grid-cols-4 gap-4">
    <Artist 
      :artist="artist" 
      v-for="(artist, index) in artists" 
      :key="index" 
      class="block" 
    />
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue';

import Artist from './Artist.vue';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// data 
// TODO: add Response and App aritst type
const artists: Ref<any[]> = ref<any[]>([]);

onMounted(async () => {
  await getUserArtists();
});

// methods
const getUserArtists = async () => {
  try {
    // FIXME: actually should call until no next page
    const response = await SpotifyHttpService.http.get('me/following?type=artist');

    if (response.status !== 200) throw new Error('Could not get albums');
    artists.value = response.data.artists.items;
  } catch (error) {
    console.error(error);
  }
}
</script>
