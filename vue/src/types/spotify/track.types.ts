export interface Track {
  name: string;
  duration: string;
}

export interface TrackList {
  name: string;
  tracks: Track[];
}

export interface TrackResponse {
  album: any;
  artists: any[];
  available_markets: string[];
  disc_number: number;
  duration_ms: number;
  explicit: false;
  external_ids: any;
  external_urls: any;
  href: string;
  id: string;
  is_playable: boolean;
  linked_from: any;
  restrictions: any;
  name: string;
  popularity: number,
  preview_url: string,
  track_number: number,
  type: string,
  uri: string,
  is_local: false
}

