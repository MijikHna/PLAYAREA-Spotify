export interface CreateUser {
  id?: number;
  username: string;
  email: string;
  password: string;
  password_confirm: string;
  is_superuser?: false;
}

export interface ActiveUser {
  id: number;
  username: string;
  email: string;
}

export interface Profile {
  id: number;
  dark_theme: string;
  active_image: string;
  images: string[];
  user_id?: number;
}

export interface User {
  id: number;
  username?: string;
  email: string;
  profile: Profile;
}
