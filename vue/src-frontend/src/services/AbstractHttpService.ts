import axios, { AxiosInstance } from "axios";

export abstract class AbstractHttpService {
  protected readonly http: AxiosInstance;

  protected constructor(protected readonly baseUrl: string) {
    this.http = axios.create({
      baseURL: baseUrl,
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
    });
  }
}
