<template>
  <div class="grid m-0 min-w-full align-items-center px-4">
    <div class="col-11">
      <Slider v-model="positionInMs" :max="durationInMs" @update:modelValue="playAtPosition" />
    </div>
    <div class="col-1">
      {{ positionInMin }}/{{ durationInMin }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from "@vue/reactivity";
import { watch } from "@vue/runtime-core";
import { storeToRefs } from "pinia";

import Slider, { SliderSlideEndEvent } from "primevue/slider";

import { useSpotifyStore } from "@/store/spotify";
import { calcDuration } from "@/helper/track";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";

//global
const spotifyStore = useSpotifyStore();
const { playingContext, spotifyPlayer } = storeToRefs(spotifyStore);

// data
const durationInMin: Ref<string> = ref("");
const durationInMs: Ref<number> = ref(0);
const positionInMs: Ref<number> = ref(0);
const positionInMin: Ref<string> = ref("");

const runningTimeout: Ref<NodeJS.Timeout | number> = ref(null);

// computed
watch(playingContext, (newValue: { duration: number, position: number, paused: boolean }) => {
  durationInMin.value = calcDuration(newValue.duration);
  durationInMs.value = newValue.duration;

  if (runningTimeout.value) clearTimeout(runningTimeout.value);
  positionInMs.value = newValue.position;

  if (newValue.paused) return;
  runningTimeout.value = setInterval(increasePosition, 1000);
});

// methods
function increasePosition(): void {
  if (positionInMs.value === null) return;

  positionInMs.value += 1000;
  positionInMin.value = calcDuration(positionInMs.value);
}

const playAtPosition = async (value: number): Promise<void> => {
  if (spotifyPlayer.value === null) return;

  try {
    const repsonse = await SpotifyHttpService.http.put(`me/player/seek?position_ms=${value}`)
    if (repsonse.status !== 204) {
      throw new Error("Could not play at position");
    }
  } catch (error) {
    console.log(error);
  }

};
</script>
