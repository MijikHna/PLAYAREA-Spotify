import { defineStore, StoreDefinition } from "pinia";
import { SpotifyState } from "@vue/runtime-dom";

export const useSpotifyStore: StoreDefinition = defineStore("spotifyStore", {
  state: () => ({
    // Player
    spotifyAuthSuccess: false as boolean,
    spotifyPlayerDOMElem: null as any,
    spotifyPlayer: null as any,
    // Devices
    playerActive: false as boolean,
    devices: [] as any[],
    //Playlist:
    currentTrack: null as any,
    nextTracks: [] as any[],
    playingContext: null as any,
    playList: null as any,
  }),
  actions: {
    resetSpotifyPlayer() {
      this.playList = null;
      this.playingContext = null;
      this.nextTracks = [];
      this.currentTrack = null;
      this.playerActive = false;
      this.spotifyPlayer = null;
      this.spotifyPlayerDOMElem = null;
      this.spotifyAuthSuccess = false;
    },
  },
});
