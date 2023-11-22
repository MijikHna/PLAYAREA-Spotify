import { DecodedUserToken, UserToken } from "@/types/auth.types";
import { Buffer } from "buffer";

export class UtilsService {
  static getDecodedAuthCookie = (): DecodedUserToken => {
    const cookies = document.cookie.split("; ");

    let decodedUserToken: DecodedUserToken = null;

    cookies.every((cookie) => {
      if (cookie.startsWith("Authorization=")) {
        const token: string = cookie.split("=")[1];

        decodedUserToken = JSON.parse(Buffer.from(token.split(".")[1], "base64").toString("utf-8"));
        return false;
      }

      return true;
    });

    return decodedUserToken;
  };

  static getAuthToken = (): UserToken => {
    const cookies = document.cookie.split("; ");

    let userToken: UserToken = null;

    cookies.every((cookie) => {
      if (cookie.startsWith("Authorization")) {
        const token: any = JSON.parse(cookie.split("=")[1]);
        userToken = {
          accessToken: token.access_token,
          tokenType: token.token_type,
        };
        return false;
      }
      return true;
    });

    return userToken;
  };
}
