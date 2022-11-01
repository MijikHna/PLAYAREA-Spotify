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

export interface UserCreate {
  id?: number;
  username: string;
  email: string;
  password: string;
  password_confirm: string;
  is_superuser?: false;
}

export interface User {
  id?: number;
  username: string;
  email: string;
}

export interface Profile {
  id?: number;
  theme: string;
  image: string;
  user_id: number;
}
