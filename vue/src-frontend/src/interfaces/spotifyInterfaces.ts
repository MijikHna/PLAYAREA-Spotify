export interface ITrack {
  name: string;
  duration: string;
}

export interface ITrackList {
  name: string;
  tracks: ITrack[];
}
