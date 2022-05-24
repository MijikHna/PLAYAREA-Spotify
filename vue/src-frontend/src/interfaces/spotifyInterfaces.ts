export interface ITrack {
  name: string;
  duration: string;
}

export interface ITrackList {
  name: string;
  tracks: ITrack[];
}

export interface IDeviceMenuEntry {
  deviceId: string;
  active: boolean;
  label: string;
  icon: string;
  command(): void;
  key: object;
}

export interface ISpotifyTabMenuItems {
  label: string;
  icon: string;
  to: string;
}
