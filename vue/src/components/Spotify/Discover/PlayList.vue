<template>
  <div>
    <Card class="p-0">
      <template #header>
        <img alt="user header" style="width: 100%" :src="playList.images[0].url" />
      </template>
      <template #title> {{ playList.name }} </template>
      <template #subtitle> {{ playList.owner.display_name }} </template>
      <template #content v-if="playList.description">
        <p class="m-0"> {{ playList.description }}</p>
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

import { PlayListResponse } from '@/types/spotify/playlist.types';
import { SpotifyHttpService } from '@/services/SpotifyHttpService';


// props
const props = defineProps<{ playList: PlayListResponse }>();

// methods
const play = async () => {
  // NOTE: maybe chech if player is selected
  const response = await SpotifyHttpService.http.put(
    `me/player/play`,
    {
      context_uri: props.playList.uri,
      offset: { position: 0 },
      position_ms: 0,
    },
  );
};
</script>
