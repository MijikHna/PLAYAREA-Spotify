<template>
  <SpotifyCard>
    <template #header-image>
      <img :src="track.album.images.at(0).url" :alt="track.name" class="w-full rounded p-3" />
    </template>
    <template #default>
      <div class="mb-4 font-medium">{{ track.name }}</div>
    </template>
    <template #footer>
      <div class="flex justify-between items-center">
        <!--TODO: make Tags, onclick go to artist -->
        <div class="mt-0 font-semibold text-lg">{{ artistsStringList }}</div>
        <span>
          <Button icon="pi" class="p-0 m-0" iconPos="top">
            <FontAwesomeIcon :icon="faRightToBracket" />
            <!-- <span>Open</span> -->
          </Button>
        </span>
      </div>
    </template>
  </SpotifyCard>
</template>

<script setup lang="ts">
  import SpotifyCard from "@/components/common/layout/SpotifyCard.vue";
  import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
  import { faRightToBracket } from "@fortawesome/free-solid-svg-icons";
  import Button from "primevue/button";
  import { computed } from "vue";

  const props = defineProps<{
    track: any;
  }>();

  // computed
  const artistsStringList = computed(() => props.track.artists.map((artist: any) => artist.name).join(", "));
</script>

<style scoped></style>
