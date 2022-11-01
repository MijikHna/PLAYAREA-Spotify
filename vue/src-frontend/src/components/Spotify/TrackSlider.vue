<template>
  <div class="row mx-0 align-items-center">
    <div class="col-11">
      <Slider v-model="positionInMs" :max="durationInMs" />
    </div>
    <div class="col-1">
      {{ durationInMin }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ComputedRef, ref, Ref } from "@vue/reactivity";
import { watch } from "@vue/runtime-core";

import Slider from "primevue/slider";

import { useSpotifyStore } from "@/store/spotify";

import { calcDuration } from "@/helper/track";

//global
const spotifyStore = useSpotifyStore();

// data
const test = 1000;
const durationInMin: Ref<string> = ref("");
const durationInMs: Ref<number> = ref(0);
const positionInMs: Ref<number> = ref(0);

// computed
const playingContext: ComputedRef<any> = computed(
  () => spotifyStore.playingContext,
);

watch(playingContext, (newValue: any) => {
  durationInMin.value = calcDuration(newValue.duration);
  durationInMs.value = newValue.duration;
  positionInMs.value = newValue.position;
});
</script>
