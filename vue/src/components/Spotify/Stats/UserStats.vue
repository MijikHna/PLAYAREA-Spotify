<template>
  <div class="flex-auto">
    <Panel header="Top 50 Tracks" toggleable>
      <DataView :value="userTracks">
        <template #list="slotProps">
          <div class="grid grid-nogutter">
            <div v-for="(track, index) in slotProps.items" :key="index" class="col-12">
              <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4"
                :class="{ 'border-top-1 surface-border': index !== 0 }">
                <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="track.image.url"
                  :alt="track.name" />
                <div
                  class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                  <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                    <div class="text-2xl font-bold text-900">{{ track.name }}</div>
                    <Knob :modelValue="track.popularity" readonly :cancel="false"></Knob>
                    <div class="flex align-items-center gap-3">
                      <span class="flex align-items-center gap-2">
                        <i class="pi pi-tag"></i>
                        <span class="font-semibold">{{ track.genres }}</span>
                      </span>
                      <Tag v-for="(artist, index) in track.artists" :value="artist"></Tag>
                    </div>
                  </div>
                  <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                    <span class="text-2xl font-semibold">Released {{ track.release_date }}</span>
                    <Button icon="pi pi-play" rounded></Button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>
      </DataView>
    </Panel>

    <Panel class="" header="Top 50 Artist" toggleable>
      <DataView :value="userArtists">
        <template #list="slotProps">
          <div class="grid grid-nogutter">
            <div v-for="(artist, index) in slotProps.items" :key="index" class="col-12">
              <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4"
                :class="{ 'border-top-1 surface-border': index !== 0 }">
                <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round"
                  :src="artist.image.url" :alt="artist.name" />
                <div
                  class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                  <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                    <div class="text-2xl font-bold text-900">{{ artist.name }}</div>
                    <Knob :modelValue="artist.popularity" readonly :cancel="false"></Knob>
                    <div class="flex align-items-center gap-3">
                      <span class="flex align-items-center gap-2">
                        <i class="pi pi-tag"></i>
                        <span class="font-semibold">{{ artist.LATER }}</span>
                      </span>
                      <Tag v-for="(genre, index) in artist.genres" :value="genre"></Tag>
                    </div>
                  </div>
                  <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                    <Button icon="pi pi-play" rounded></Button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>

      </DataView>
    </Panel>
  </div>
</template>

<script setup lang="ts">
import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional
import Panel from 'primevue/panel';

import Tag from 'primevue/tag';
import Knob from 'primevue/knob';
import Button from 'primevue/button';

import { SpotifyHttpService } from '@/services/SpotifyHttpService';
import { Ref, onMounted, ref } from 'vue';

import { UserTopStatsResponse, TopArtistsResponse, TopTrackResponse, TopTrack, TopArtist } from '@/types/spotify/stat.types';
import { AxiosResponse } from 'axios';

// data
const userTracks: Ref<TopTrack[]> = ref<TopTrack[]>();
const userArtists: Ref<TopArtists[]> = ref<TopArtists[]>();

// methods
const getUserTracksStats = async () => {
  const response = await SpotifyHttpService.http.get('/me/top/tracks?limit=50&offset=0');

  try {
    userTracks.value = response.data.items.map(
      (track: TopTrackResponse): TopTrack => ({
        name: track.name,
        popularity: track.popularity,
        duration_ms: track.duration_ms,
        release_date: track.album.release_date,
        image: track.album.images[0],
        artists: track.artists.map((artist: any) => artist.name),
      })
    );
  }
  catch (error) {
    console.error(error);
  }
};

const getUserArtistsStats = async () => {
  const response = await SpotifyHttpService.http.get('/me/top/artists?limit=50&offset=0');
  console.log(response.data);

  try {
    userArtists.value = response.data.items.map(
      (artist: TopArtistsResponse): TopArtist => ({
        name: artist.name,
        genres: artist.genres,
        popularity: artist.popularity,
        image: artist.images[0],
      })
    );
  }
  catch (error) {
    console.error(error);
  }
};

onMounted(async () => {
  await getUserTracksStats();
  await getUserArtistsStats();
});


</script>

<style lang="scss" scoped></style>
