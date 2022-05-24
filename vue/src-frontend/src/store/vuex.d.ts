declare module "@vue/runtime-core" {
  interface SpotifyState {
    // Spotify Player
    spotifyAuthSuccess: boolean;
    spotifyPlayerSDKDOMElem: any | null;
    spotifyPlayer: any | null;
    // Devices
    thisPlayerActive: boolean;
    devices: any[];
    // Playlist
    currentTrack: any | null;
    nextTracks: any[];
    playingContext: any | null;
    playList: any | null;
  }

  interface AuthState {
    isAuthenticated: boolean;
  }
}
