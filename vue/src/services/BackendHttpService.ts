import { NewSheet, Table, TableInfo } from "@/types/sheet-app.types";
import axios, { AxiosInstance, AxiosResponse } from "axios";

export class BackendHttpService {
  private static instance: BackendHttpService;
  private httpInstance: AxiosInstance;

  //NOTE: eventually add retry


  constructor() {
    this.httpInstance = axios.create({
      baseURL: `${process.env.VUE_APP_BACKEND_URL}`,
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      withCredentials: true,
    });

    this.httpInstance.interceptors.response.use(
      (response: AxiosResponse) => response,
      async (error) => {
        if (error.response.status === 401) {
          const response = await this.httpInstance.post('/auth/renew-token', { renew_token: this.getRefreshTokenFromCookie() }, { withCredentials: true });
          if (response.status === 200) return response;

          return Promise.reject(error)
        }
        return Promise.reject(error);
      },
    );
  }

  static get http(): AxiosInstance {
    if (!BackendHttpService.instance) BackendHttpService.instance = new BackendHttpService();

    return BackendHttpService.instance.httpInstance;
  }

  getRefreshTokenFromCookie(): string {
    return document.cookie.split(';').find(cookie => cookie.startsWith('refresh_token')).split(':').at(1).trim();
  }

  // sheet
  public static async createSheet(newSheet: INewSheet): Promise<AxiosResponse<Table>> {
    return await this.http.post("/sheet/create", newSheet);
  }

  public static async getUserTables(): Promise<AxiosResponse<TableInfo[]>> {
    return await this.http.get("/sheet/tables");
  }

  public static async getTable(id: number): Promise<AxiosResponse<Table>> {
    return await this.http.get(`/sheet/tables/${id}`);
  }
}
