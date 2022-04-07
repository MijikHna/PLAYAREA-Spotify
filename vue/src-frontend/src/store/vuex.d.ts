declare module "@vue/runtime-core" {
  interface SpotifyState {
    // Spotify Player
    spotifyAuthSuccess: boolean;
    spotifyPlayerSDKDOMElem: any;
    spotifyPlayer: any;
    // Devices
    devices: any[];
    // Playlist
    currentTrack: string;
    currentPlayList: string;
  }

  interface AuthState {
    isAuthenticated: boolean;
  }
}
