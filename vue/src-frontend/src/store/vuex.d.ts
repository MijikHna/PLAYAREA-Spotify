declare module "@vue/runtime-core" {
  interface SpotifyState {
    spotifyAuthSuccess: boolean;
    spotifyPlayerSDKDOMElem: any;
    spotifyPlayer: any;
    currentTrack: string;
    currentPlayList: string;
  }

  interface AuthState {
    isAuthenticated: boolean;
  }
}
