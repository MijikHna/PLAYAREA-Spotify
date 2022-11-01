<template>
  <div class="flex border clickable" @click="play" v-ripple>
    <div>
      <template v-for="(artist, index) in track.artists">
        <span v-if="index !== track.artists.length - 1"
          >{{ artist.name }},
        </span>
        <span v-else>
          {{ artist.name }}
        </span>
      </template>
      <span> - </span>
      {{ track.name }}
    </div>
    <div>{{ trackDuration }}</div>
  </div>
</template>

<script setup lang="ts">
import { PropType } from "vue";
import { computed, ComputedRef } from "@vue/reactivity";

import { useSpotifyStore } from "@/store/spotify";

import { ITrack } from "@/interfaces/spotifyInterfaces";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";
import { calcDuration } from "@/helper/track";

const props = defineProps({
  track: Object as PropType<ITrack>,
});

//global
const spotifyStore = useSpotifyStore();

// computed
const trackDuration: ComputedRef<string> = computed(() => {
  if (!props.track) {
    return "";
  }

  return calcDuration(props.track.duration_ms);
});

const playingContext: ComputedRef = computed(() => spotifyStore.playingContext);
const playList: ComputedRef = computed(() => spotifyStore.playList);

// filters
const trimEnd = function (value: string) {
  return value.trimEnd();
};

//methods
const play: Function = async () => {
  if (playingContext.value.context.uri === playList.value.uri) {
    const playListPosition = playList.value.tracks.items.findIndex(
      (track) => track.track.id === props.track.id,
    );

    try {
      await SpotifyHttpService.playTrack(
        playingContext.value.context.uri,
        playListPosition,
      );
    } catch (e) {
      // Todo
    }
  }
};
</script>

<style scoped>
.clickable {
  cursor: pointer;
}
</style>
