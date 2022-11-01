declare module "@vue/runtime-core" {
  interface SpotifyState {
    // Spotify Player
    spotifyAuthSuccess: boolean;
    spotifyPlayerDOMElem: any | null;
    spotifyPlayer: any | null;
    // Devices
    playerActive: boolean;
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
