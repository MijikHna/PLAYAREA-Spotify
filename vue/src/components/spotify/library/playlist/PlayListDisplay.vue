<template>
  <div class="grid grid-cols-5 gap-4">
    <Playlist 
      :playList="playList" 
      v-for="(playList, index) in playLists" 
      :key="index" 
      class="block place-self-stretch" />
  </div>
</template>

<script setup lang="ts">
  import { Ref, onMounted, ref } from "vue";

  import { AxiosResponse } from "axios";

  import Playlist from "./Playlist.vue";

  import { SpotifyHttpService } from "@/services/SpotifyHttpService";

  // data
  // FIXME: define playlist Response and App types
  const playLists: Ref<any[]> = ref([]);

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
    playLists.value = response.data.items
  };
</script>
