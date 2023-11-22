<template>
  <PlayingList />
  <Divider align="center">
    <span class="p-tag">Playlist</span>
  </Divider>
  <PlayList />
</template>

<script setup lang="ts">
import Divider from "primevue/divider";

import PlayList from "./PlayList.vue";
import PlayingList from "./PlayingList.vue";
</script>
