<template>
  <Splitter class="min-discover-height border-solid">
    <SplitterPanel class="overflow-auto" :size="30">
      <DiscoverMenu />
    </SplitterPanel>
    <SplitterPanel class="overflow-auto">
      <Router-view />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
import DiscoverMenu from '@/components/Spotify/Discover/DiscoverMenu.vue';

import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
</script>

<style scoped>
.min-discover-height {
  min-height: calc(100vh - 56px - 56px - 45px - 42px);
  max-height: calc(100vh - 56px - 56px - 45px - 42px)
}
</style>
