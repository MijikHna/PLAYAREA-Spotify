<template>
  <div class="grid m-0 p-2">
    <PlayList :playList="playList" v-for="(playList, index) in playLists.items" :key="index"
      class="col-12 md:col-6 lg:col-3" />
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from 'vue';

import { AxiosResponse } from 'axios';

import PlayList from './PlayList.vue';

import { PlayListsResponse } from '@/types/spotify/playlist.types';
import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// data
const playLists: Ref<PlayListsResponse[]> = ref([]);

onMounted(async () => {
  await getUsersPlaylists();
});

// methods
const getUsersPlaylists = async () => {
  let response: AxiosResponse;
  try {
    response = await SpotifyHttpService.http.get("me/playlists");
  } catch (error) {
    console.log(error);
  }
  playLists.value = response.data as PlayListsResponse[];
}


</script>
