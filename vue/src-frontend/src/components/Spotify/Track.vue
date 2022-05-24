<template>
  <div
    class="flex border clickable"
    @click="play"
    v-ripple
  >
    <div>
      <template v-for="(artist, index) in track.artists">
        <span v-if="index !== track.artists.length-1">{{ artist.name }}, </span>
        <span v-else>
          {{artist.name}}
        </span>
      </template>
      <span> - </span>
      {{ track.name }}</div>
    <div>{{ trackDuration }}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { computed, ComputedRef, track } from "@vue/reactivity";

import { ITrack } from "@/interfaces/spotifyInterfaces";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";
import { calcDuration } from '@/helper/track';
import { Store, useStore } from "vuex";

import Ripple from 'primevue/ripple';

export default defineComponent({
  name: "Track",
  props: {
    track: {
      type: Object as PropType<ITrack>,
    },
  },
  directives: {
    'ripple': Ripple,
  },

  setup(props) {
    //global
    const store: Store<any> = useStore();

    // computed
    const trackDuration: ComputedRef<string> = computed(() => {
      if (!props.track) {
        return '';
      }

      return calcDuration(props.track.duration_ms)
    });
    const playingContext: ComputedRef<any> = computed(() => store.state.spotify.playingContext);
    const playList: ComputedRef<any> = computed(() => store.state.spotify.playList);

    // filters
    const trimEnd = function(value: string) {
      return value.trimEnd();
    };

    //methods
    const play: Function = async () => {
      if (playingContext.value.context.uri === playList.value.uri ){
        const playListPosition = playList.value.tracks.items.findIndex(track => track.track.id === props.track.id);

        try {
          await SpotifyHttpService.playTrack(playingContext.value.context.uri, playListPosition);
        }
        catch(e){
          // Todo
        }
        finally{
          return;
        }
      }

      try {
        await SpotifyHttpService.playTrack(props.track.album.uri);
      }
      catch(e){

      }
    }

    return {
      // props
      props,
      // computed
      trackDuration,
      // fitlers
      trimEnd,
      // methods
      play
    }
  }
});
</script>

<style scoped>
.clickable {
  cursor: pointer;
}
</style>