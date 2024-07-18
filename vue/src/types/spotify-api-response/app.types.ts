export interface SpotifyWindow extends Window {
  Spotify: {
    Player: any;
  };
  onSpotifyWebPlaybackSDKReady(): void;
}

export interface DeviceMenuEntry {
  deviceId: string;
  active: boolean;
  label: string;
  icon: string;
  command(): void;
  key?: object;
}

export interface SpotifyTabMenuItem {
  label: string;
  icon: string;
  to: string;
}

