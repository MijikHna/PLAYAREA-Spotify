import axios, { AxiosError, AxiosInstance, AxiosResponse } from "axios";

export class SpotifyHttpService {
  private static instance: SpotifyHttpService;
  private httpInstance: AxiosInstance;


  constructor() {
    if (SpotifyHttpService.instance) return SpotifyHttpService.instance;

    this.httpInstance = axios.create({
      baseURL: "https://api.spotify.com/v1/",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
    });

    // user interceptor to handle 401 error
    this.httpInstance.interceptors.response.use(
      (response: AxiosResponse) => response,
      (error: AxiosError) => {
        if (error.response.status === 401) {
          console.error("Spotify: 401 error");
        }
        return Promise.reject(error);
      },
    );
  }

  static get http(): AxiosInstance {
    if (!SpotifyHttpService.instance) SpotifyHttpService.instance = new SpotifyHttpService();

    return SpotifyHttpService.instance.httpInstance;
  }

  public static async getCurrentPlaylist(playlistId: string): Promise<any> {
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
}
