<template>
    <li
        :class="['p-1 hover:bg-surface-100 hover:bg-surface-400 hover:cursor-pointer rounded border border-transparent transition-all transition-duration-200']"
        @click="play"
    >
        <div class="flex flex-wrap justify-between items-center gap-2">
            <div>
            <img class="w-14 shrink-0 rounded" :src="track.album.images[0].url" :alt="track.name" />
            </div>
            <div class="flex flex-col gap-1 text-right">
              <div class="flex truncate justify-end">
                <span class="font-bold inline-block text-nowrap truncate">{{ track.name }}</span>
              </div>
                <div class="flex gap-2 justify-end text-nowrap">
                    <span v-for="(artist, index) in track.artists" :key="index">{{ artist.name }}</span>
                </div>
            </div>
        </div>
    </li>
</template>

<script setup lang="ts">
import { computed, ComputedRef } from "@vue/reactivity";
import { storeToRefs } from "pinia";

import { useSpotifyStore } from "@/store/spotify";


import { TrackResponse } from "@/types/spotify-api-response/track-response.types";
import { calcDuration } from "@/helper/track";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";


const props = defineProps<{ track: TrackResponse }>();

//global
const spotifyStore = useSpotifyStore();

// store data
const { player } = storeToRefs(spotifyStore);

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
    player.value.activePlayList.items.findIndex((item: { track: TrackResponse }) =>
      item.track.id === props.track.id,
    );

  try {
    const response = await SpotifyHttpService.http.put('me/player/play', {
      context_uri: player.value.playingContext.context.uri,
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
</style>
