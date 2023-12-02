import { defineStore, StoreDefinition } from "pinia";
import { Device } from "@/types/spotify/device.types";
import { Track } from "@/types/spotify/track.types";
import { PlayList } from "@/types/spotify/playlist.types";

export const useSpotifyStore:
  StoreDefinition<'spotifyStore', SpotifyState, any, SpotifyActions> = defineStore("spotifyStore", {
    state: (): SpotifyState => ({
      // General
      loggedIn: false as boolean,
      // Player
      spotifyPlayerDOMElem: null as HTMLScriptElement,
      spotifyPlayer: null as any,
      // Devices
      playerActive: false as boolean,
      devices: [] as Device[],
      // Tracks
      currentTrack: null as Track,
      nextTracks: [] as Track[],
      //Playlist:
      playingContext: null as any,
      activePlayList: null as PlayList,
      playLists: [] as PlayList[],
    }),
    actions: {
      resetSpotifyPlayer() {
        // Playlist:
        this.playLists = [];
        this.activePlayList = null;
        this.playingContext = null;
        // Tracks
        this.currentTrack = null;
        this.nextTracks = [];
        //Devices
        this.devices = [];
        this.playerActive = false;
        // Player
        this.spotifyPlayer = null;
        this.spotifyPlayerDOMElem = null;
      },
    },
  });

export interface SpotifyState {
  loggedIn: boolean;
  spotifyPlayerDOMElem: HTMLScriptElement;
  spotifyPlayer: any;
  playerActive: boolean;
  devices: Device[];
  currentTrack: Track;
  nextTracks: Track[];
  playingContext: any;
  activePlayList: PlayList;
  playLists: any[];
}

export interface SpotifyActions {
  resetSpotifyPlayer(): void;
}
