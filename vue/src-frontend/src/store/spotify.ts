import { SpotifyState } from "@vue/runtime-dom";

export const spotify = {
  state: () => ({
    // Spotify Player
    spotifyAuthSuccess: false,
    spotifyPlayerSDKDOMElem: null,
    spotifyPlayer: null,
    // Devices
    devices: [],
    // Playlist
    currentTrack: null,
    currentPlayList: null,
  }),
  getters: {
    getSpotifyAuthSuccess(state: SpotifyState) {
      return state.spotifyAuthSuccess;
    },
  },
  mutations: {
    setSpotifyAuthSuccess(state: SpotifyState, authSuccess: boolean) {
      state.spotifyAuthSuccess = authSuccess;
    },
    setSpotifyPlayerDOMElem(state: SpotifyState, spotifyElem: HTMLElement) {
      state.spotifyPlayerSDKDOMElem = spotifyElem;
    },
    setSpotifyPlayer(state: SpotifyState, spotifyPlayer: any) {
      state.spotifyPlayer = spotifyPlayer;
    },
    setCurrentTrack(state: SpotifyState, newState: any) {
      state.currentTrack = newState;
    },
  },
  actions: {},
  modules: {},
};
