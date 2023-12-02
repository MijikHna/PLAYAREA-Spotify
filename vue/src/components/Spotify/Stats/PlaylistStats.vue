<template>
  <div>
    <DataView :value="playlists">
      <template #list="slotProps">
        <div class="grid grid-nogutter">
          <div v-for="(playlist, index) in slotProps.items" :key="index" class="col-12">
            <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4"
              :class="{ 'border-top-1 surface-border': index !== 0 }">
              <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round"
                :src="playlist.image.url" :alt="playlist.name" />
              <div
                class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
                <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                  <div class="text-2xl font-bold text-900">{{ playlist.name }}</div>
                </div>
                <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                  <Button icon="pi pi-calculator" rounded @click="anaylzePlaylist(playlist)"
                    label="Analyze Playlist"></Button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </DataView>

    <Dialog v-model:visible="visible" modal header="Header" :style="{ width: '50rem' }"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <template #header>
        <div class="inline-flex align-items-center justify-content-center gap-2">
          <i class="pi pi-check-circle" style="font-size: 2rem; color: #4caf50;"></i>
          <h4 class="m-0">Playlist Analyzes: {{playlistAudioFeatures.name}}</h4>
        </div>
      </template>
      <p class="m-0">
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Acousticness: {{ playlistAudioFeatures.acousticness }} %</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Danceability: {{ playlistAudioFeatures.danceability }} %</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Energy: {{ playlistAudioFeatures.energy }} %</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Instrumentalness: {{ playlistAudioFeatures.instrumentalness }} %
        </div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Liveness: {{ playlistAudioFeatures.liveness }} %</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Speechiness: {{ playlistAudioFeatures.speechiness }} %</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Valence: {{ playlistAudioFeatures.valence }}</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Loadness: {{ playlistAudioFeatures.loudness }} Db</div>
      </div>
      <div class="flex flex-column align-items-center gap-3">
        <div class="text-2xl font-bold text-900">Temp: {{ playlistAudioFeatures.tempo }} BPM</div>
      </div>
      </p>
      <template #footer>
        <Button label="Ok" icon="pi pi-check" @click="visible = false" autofocus />
      </template>
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref, onMounted } from "vue";
import { AxiosResponse } from "axios";

import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';
import Knob from 'primevue/knob';

import { SpotifyHttpService } from "@/services/SpotifyHttpService";
import {
  SpotifyAPICollectionResponse,
  SpotifyAPIPlaylistTrackCollectionResponse,
  SpotifyAPIAudioFeaturesResponse,
  SpoitifyAPIAudioFeatures,
  SpotifiyAPIPlaylist,
  SpotifyAPITrack,
  Playlist
} from "@/types/spotify/stat.types";

//global

// data
const visible: Ref<boolean> = ref<boolean>(false);
const playlists: Ref<Playlist[]> = ref<Playlist[]>([]);
const playlistAudioFeatures: Ref<SpoitifyAPIAudioFeatures & { name: string }> = ref<SpoitifyAPIAudioFeatures & { name: string }>();

// methods
const getUserPlaylists = async () => {
  try {
    const response: SpotifyAPICollectionResponse = await SpotifyHttpService.http.get('/me/playlists?limit=50&offset=0');
    console.log(response.data);

    playlists.value = response.data.items.map((playlist: SpotifiyAPIPlaylist) => ({
      id: playlist.id,
      name: playlist.name,
      image: playlist.images[0],
    }));
  }
  catch (error) {
    console.error(error);
  }
};

const anaylzePlaylist = async (playlist: Playlist) => {
  try {
    const playlistTracksResponse: AxiosResponse<SpotifyAPICollectionResponse> =
      await SpotifyHttpService.http.get(`/playlists/${playlist.id}/tracks`);

    if (playlistTracksResponse.status !== 200) throw new Error('Error getting playlist tracks');

    const tracks = playlistTracksResponse.data.items;

    // build string of track ids, comma separated, use reduce
    const trackIds: string = tracks.reduce((acc: string, track: SpotifyAPIPlaylistTrackCollectionResponse) => acc + track.track.id + ',', '');

    const response: AxiosResponse<SpotifyAPIAudioFeaturesResponse> =
      await SpotifyHttpService.http.get(`/audio-features?ids=${trackIds}`);

    if (response.status !== 200) throw new Error('Error getting audio features');

    // get average of all audio features, use reduce
    const audioFeatures: SpotifyAPIAudioFeaturesResponse = response.data;
    const audioFeaturesSum = audioFeatures.audio_features.reduce(
      (acc: SpoitifyAPIAudioFeatures, audioFeature: SpoitifyAPIAudioFeatures) => {
        acc.acousticness += audioFeature.acousticness;
        acc.danceability += audioFeature.danceability;
        acc.energy += audioFeature.energy;
        acc.instrumentalness += audioFeature.instrumentalness;
        acc.liveness += audioFeature.liveness;
        acc.speechiness += audioFeature.speechiness;
        acc.valence += audioFeature.valence;
        acc.loudness += audioFeature.loudness;
        acc.tempo += audioFeature.tempo;
        return acc;
      },
      {
        acousticness: 0,
        danceability: 0,
        energy: 0,
        instrumentalness: 0,
        liveness: 0,
        speechiness: 0,
        valence: 0,
        loudness: 0,
        tempo: 0,
      }
    );

    playlistAudioFeatures.value = {
      //convert to percent
      acousticness: Math.floor(audioFeaturesSum.acousticness / audioFeatures.audio_features.length * 100),
      danceability: Math.floor(audioFeaturesSum.danceability / audioFeatures.audio_features.length * 100),
      energy: Math.floor(audioFeaturesSum.energy / audioFeatures.audio_features.length * 100),
      instrumentalness: Math.floor(audioFeaturesSum.instrumentalness / audioFeatures.audio_features.length * 100),
      liveness: Math.floor(audioFeaturesSum.liveness / audioFeatures.audio_features.length * 100),
      speechiness: Math.floor(audioFeaturesSum.speechiness / audioFeatures.audio_features.length * 100),
      valence: Math.floor(audioFeaturesSum.valence / audioFeatures.audio_features.length * 100),
      loudness: (audioFeaturesSum.loudness / audioFeatures.audio_features.length).toFixed(2),
      tempo: Math.floor(audioFeaturesSum.tempo / audioFeatures.audio_features.length),
    };

    playlistAudioFeatures.value.name = playlist.name;
    visible.value = true;
  }
  catch (error) {
    console.error(error);
  }
};

onMounted(async () => {
  await getUserPlaylists();
});

</script>
