import { SpotifyState } from "@vue/runtime-dom";

export const spotify = {
  state: () => ({
    // Spotify Player
    spotifyAuthSuccess: false,
    spotifyPlayerSDKDOMElem: null,
    spotifyPlayer: null,
    // Devices
    thisPlayerActive: false,
    devices: [],
    // Playlist
    currentTrack: null,
    nextTracks: [],
    playingContext: null,
    playList: null,
  }),
  getters: {
    getSpotifyAuthSuccess(state: SpotifyState) {
      return state.spotifyAuthSuccess;
    },
  },
  mutations: {
    // Spotify Player
    setSpotifyAuthSuccess(state: SpotifyState, authSuccess: boolean) {
      state.spotifyAuthSuccess = authSuccess;
    },
    setSpotifyPlayerDOMElem(state: SpotifyState, spotifyElem: HTMLElement) {
      state.spotifyPlayerSDKDOMElem = spotifyElem;
    },
    setSpotifyPlayer(state: SpotifyState, spotifyPlayer: any) {
      state.spotifyPlayer = spotifyPlayer;
    },
    // Devices
    setThisPlayerActive(state: SpotifyState, active: any) {
      state.thisPlayerActive = active;
    },
    setDevices(state: SpotifyState, devices: any[]) {
      state.devices = devices;
    },

    // Playslist
    setCurrentTrack(state: SpotifyState, currentTrack: any) {
      state.currentTrack = currentTrack;
    },
    setNextTracks(state: SpotifyState, nextTracks: any[]) {
      state.nextTracks = nextTracks;
    },
    setPlayingContext(state: SpotifyState, context: any) {
      state.playingContext = context;
    },
    setPlayList(state: SpotifyState, playList: any) {
      state.playList = playList;
    },
  },
  actions: {
    resetSpotifyPlayer({ commit }) {
      // Playlist
      commit("setPlayingContext", null);
      commit("setNextTracks", []);
      commit("setCurrentTrack", null);
      // Devices
      commit("setDevices", []);
      commit("setThisPlayerActive", false);
      // SpotifyPlayer
      commit("setSpotifyPlayer", null);
      commit("setSpotifyPlayerDOMElem", null);
      commit("setSpotifyAuthSuccess", false);
    },
  },
};
