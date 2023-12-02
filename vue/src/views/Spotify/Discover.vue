<template>
  <Splitter class="min-discover-height border-solid">
    <SplitterPanel class="overflow-auto" :size="30">
      <ScrollPanel style="height: var(--discover-scrollpanel-height);" :pt="{
        wrapper: {
          style: { 'border-right': '10px solid var(--surface-ground)' }
        },
        bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
      }">
        <DiscoverMenu />
      </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="overflow-auto">
      <ScrollPanel style="height: var(--discover-scrollpanel-height);" :pt="{
        wrapper: {
          style: { 'border-right': '10px solid var(--surface-ground)' }
        },
        bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
      }">
        <Router-view />
      </ScrollPanel>
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
import ScrollPanel from "primevue/scrollpanel";
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';

import DiscoverMenu from '@/components/Spotify/Discover/DiscoverMenu.vue';

</script>

<style scoped>
.min-discover-height {
  min-height: var(--discover-height);
  max-height: var(--discover-height);
}
</style>
