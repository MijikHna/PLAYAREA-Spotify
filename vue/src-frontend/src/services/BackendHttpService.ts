import { User, UserCreate, UserToken } from "@/interfaces/baseInterfaces";
import { UtilsService } from "./UtilsService";

import axios, { AxiosInstance, AxiosResponse } from "axios";
import { INewSheet, Table } from "@/interfaces/sheetInterfaces";

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
    const userToken: UserToken | null = UtilsService.getAuthToken();

    if (userToken) {
      this.http.defaults.headers.common[
        "Authorization"
      ] = `${userToken.tokenType} ${userToken.accessToken}`;
    }
  }

  public static async getUserProfile(username: string): Promise<AxiosResponse> {
    this.setUserToken();
    return await BackendHttpService.http.get(`/users/${username}`);
  }

  public static async updateUserProfile(
    userProfile: any,
  ): Promise<AxiosResponse> {
    this.setUserToken();
    return await BackendHttpService.http.put("/profiles", userProfile);
  }

  public static async addPicture(image: any): Promise<AxiosResponse> {
    this.setUserToken();
    return await BackendHttpService.http.post("profiles/picture", image, {
      headers: { "Content-type": "multipart/form-data" },
    });
  }
  // spotify
  public static async getSavedSpotifyToken(): Promise<any> {
    this.setUserToken();
    return await BackendHttpService.http.get("/spotify/get-token");
  }

  public static async loginToSpotify(): Promise<any> {
    this.setUserToken();
    return await BackendHttpService.http.get<any>("/spotify/login");
  }

  public static async logOutFromSpotify(): Promise<AxiosResponse<void>> {
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

  // sheet
  public static async createSheet(
    newSheet: INewSheet,
  ): Promise<AxiosResponse<Table>> {
    this.setUserToken();
    return await this.http.post("/sheet/create", newSheet);
  }

  public static async getUserTables(): Promise<AxiosResponse<string[]>> {
    this.setUserToken();
    return await this.http.get("/sheet/tables");
  }
}
