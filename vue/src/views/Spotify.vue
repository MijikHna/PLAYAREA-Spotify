<template>
  <div class="col-12 p-0">
    <Menu />
    <div class="flex">
      <TabMenu :model="tabMenuItems" @tabChange="handleTabChange" />
    </div>
    <router-view v-slot="{ Component }">
      <KeepAlive>
        <component :is="Component" />
      </KeepAlive>
    </router-view>
  </div>
</template>

<script setup lang="ts">
import { SpotifyTabMenuItem } from "@/types/spotify/app.types";

import { ref, Ref } from "vue";

import Menu from "@/components/Spotify/Menu.vue";
import TabMenu, { TabMenuChangeEvent } from 'primevue/tabmenu';
import { useRouter } from "vue-router";

// data
const router = useRouter();

const tabMenuItems: Ref<SpotifyTabMenuItem[]> = ref([
  {
    label: 'Player',
    icon: 'pi pi-volume-up',
    to: 'player',
  },
  {
    label: 'Discover',
    icon: 'pi pi-list',
    to: 'discover',
  },
  {
    label: 'Stats',
    icon: 'pi pi-star',
    to: 'stats',
  }
]);

const handleTabChange = (e: TabMenuChangeEvent) => {
  router.push({ name: tabMenuItems.value[e.index].to });
}
</script>

<style scoped></style>

