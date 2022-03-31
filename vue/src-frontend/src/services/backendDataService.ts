import axios, { AxiosInstance } from "axios";

export class BackendDataService {
  private static backendApi = axios.create({
    baseURL: `${process.env.VUE_APP_BACKEND_URL}`,
    headers: {
      "Content-type": "application/json",
    },
  });

  // returns Promise
  static getSavedSpotifyToken(): Promise<any> {
    return this.backendApi.get(`/spotify/get-token`);
  }

  // returns response
  static async getSavedSpotifyTokenAsync(): Promise<any> {
    return await this.backendApi.get<any>(`/spotify/get-token`);
  }
}
