import { AbstractHttpService } from "./AbstractHttpService";
import { BackendHttpService } from "./BackendHttpService";

export class SpotifyHttpService extends AbstractHttpService {
  constructor() {
    super("https://api.spotify.com/v1/");
  }

  public async getAvailableDevices(): Promise<any> {
    const backendHttpSrv = new BackendHttpService();
    const backendResponse = await backendHttpSrv.getSavedSpotifyToken();

    this.http.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${backendResponse.data.token}`;

    const response = await this.http.get("/me/player/devices");
    return response.data.devices;
  }
}
