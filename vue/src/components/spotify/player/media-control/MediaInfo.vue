<template>
  <div class="flex flex-col">
  <!-- Track: Image, Name -->
      <div class="text-center bg-surface-100 flex flex-row justify-center item-center mb-4 py-3">
        <div class="mx-6">
          <div class="mx-auto">
            <img :src="track.album.images[0].url" :alt="track.name" class="w-28 rounded" />
          </div>
        </div>
        <div class="mx-6 my-auto">{{ track.name }}</div>
      </div>
  <!-- Artists: Image, Name, Genres, Popularity, Followers -->

  <div 
    class="grid gap-5 justify-center" 
    :class="{
      'grid-cols-1': artists.length === 1,
      'grid-cols-2': artists.length === 2,
      'grid-cols-3': artists.length >= 3,
    }">

  <div 
    class="border border-surface-200 dark:border-surface-700 rounded m-2 p-4" 
    v-for="(artist, index) in artists"
    :key="index">
    <div class="mb-4">
      <!-- Image -->
      <div class="relative mx-auto">
        <img
          :src="artist.image"
          :alt="artist.name"
          class="w-48 rounded mx-auto"
        />
      </div>
    </div>
    <!-- Name -->
    <div class="mb-4 font-medium">{{ artist.name }}</div>

    <!-- Genres, Popularity, Followers -->
    <div class="flex justify-between items-center">
      <div class="mt-0 flex flex-col">
        <div v-if="artist?.genres.length">
          <span>Genres: </span> <span>{{ artist.genres.join(", ") }}</span>
        </div>
        <div>
          <span>Popularity: </span> <span>{{ artist.popularity }}</span>
        </div>
        <div>
          <span>Followers: </span> <span>{{ artist.followers }}</span>
        </div>
      </div>
      <span>
        <Button label=" " iconPos="top" class="bg-green-300 m-1">
          <FontAwesomeIcon :icon="faEye" /> 
          <span>Artist</span>
        </Button>
      </span>
    </div>
  </div>
  </div>
  </div>
</template>

<script setup lang="ts">
  import { defineProps, Ref, ref, watch } from "vue";
  import { SpotifyHttpService } from "@/services/SpotifyHttpService";

  import Button from "primevue/button";
    
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
  import { faEye } from "@fortawesome/free-solid-svg-icons";

  const props = defineProps<{
    track: {
      name: string;
      album: { images: { url: string }[] };
      artists: { name: string; uri: string }[];
    };
  }>();

  //data
  const artists: Ref<any[]> = ref([]);

  // computed
  watch(
    () => props.track.artists,
    async (newValue: {name: string, uri: string}[]): Promise<void> => {
      artists.value = await Promise.all(
        newValue.map(async (artist): Promise<any> => {
          return {
            name: artist.name,
            ...(await getArtistInfo(artist)),
          };
        }),
      );
    }
  )
  // functions
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
  };
</script>

<style scoped></style>
