import { TrackResponse } from "./track.types";

export interface PlayList {
  id: string;
  name: string;
}

export interface PlayListResponse {
  description: string;
  external_urls: any;
  followers: { href: string; total: number };
  href: string;
  id: string;
  images: [{ url: string; height: number, width: number }];
  name: string;
  owner: {
    external_urls: { spotify: string };
    followers: { href: "string", "total": 0 };
    href: string;
    id: string;
    type: string;
    uri: string;
    display_name: string;
  },
  public: boolean;
  snapshot_id: string;
  tracks: {
    href: string;
    limit: number;
    next: string;
    offset: number;
    previous: string;
    total: number;
    items: [
      {
        added_at: string;
        added_by: any;
        is_local: boolean;
        track: TrackResponse;
      }
    ]
  },
  type: string;
  uri: string;
}

export interface PlayListsResponse {
  href: string
  limit: number,
  next: string;
  offset: number,
  previous: number;
  total: number,
  items: PlayListResponse[]
}
