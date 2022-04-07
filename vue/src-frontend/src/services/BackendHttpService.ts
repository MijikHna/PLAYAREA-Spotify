import { UserToken } from "@/interfaces/baseInterfaces";
import { AbstractHttpService } from "./AbstractHttpService";
import { UtilsServcie } from "./UtilsService";

export class BackendHttpService extends AbstractHttpService {
  constructor() {
    super(`${process.env.VUE_APP_BACKEND_URL}`);

    const userToken: UserToken | null = UtilsServcie.getAuthToken();

    if (userToken) {
      this.http.defaults.headers.common[
        "Authorization"
      ] = `${userToken.tokenType} ${userToken.accessToken}`;
    }
  }

  // returns Promise
  public getSavedSpotifyToken(): Promise<any> {
    return this.http.get(`/spotify/get-token`);
  }

  // returns response
  public async getSavedSpotifyTokenAsync(): Promise<any> {
    return await this.http.get<any>(`/spotify/get-token`);
  }

  public async loginToSpotify(): Promise<any> {
    return await this.http.get<any>("/spotify/login");
  }
}
