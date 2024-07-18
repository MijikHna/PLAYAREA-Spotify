import { defineStore, StoreDefinition } from "pinia";
import { Device } from "@/types/spotify/device.types";
import { Track } from "@/types/spotify/track.types";
import { PlayList } from "@/types/spotify/playlist.types";

export const useSpotifyStore: StoreDefinition<"spotifyStore", SpotifyState, any, SpotifyActions> = defineStore("spotifyStore", {
  state: (): SpotifyState => ({
    // General
    auth: { loggedIn: false, token: null },
    // DOM
    dom: {
      spotifyPlayerDOMElem: null as HTMLScriptElement | null,
      spotifyPlayer: null as any,
    },
    // Player
    player: {
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
    },
  }),
  actions: {
    resetSpotifyPlayer() {
      // Playlist:
      this.player.playLists = [];
      this.player.activePlayList = null;
      this.player.playingContext = null;
      // Tracks
      this.player.currentTrack = null;
      this.player.nextTracks = [];
      //Devices
      this.player.devices = [];
      this.player.playerActive = false;
      // Player
      this.splayer.potifyPlayer = null;
      this.splayer.potifyPlayerDOMElem = null;
    },
  },
});

export interface SpotifyState {
  auth: { loggedIn: boolean; token: string };
  dom: {
    spotifyPlayerDOMElem: HTMLScriptElement;
    spotifyPlayer: any;
  };
  player: {
    playerActive: boolean;
    devices: Device[];
    currentTrack: Track;
    nextTracks: Track[];
    playingContext: any;
    activePlayList: PlayList;
    playLists: any[];
  };
}

export interface SpotifyActions {
  resetSpotifyPlayer: () => void;
}
