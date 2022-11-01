<template>
  <Splitter class="spotify-player-height rounded-0">
    <SplitterPanel class="current-playing" :size="30" :minSize="10">
      <ScrollPanel style="width: 100%">
        <TrackList />
      </ScrollPanel>
    </SplitterPanel>
    <SplitterPanel class="current-playlist" :size="70" :minSize="50">
      <Control />
    </SplitterPanel>
  </Splitter>
</template>

<script setup lang="ts">
  import { useSpotifyStore } from "@/store/spotify";
  import { onMounted } from "vue";

  import Splitter from "primevue/splitter";
  import SplitterPanel from "primevue/splitterpanel";
  import ScrollPanel from "primevue/scrollpanel";

  import { ToastServiceMethods } from "primevue/toastservice";
  import { useToast } from "primevue/usetoast";

  import { ITrack, ITrackList } from "@/interfaces/spotifyInterfaces";
  import { BackendHttpService } from "@/services/BackendHttpService";

  import Control from "@/components/Spotify/Control.vue";
  import TrackList from "@/components/Spotify/TrackList.vue";

  import { AxiosResponse } from "axios";

  //global
  const spotifyStore = useSpotifyStore();
  const toast: ToastServiceMethods = useToast();

  onMounted(async () => {
    await initSpotifyPlayer();
  });

  const initSpotifyPlayer = async function () {
    if (spotifyStore.spotifyPlayer) {
      return;
    }

    // try {
    //   const response: AxiosResponse  = await BackendHttpService.getSavedSpotifyToken();

    //   if (response.status === 200){
    //     spotifyStore.setSpotifyAuthSuccess(true);
    //   }
    // }catch(e){
    //   return;
    // }

    const spotifyPlayerSDKDOMElemTemp = document.createElement("script");
    spotifyPlayerSDKDOMElemTemp.setAttribute(
      "src",
      "https://sdk.scdn.co/spotify-player.js",
    );
    spotifyPlayerSDKDOMElemTemp.setAttribute("defer", "true");
    document.head.appendChild(spotifyPlayerSDKDOMElemTemp);
    spotifyStore.spotifyPlayerDOMElem = spotifyPlayerSDKDOMElemTemp;

    window.onSpotifyWebPlaybackSDKReady = () => {
      spotifyStore.spotifyPlayer = new window.Spotify.Player({
        name: "Playarea2 Web Playback",
        getOAuthToken: async (cb) => {
          const response: AxiosResponse =
            await BackendHttpService.getSavedSpotifyToken();
          cb(response.data.token);
        },
        volume: 0.5,
      });

      spotifyStore.spotifyPlayer.addListener("ready", ({ device_id }) => {
        toast.add({
          severity: "success",
          summary: "Spotify Player",
          detail: "Spotify Player is ready",
          life: 5000,
        });
      });

      spotifyStore.spotifyPlayer.addListener("not_ready", ({ device_id }) => {
        // Toaster Message
        console.log("Device ID has gone offline");
      });

      spotifyStore.spotifyPlayer.addListener(
        "player_state_changed",
        (
          // {track_window: {current_track, next_tracks } = null}
          state: any = null,
        ) => {
          console.log(state);

          if (state === null) {
            spotifyStore.playList = null;
            spotifyStore.playingContext = null;
            spotifyStore.playerActive = false;
            spotifyStore.currentTrack = null;
            spotifyStore.nextTracks = [];

            return;
          }

          // if (!state?.track_window?.current_track || !state.track_window.next_tracks) {
          //   return;
          // }

          spotifyStore.playerActive = true;
          spotifyStore.currentTrack = state.track_window.current_track;
          spotifyStore.nextTracks = state.track_window.next_tracks;
          spotifyStore.playingContext = state;
        },
      );

      spotifyStore.spotifyPlayer.connect();

      spotifyStore.spotifyAuthSuccess = true;
    };
  };
</script>

<style scoped lang="css">
  ::v-deep(.tabmenudemo-content) {
    padding: 2rem 1rem;
  }
  .current-playing {
    overflow-y: auto;
    max-height: 25%;
  }

  .current-playlist {
    overflow-y: auto;
    max-height: 25%;
  }
</style>
