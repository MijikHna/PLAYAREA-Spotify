<template>
  <div class="row mx-0 align-items-center">
    <div class="col-11">
      <Slider v-model="positionInMs" :max="durationInMs"/>
    </div>
    <div class="col-1">
      {{ durationInMin }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ComputedRef, ref, Ref } from '@vue/reactivity';
import { Store, useStore } from 'vuex';

import { calcDuration } from '@/helper/track';

import Slider from 'primevue/slider';
import { watch } from '@vue/runtime-core';

//global
const store: Store<any> = useStore();

// data
const test = 1000
const durationInMin: Ref<string> = ref('');
const durationInMs: Ref<number> = ref(0);
const positionInMs: Ref<number> = ref(0);

// computed
const playingContext: ComputedRef<any> = computed(() => store.state.spotify.playingContext);

watch(
  playingContext,
  (newValue: any) => {
    durationInMin.value = calcDuration(newValue.duration);
    durationInMs.value = newValue.duration;
    positionInMs.value = newValue.position;
  }
)
</script>