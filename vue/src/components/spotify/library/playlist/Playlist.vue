<template>
    <SpotifyCard>
      <template #header-image>
        <img :alt="playList.name" style="width: 100%" :src="playList.images[0].url" />
      </template>
      <template #default> 
        <div class="flex flex-col justify-around">
          <div class="text-base my-1">{{ playList.name }} </div>
          <div class="text-base font-semibold text-lg my-1"> {{ playList.owner.display_name }} </div>
          <div v-if="playList.description">
            <p class="m-0 text-sm"> {{ playList.description }}</p>
          </div>
        </div>
      </template>
      <template #footer>
        <Button icon="pi" label="Play" @click="play">
          <FontAwesomeIcon :icon="faPlay" /> 
        </Button>
      </template>
    </SpotifyCard>
</template>

<script setup lang="ts">
import SpotifyCard from "@/components/common/layout/SpotifyCard.vue";
import Button from 'primevue/button';
import { SpotifyHttpService } from '@/services/SpotifyHttpService';
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faPlay } from "@fortawesome/free-solid-svg-icons"

// props
const props = defineProps<{ playList: any }>();

// methods
const play = async () => {
  // NOTE: maybe check if player is selected
  // FIXME: define playListResponse and App types
  const response = await SpotifyHttpService.http.put(
    `me/player/play`,
    {
      context_uri: props.playList.uri,
      offset: { position: 0 },
      position_ms: 0,
    },
  );

  // TODO: ...

};
</script>
