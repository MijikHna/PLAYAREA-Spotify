import { Buffer } from "buffer";

export class UtilsService {
  static decodeCookieToken = <T>(cookieName: string): T | null => {
    const cookies = document.cookie.split("; ");

    let decodedUserToken: T | null = null;

    const cookie = cookies.find((cookie) => cookie.startsWith(cookieName))?.split("=")[1];

    if (cookie) {
      decodedUserToken = JSON.parse(Buffer.from(cookie.split(".")[1], "base64").toString("utf-8"));
    }
    return decodedUserToken;
  };

  static getCookieValue = (cookieName: string): string => {
    const cookies = document.cookie.split("; ");

    const cookie: string | null = cookies.find((cookie) => cookie.startsWith(cookieName));

    if (!cookie) return null;

    return cookie.split("=")[1];
  };

  static isTokenExpired = (expDate: number): boolean => {
    const now = new Date();
    const exp = new Date(expDate * 1000);

    return now > exp;
  };

  static deleteCookie = (cookieName: string): void => {
    const cookies = document.cookie.split("; ");
    if (cookies.find((cookie) => cookie.startsWith(cookieName))) {
      document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC;`;
    }
  };
}
