export interface Track {
  name: string;
  duration: string;
}

export interface TrackList {
  name: string;
  tracks: Track[];
}
