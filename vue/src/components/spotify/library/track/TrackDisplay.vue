<template>
  <!--TODO: ScrollPanel -->
  <ScrollPanel style="height: var(--library-height); width: 100%" :dt="{ bar: { background: '{primary.color}' } }">
    <div class="grid grid-cols-5 gap-4 mx-3">
      <Track 
      :track="track.track" 
      v-for="(track, index) in tracks" 
      :key="index" 
      />
    </div>
  </ScrollPanel>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from 'vue';
import Track from './Track.vue';
import { SpotifyHttpService } from '@/services/SpotifyHttpService';
import ScrollPanel from 'primevue/scrollpanel';

// data
const tracks: Ref<any> = ref<any>([]);

// methods
const getTracks = async () => {
  try {
    const response = await SpotifyHttpService.http.get('me/tracks');

    if (response.status !== 200) throw new Error('Could not get tracks');
    
    tracks.value = response.data.items;
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

// hooks
onMounted(async () => {
  await getTracks();
});



</script>

<style scoped>

</style>
