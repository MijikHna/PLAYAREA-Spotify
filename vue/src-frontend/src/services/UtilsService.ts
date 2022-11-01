import { DecodesUserToken, UserToken } from "@/interfaces/baseInterfaces";
import { Buffer } from "buffer";

export class UtilsService {
  static getDecodedAuthCookie = (): DecodesUserToken => {
    const cookies = document.cookie.split("; ");

    let decodedUserToken: DecodesUserToken = null;

    cookies.every((cookie) => {
      if (cookie.startsWith("Authorization")) {
        const token: any = JSON.parse(cookie.split("=")[1]);
        decodedUserToken = JSON.parse(
          Buffer.from(token.access_token.split(".")[1], "base64").toString(
            "utf-8",
          ),
        );
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
