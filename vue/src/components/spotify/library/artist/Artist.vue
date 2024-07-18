<template>
    <SpotifyCard>
      <template #header-image>
        <img :alt="artist.name" style="width: 100%" :src="artist.images[0].url" />
      </template>

      <template #default>
        <div class="flex flex-col">

        </div>
        <div > {{ artist.name }} </div>
        <div > Popularity: {{ artist.popularity }} </div>
        <div >
          <p class="m-0">
          <span> {{ genresStringList }}</span> <br />
          Popularity: <span> {{ artist.popularity }} </span> <br />
          Followers: <span> {{ artist.followers.total }} </span> <br />
          </p>
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
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  import { faPlay } from '@fortawesome/free-solid-svg-icons';
import Button from 'primevue/button';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';
import SpotifyCard from '@/components/common/layout/SpotifyCard.vue';
import { computed } from 'vue';

// props
const props = defineProps<{ artist: any }>();

//computed
const genresStringList = computed(() => props.artist.genres.map((genre: any) => genre).join(", "));
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
