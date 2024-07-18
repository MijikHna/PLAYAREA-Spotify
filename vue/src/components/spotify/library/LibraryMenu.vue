<template>
  <div class="flex flex-col mx-1">
    <Card class="m-1 cursor-pointer hover:bg-surface-300" v-for="(menuItem, index) in libarayMenuItems" :key="index"
      @click="router.push({ name: menuItem.to })">
      <template #title> {{ menuItem.label }}</template>
      <template #subtitle>
        {{ menuItem.description }}
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { Ref, ref } from 'vue';

import Card from 'primevue/card';
import { useRouter } from 'vue-router';

//global data
const router = useRouter()

// data selected
const libarayMenuItems: Ref<{ label: string, description: string; icon: string; to: string }[]>
  = ref([
    {
      label: "Playlists",
      description: "Create and manage your playlists",
      icon: "pi pi-fw pi-list",
      to: "playlists",
    },
    {
      label: "Artists",
      description: "Follow your favorite artists",
      icon: "pi pi-fw pi-user",
      to: "artists",
    },
    {
      label: "Albums",
      description: "Save your favorite albums",
      icon: "pi pi-fw pi-images",
      to: "albums",
    },
    {
      label: "Tracks",
      description: "Save your favorite tracks",
      icon: "pi pi-fw pi-music",
      to: "tracks",
    },
  ]);
</script>

<style scoped>
>>>.p-card-content {
  padding: 0;
}
</style>
