import { User, UserCreate, UserToken } from "@/interfaces/baseInterfaces";
import { UtilsServcie } from "./UtilsService";

import axios, { AxiosInstance, AxiosResponse } from "axios";

export class BackendHttpService {
  private static http: AxiosInstance = axios.create({
    baseURL: `${process.env.VUE_APP_BACKEND_URL}`,
    headers: {
      "Content-type": "application/json",
      Accept: "application/json",
    },
  });
  // base
  public static async setUserToken() {
    const userToken: UserToken | null = UtilsServcie.getAuthToken();

    if (userToken) {
      this.http.defaults.headers.common[
        "Authorization"
      ] = `${userToken.tokenType} ${userToken.accessToken}`;
    }
  }
  // spotify
  public static async getSavedSpotifyToken(): Promise<any> {
    this.setUserToken();
    return await BackendHttpService.http.get(`/spotify/get-token`);
  }

  public static async loginToSpotify(): Promise<any> {
    this.setUserToken();
    return await BackendHttpService.http.get<any>("/spotify/login");
  }

  public static async lougOutFromSpotify(): Promise<AxiosResponse<void>> {
    this.setUserToken();
    return await BackendHttpService.http.delete("/spotify/logout");
  }

  // user
  public static async createUser(
    user: UserCreate,
  ): Promise<AxiosResponse<User>> {
    this.setUserToken();
    return await BackendHttpService.http.post<User>("/users/create", user);
  }
}
