<template>
  <div>
    <Card class="p-0">
      <template #header>
        <img alt="user header" style="width: 100%" :src="artist.images[0].url" />
      </template>
      <template #title> {{ artist.name }} </template>
      <template #subtitle> Popularity: {{ artist.popularity }} </template>
      <template #content>
        <p class="m-0">
          Genres: <span v-for="(genre, index) in artist.genres" :key="index">{{ genre }},</span> <br />
          Popularity: <span> {{ artist.popularity }} </span> <br />
          Followers: <span> {{ artist.followers.total }} </span> <br />
        </p>
      </template>
      <template #footer>
        <Button icon="pi pi-play" label="Play" @click="play" />
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import Card from 'primevue/card';
import Button from 'primevue/button';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';

// props
const props = defineProps<{ artist: any }>();

// methods
const play = async () => {
  // NOTE: maybe chech if player is selected
  const response = await SpotifyHttpService.http.put(
    `me/player/play`,
    {
      context_uri: props.artist.uri,
      offset: { position: 0 },
      position_ms: 0,
    },
  );
};
</script>
