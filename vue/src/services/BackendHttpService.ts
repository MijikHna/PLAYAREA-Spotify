import { NewSheet, Table, TableInfo } from "@/types/sheet-app.types";
import axios, { AxiosInstance, AxiosResponse } from "axios";

export class BackendHttpService {
  private static instance: BackendHttpService;
  private httpInstance: AxiosInstance;


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
      (error) => {
        if (error.response.status === 401) {
          console.error("PLAYAREA: 401 error");
        }
        return Promise.reject(error);
      },
    );
  }

  static get http(): AxiosInstance {
    if (!BackendHttpService.instance) BackendHttpService.instance = new BackendHttpService();

    return BackendHttpService.instance.httpInstance;
  }

  // sheet
  public static async createSheet(newSheet: INewSheet): Promise<AxiosResponse<Table>> {
    this.setUserToken();
    return await this.http.post("/sheet/create", newSheet);
  }

  public static async getUserTables(): Promise<AxiosResponse<TableInfo[]>> {
    this.setUserToken();
    return await this.http.get("/sheet/tables");
  }

  public static async getTable(id: number): Promise<AxiosResponse<Table>> {
    this.setUserToken();
    return await this.http.get(`/sheet/tables/${id}`);
  }
}
