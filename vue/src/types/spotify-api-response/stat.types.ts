// Spotify APP
export interface StatMenuItem {
  label?: string;
  icon?: string;
  item?: StatMenuItem[];
  command?: () => void;
}

export interface Track {
  id: string;
  name: string;
  image: { url: string; height: number; width: number };
  duration_min: number;
  popularity: number;
  release_date: string;
}

export interface Artist {
  id: string;
  name: string;
  image: { url: string; height: number; width: number };
  genres: string[];
  popularity: number;
}

export interface Album {
  id: string;
  name: string;
  image: { url: string; height: number; width: number };
  release_date: string;
  tracks: Track[];
}

export interface Playlist {
  id: string;
  name: string;
  image: { url: string; height: number; width: number };
  tracks: Track[];
}

// Spotify API Responses
export interface SpotifyAPICollectionsResponse {
  href: string;
  limit: number;
  next: string;
  offset: number;
  previous: string;
  total: number;
  items: SpotifyAPIItem[]
}


type SpotifyAPIItem = SpotifyAPIPlaylist | SpotifyAPIArtist | SpotifyAPITrack | SpotifyAPIPlaylistTrackCollectionResponse;

export interface SpotifyAPIArtist {
  external_urls: {
    spotify: string;
  },
  followers: {
    href: string | null;
    total: number;
  },
  genres: string[];
  href: string;
  id: string;
  images: [
    {
      height: number;
      url: string;
      width: number;
    }
  ],
  name: string;
  popularity: number;
  type: string;
  uri: string;
}

interface SpotifyAPIPlaylistTrackCollectionResponse {
  added_at: string;
  added_by: {
    external_urls: {
      spotify: string;
    },
    followers: {
      href: string;
      total: number;
    },
    href: string;
    id: string;
    type: string;
    uri: string;
  },
  is_local: boolean;
  track: SpotifyAPITrack;
}

export interface SpotifyAPITrack {
  album: {
    album_type: string;
    artists: [
      {
        external_urls: {
          spotify: string;
        },
        href: string;
        id: string;
        name: string;
        type: string;
        uri: string;
        genres: string[];
      }
    ],
    available_markets: string[];
    external_urls: {
      spotify: string;
    },
    href: string;
    id: string;
    images: [
      {
        height: number;
        url: string;
        width: number;
      }
    ],
    name: string;
    release_date: string;
    release_date_precision: string;
    total_tracks: number;
    type: string;
    uri: string;
  },
  artists: [
    {
      external_urls: {
        spotify: string;
      },
      href: string;
      id: string;
      name: string;
      type: string;
      uri: string;
    }
  ],
  available_markets: string[];
  disc_number: number;
  duration_ms: number;
  explicit: boolean;
  external_ids: {
    isrc: string;
  },
  external_urls: {
    spotify: string;
  },
  href: string;
  id: string;
  is_local: boolean;
  name: string;
  popularity: number;
  preview_url: string;
  track_number: number;
  type: string;
  uri: string;
}

export interface SpotifyAPIPlaylist {
  collaborative: false,
  description: string;
  external_urls: {
    spotify: string;
  },
  href: string;
  id: string;
  images: [
    {
      url: string;
      height: number;
      width: number;
    }
  ],
  name: string;
  owner: {
    external_urls: {
      spotify: string;
    },
    followers: {
      href: string;
      total: number;
    },
    href: string;
    id: string;
    type: string;
    uri: string;
    display_name: string;
  },
  public: boolean,
  snapshot_id: string;
  tracks: {
    href: string;
    total: number;
  },
  type: string;
  uri: string;
}

export interface SpotifyAPIAudioFeaturesResponse {
  audio_features: SpotifyAPIAudioFeatures[];
}

export interface SpotifyAPIAudioFeatures {
  danceability: number;
  energy: number;
  key: number;
  loudness: number;
  mode: number;
  speechiness: number;
  acousticness: number;
  instrumentalness: number;
  liveness: number;
  valence: number;
  tempo: number;
  id: string;
  uri: string;
  track_href: string;
  analysis_url: string;
  duration_ms: number;
  time_signature: number;
}
