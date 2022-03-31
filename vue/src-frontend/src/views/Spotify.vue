<template>
  <div
    class="container-flex full-height"
  >
    <div class="row px-0 mx-0">
      <Menu />
    </div>
    <Splitter class="spotify-player-height rounded-0">
      <SplitterPanel :size="30" :minSize="10">
        <TrackList />
      </SplitterPanel>
      <SplitterPanel :size="70" :minSize="20">
        <Player />
      </SplitterPanel>
    </Splitter>
  </div>
</template>

<script lang="ts">
import {ITrack, ITrackList} from "@/interfaces/spotify/spotifyInterfaces";
import { BackendDataService } from "@/services/backendDataService";

import Menu from "@/components/Spotify/Menu.vue";
import Player from "@/components/Spotify/Player.vue";
import TrackList from "@/components/Spotify/TrackList.vue";

import Splitter from "primevue/splitter";
import SplitterPanel from "primevue/splitterpanel";

import { defineComponent, computed, onMounted } from "vue";
import { Store, useStore } from 'vuex'

export default defineComponent({
  name: "Spotify",
  components: {
    Menu,
    Player,
    TrackList,
    Splitter,
    SplitterPanel,
  },
  setup(){
    const store: Store<any> = useStore();

    // attr
    let spotifyPlayerSDKDOMElem: HTMLElement|null = computed(() => store.state.spotify.spotifyPlaybackSDKDOMElem);
    let spotifyPlayer: any = computed(() => store.state.spotify.spotifyPlayer);
    const currentTrack: ITrack = computed(() => store.state.spotify.currentTrack);
    const trackList: ITrackList = computed(() => store.state.spotify.trackList);

    // methods
    const initSpotifyPlayer = function(){

      BackendDataService.getSavedSpotifyToken()
        .then((response: any) => {
          if (response.status !== 200) {
            return;
          }

          store.commit("setSpotifyAuthSuccess", response.status === 200);

          spotifyPlayerSDKDOMElem = document.createElement("script");
          spotifyPlayerSDKDOMElem.setAttribute(
            "src",
            "https://sdk.scdn.co/spotify-player.js"
          );
          spotifyPlayerSDKDOMElem.setAttribute("defer", "true");
          document.head.appendChild(spotifyPlayerSDKDOMElem);

          window.onSpotifyWebPlaybackSDKReady = () => {
            spotifyPlayer = new window.Spotify.Player({
              name: "Playarea2 Web Playback SDK",
              getOAuthToken: (cb) => {
                cb(response.data.token);
              },
              volume: 0.5,
            });

            spotifyPlayer.addListener("ready", ({ device_id }) => {
              console.log("Ready with Device ID", device_id);
            });

            spotifyPlayer.addListener("not_ready", ({ device_id }) => {
              console.log("Device ID has gone offline", device_id);
            });

            spotifyPlayer.connect();
          };
        }).catch((err: Error) => {
          console.error(err.message);
        });
    }

    onMounted(async () => {
      await initSpotifyPlayer();
    });

    const disableSpotifyPlayer = function() {
      spotifyPlayer = null;
      spotifyPlayerSDKDOMElem = null;
    };

    return {
      //attr
      spotifyPlayerSDKDOMElem,
      spotifyPlayer,
      currentTrack,
      trackList,
      //methods
      initSpotifyPlayer,
      disableSpotifyPlayer,
    }
  }
});
</script>

<style scoped>
.spotify-player-height {
  min-height: calc(100vh - 56px - 56px - 45px);
}
</style>

