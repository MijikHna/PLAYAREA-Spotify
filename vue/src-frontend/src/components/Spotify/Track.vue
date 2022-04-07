<template>
  <div class="border">
    <div>{{ track.name }}</div>
    <div>{{ trackDuration }}</div>
  </div>
</template>

<script lang="ts">
import { ITrack } from "@/interfaces/spotifyInterfaces";
import { computed } from "@vue/reactivity";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "Track",
  props: {
    track: {
      type: Object as PropType<ITrack>,
    },
  },

  setup(props) {
    // computed
    const trackDuration: string = computed(() => {
      if (!props.track) {
        return '';
      }
      const duration_sec = Math.round(props.track.duration_ms / 1000);
      const min = Math.floor(duration_sec / 60);
      const sec = duration_sec % 60;

      return `${min}:${sec.toLocaleString('en-US', {minimumIntegerDigits:2})}`
    });

    return {
      // props
      props,
      //computed
      trackDuration,

    }
  }
});
</script>

<style scoped></style>