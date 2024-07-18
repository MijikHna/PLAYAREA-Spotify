<template>
  <!-- TODO: max-width -->
  <Tabs v-model:value="tabIndex">
    <TabList>
      <Tab v-for="tabPane in tabPaneComonents" :key="tabPane.value" :value="tabPane.value">
        {{ tabPane.name }}
      </Tab>
    </TabList>
    <TabPanels>
      <TabPanel v-for="tabPane in tabPaneComonents" :key="tabPane.value" :value="tabPane.value">
        <component :is="tabPane.component" />
      </TabPanel>
    </TabPanels>
  </Tabs>

</template>

<script setup lang="ts">
import Tabs from "primevue/tabs";
import TabList from "primevue/tablist";
import Tab from "primevue/tab";
import TabPanels from "primevue/tabpanels";
import TabPanel from "primevue/tabpanel";

import { ref, Ref } from "vue";

import AlbumDisplay from "@/components/spotify/library/album/AlbumDisplay.vue";
import TrackDisplay from "@/components/spotify/library/track/TrackDisplay.vue";
import ArtistDisplay from "@/components/spotify/library/artist/ArtistDisplay.vue";
import PlayListDisplay from "@/components/spotify/library/playlist/PlayListDisplay.vue";
PlayListDisplay


type TabPane = { name: string; component: any, value: string};

// NOTE: import the components dynamically
const tabIndex: Ref<string> = ref("0");
const tabPaneComonents: TabPane[] = [
  { name: "Playlists", component: PlayListDisplay, value: "0"},
  { name: "Artists", component: ArtistDisplay, value: "1"},
  { name: "Tracks", component: TrackDisplay, value: "2"},
  { name: "Albums", component: AlbumDisplay, value: "3"},
];
</script>

<style scoped>
</style>
