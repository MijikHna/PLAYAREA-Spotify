<template>
  <Card class="my-2 cursor-pointer" @click="play" v-ripple>
    <template #title> {{ track.name }}</template>
    <template #subtitle>
      <template v-for="(artist, index) in track.artists">
        <span v-if="index !== track.artists.length - 1">{{ artist.name }},
        </span>
        <span v-else>
          {{ artist.name }}
        </span>
      </template>
      <br />
      {{ trackDuration }}
    </template>
  </Card>
</template>

<script setup lang="ts">
import { computed, ComputedRef } from "@vue/reactivity";
import { storeToRefs } from "pinia";

import Card from "primevue/card";

import { useSpotifyStore } from "@/store/spotify";


import { TrackResponse } from "@/types/spotify/track.types";
import { calcDuration } from "@/helper/track";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";


const props = defineProps<{ track: TrackResponse }>();

//global
const spotifyStore = useSpotifyStore();

// store data
const { playingContext, activePlayList } = storeToRefs(spotifyStore);

// computed
const trackDuration: ComputedRef<string> = computed(() => {
  if (!props.track) return "";

  return calcDuration(props.track.duration_ms);
});

// filters
const trimEnd = (value: string) => value.trimEnd();

//methods
const play = async () => {
  const playListPosition =
    activePlayList.value.items.findIndex((item: { track: TrackResponse }) =>
      item.track.id === props.track.id,
    );

  try {
    const response = await SpotifyHttpService.http.put('me/player/play', {
      context_uri: playingContext.value.context.uri,
      offset: {
        position: playListPosition,
      },
      position_ms: 0,
    });
    if (response.status === 204) console.log('Play new: Succuess')
  } catch (e) {
    // Todo
    console.log(e);
  }
};
</script>

<style scoped>
/* override global p-card-content for this component */
>>>.p-card-content {
  padding: 0;
}
</style>
