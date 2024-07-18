declare global {
  interface Window {
    Spotify: {
      Player: any;
    };
    onSpotifyWebPlaybackSDKReady: () => void;
  }
}
