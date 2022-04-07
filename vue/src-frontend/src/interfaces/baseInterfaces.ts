export interface MenuItem {
  label: string;
  icon: string;
  url: string;
}

export interface App {
  name: string;
  url: string;
  image: string;
}

export interface DecodesUserToken {
  username: string;
  exp: number;
}

export interface UserToken {
  accessToken: string;
  tokenType: string;
}
