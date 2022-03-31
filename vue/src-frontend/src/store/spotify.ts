import { SpotifyState } from "@vue/runtime-dom";

export const spotify = {
  state: () => ({
    spotifyAuthSuccess: false,
    spotifyPlayerSDKDOMElem: null,
    spotifyPlayer: null,
    currentTrack: "Test",
    currentPlayList: "Test",
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
  },
  actions: {},
  modules: {},
};
