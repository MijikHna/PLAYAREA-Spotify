<template>
  <Splitter class="rounded-0">
    <!-- TODO: if mobile get rid of the sidebar: should be horizontal -->
    <SplitterPanel class="flex items-center justify-center w-100" :size="30" :minSize="10">
      <ScrollPanel style="height: var(--player-height); width: 100%" :dt="{ bar: { background: '{primary.color}' } }">
        <MediaContextPanel />
      </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="flex items-center justify-center" :size="70" :minSize="50">
      <MediaControlPanel />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
  import ScrollPanel from "primevue/scrollpanel";
  import Splitter from "primevue/splitter";
  import SplitterPanel from "primevue/splitterpanel";

  import MediaControlPanel from "@/components/spotify/player/media-control/MediaControlPanel.vue";
  import MediaContextPanel from "@/components/spotify/player/media-context/MediaContextPanel.vue";
</script>

<style scoped lang="css">
  ::v-deep(.tabmenudemo-content) {
    padding: 2rem 1rem;
  }
</style>
