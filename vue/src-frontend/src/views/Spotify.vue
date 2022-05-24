<template>
  <div class="max-player-width mx-auto">
    <div class="row px-0 mx-0">
      <Menu />
    </div>

    <div class="card">
        <TabMenu :model="tabMenuItems" class-/>
    </div>
    <!-- <KeepAlive include="Player">
      <router-view/>
    </KeepAlive> -->

    <router-view v-slot="{ Component }">
      <KeepAlive>
        <component :is="Component"/>
      </KeepAlive>
    </router-view>
  </div>
</template>

<script setup lang="ts">
import { ISpotifyTabMenuItems } from "@/interfaces/spotifyInterfaces";

import Menu from "@/components/Spotify/Menu.vue";
import TabMenu from 'primevue/tabmenu';

// data
const tabMenuItems: ISpotifyTabMenuItems[] = [
  {
    label: 'Player',
    icon: 'pi pi-volume-up',
    to: 'player',
  },
  {
    label: 'Discover',
    icon: 'pi pi-list',
    to: 'discover'
  },
  {
    label: 'Stats',
    icon: 'pi pi-star',
    to: 'stats'
  }
]
</script>

<style scoped>
.spotify-player-height {
  min-height: calc(100vh - 56px - 56px - 45px - 44px);
  max-height: calc(100vh - 56px - 56px - 45px - 44px);
}

.max-player-width {
  max-width: 1200px;
}
</style>

