<template>
  <Splitter class="rounded-0">
    <SplitterPanel class="current-playing" :size="30" :minSize="10">
      <ScrollPanel style="height: var(--player-height);" :pt="{
        wrapper: {
          style: { 'border-right': '10px solid var(--surface-ground)' }
        },
        bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
      }">
        <PlayingContext />
      </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="current-playlist" :size="70" :minSize="50">
      <Control />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
import ScrollPanel from "primevue/scrollpanel";
import Splitter from "primevue/splitter";
import SplitterPanel from "primevue/splitterpanel";

import Control from "@/components/Spotify/Player/Control.vue";
import PlayingContext from "@/components/Spotify/Player/PlayingContext.vue";

</script>

<style scoped lang="css">
::v-deep(.tabmenudemo-content) {
  padding: 2rem 1rem;
}

.current-playing {
  overflow-y: auto;
  max-height: 25%;
}

.current-playlist {
  overflow-y: auto;
  max-height: 25%;
}

.spotify-player-height {
  min-height: var(--player-height);
  max-height: var(--player-height);
}
</style>
