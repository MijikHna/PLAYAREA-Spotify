import axios, { AxiosInstance, AxiosResponse } from "axios";
import { BackendHttpService } from "./BackendHttpService";

export class SpotifyHttpService {
  private static http: AxiosInstance = axios.create({
    baseURL: "https://api.spotify.com/v1/",
    headers: {
      "Content-type": "application/json",
      Accept: "application/json",
    },
  });

  private static async setSpotifyApiToken(): Promise<void> {
    const response = await BackendHttpService.getSavedSpotifyToken();
    this.http.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${response.data.token}`;
  }

  public static async getAvailableDevices(): Promise<any> {
    await this.setSpotifyApiToken();
    const response = await this.http.get("/me/player/devices");

    return response.data.devices;
  }

  public static async selectPlayer(
    deviceIds: string[],
  ): Promise<AxiosResponse<any>> {
    await this.setSpotifyApiToken();

    try {
      return await this.http.put("me/player", {
        device_ids: deviceIds,
        play: false,
      });
    } catch (e) {
      throw e;
    }
  }

  public static async getCurrentPlaylist(playlistId: string): Promise<any> {
    this.setSpotifyApiToken();
    try {
      let response: AxiosResponse<any> = await this.http.get(
        `/playlists/${playlistId}`,
      );

      if (response.status !== 200) {
        throw Error;
      }

      const playList: any = response.data;

      while (playList.tracks.items.length < playList.tracks.total) {
        response = await this.http.get(
          `/playlists/${playlistId}/tracks?limit=50&offset=${playList.tracks.items.length}`,
        );

        if (response.status !== 200) {
          throw Error;
        }

        playList.tracks.items = playList.tracks.items.concat(
          response.data.items,
        );
      }

      return playList;
    } catch (e) {
      throw e;
    }
  }

  public static async playTrack(
    trackContext: string,
    playListPosition: number,
  ): Promise<any> {
    try {
      this.setSpotifyApiToken();
      const response: AxiosResponse<any> = await this.http.put(
        "me/player/play",
        {
          context_uri: trackContext,
          offset: {
            position: playListPosition,
          },
          position_ms: 0,
        },
      );

      if (response.status !== 204) {
        console.log("success");
        return response.data;
      }
    } catch (e) {
      throw e;
    }
  }
}
