<template>
    <SpotifyCard>
      <template #header-image>
        <img :alt="album.name" style="w-full rounded p-3" :src="album.images[0].url" />
      </template>
      <template #default>
        <div class="flex flex-col">
          <div class="mx-1"> {{ album.name }} </div>
          <div class="mx-1"> Tracks: {{ album.total_tracks }} </div>
        </div>
      </template>
      <template #footer>
        <Button icon="pi pi-play" label="Play" @click="play">
          <FontAwesomeIcon :icon="faPlay" />
        </Button>
      </template>
    </SpotifyCard>
</template>

<script setup lang="ts">
import Button from 'primevue/button';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faPlay } from '@fortawesome/free-solid-svg-icons';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';
import SpotifyCard from '@/components/common/layout/SpotifyCard.vue';

// props
const props = defineProps<{ album: any }>();

// methods
const play = async () => {
  // NOTE: maybe chech if player is selected
  const response = await SpotifyHttpService.http.put(
    `me/player/play`,
    {
      context_uri: props.album.uri,
      offset: { position: 0 },
      position_ms: 0,
    },
  );

  console.log(response);
};
</script>
