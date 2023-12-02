<template>
  <div class="border-solid flex stat-height">
    <div class="flex-intiial flex">
      <div class="card flex justify-content-center">
        <Sidebar :pt="{ mask: { style: { top: '140px', height: 'var(--stats-sidebar-height)' } } }"
          v-model:visible="visible" header="Sidebar">
          <div class="card flex justify-content-center">
            <PanelMenu :model="menuItems" class="w-full md:w-20rem" />
          </div>
        </Sidebar>
        <div class="flex flex-column min-h-full surface-300">
          <Button icon="pi pi-arrow-right" @click="visible = true" />
        </div>
      </div>
    </div>
    <ScrollPanel class="-py-8" style="width: 100%; height: var(--stats-scrollpanel-height);" :pt="{
      wrapper: {
        style: { 'border-right': '10px solid var(--surface-ground)' }
      },
      bary: 'hover:bg-primary-400 bg-primary-300 opacity-100;'
    }">
      <div class="flex-auto flex">
        <router-view />
      </div>
    </ScrollPanel>
  </div>
</template>

<script setup lang="ts">
import { Ref, ref } from 'vue';
import { useRouter } from "vue-router";

import PanelMenu from 'primevue/panelmenu';
import ScrollPanel from "primevue/scrollpanel";
import Sidebar from 'primevue/sidebar';
import Button from 'primevue/button';


import { StatMenuItem, } from '@/types/spotify/stat.types';

//global
const router = useRouter();
// data
const visible: Ref<boolean> = ref<boolean>(false);

const menuItems: Ref<StatMenuItem[]> = ref<StatMenuItem[]>([
  {
    label: 'My Stats',
    //icon: 'pi pi-fw pi-chart-bar',
    command: () => router.push({ name: 'my-top' }),
  },
  {
    label: 'Playlists',
    icon: 'pi pi-fw pi-list',
    command: () => router.push({ name: 'playlist-stats' }),
  },
  {
    label: 'Artists',
    icon: 'pi pi-fw pi-user',
    command: () => router.push({ name: 'artist-stats' }),
  },
  {
    label: 'Podcasts',
    icon: 'pi pi-fw pi-podcast',
    command: () => router.push({ name: 'podcast-stats' }),
  },
]);
</script>

<style scoped>
.stat-height {
  min-height: var(--stats-height);
  max-height: var(--stats-height);
}
</style>
