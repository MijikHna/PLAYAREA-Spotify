<template>
  <div>
    <Card class="p-0">
      <template #header>
        <img alt="user header" style="width: 100%" :src="album.album.images[0].url" />
      </template>
      <template #title> {{ album.album.name }} </template>
      <template #subtitle> {{ album.album.total_tracks }} </template>
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
const props = defineProps<{ album: any }>();

// methods
const play = async () => {
  // NOTE: maybe chech if player is selected
  const response = await SpotifyHttpService.http.put(
    `me/player/play`,
    {
      context_uri: props.album.album.uri,
      offset: { position: 0 },
      position_ms: 0,
    },
  );
};
</script>
