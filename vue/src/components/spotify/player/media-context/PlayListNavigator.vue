<template>
  <ul class="m-0 p-0 list-none rounded p-2 flex flex-col gap-2 w-full">
      <MediaQuickInfo v-for="(trackItem, index) in player.activePlayList?.items" :key="index" :track="trackItem.track" />
  </ul>
</template>

<script setup lang="ts">
  import { ref, Ref, watch } from "vue";
  import { storeToRefs } from "pinia";

  import { useSpotifyStore } from "@/store/spotify";

  import MediaQuickInfo from "./MediaQuickInfo.vue";

  import { SpotifyHttpService } from "@/services/SpotifyHttpService";

  // global
  const spotifyStore = useSpotifyStore();

  // store data
  const { player, dom } = storeToRefs(spotifyStore);

  // watchers
  watch(
    () => player.value.playingContext?.context?.uri,
    async (newValue) => {
      if (!newValue) return;

      const currentState = await dom.value.spotifyPlayer.getCurrentState();

      if (currentState?.context?.uri?.match(new RegExp("spotify:playlist.*"))) {
        // TODO: try-catch
        const response = await SpotifyHttpService.http.get(`/playlists/${currentState.context.uri.split(":")[2]}/tracks`,
        );

        const responsePlaylist = response.data;

        player.value.activePlayList = responsePlaylist;
        console.log(responsePlaylist);
      }
      // TODO: Album Context should be different or define type which suites for both and process the response accordingly
    //   else if (currentState?.context?.uri?.match(new RegExp("spotify:album.*"))) {
    //     const response = await SpotifyHttpService.http.get(`/albums/${currentState.context.uri.split(":")[2]}`,
    //     );
    //     const responsePlaylist = response.data.tracks;
    //
    //
    //     player.value.activePlayList = responsePlaylist;
    //     console.log(responsePlaylist);
    //   }
    }
  );
</script>
