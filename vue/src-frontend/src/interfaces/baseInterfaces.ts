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

export interface IUser {
  id?: number;
  email: string;
  first_name: string;
  last_name: string;
  avatar: string;
}

interface RequestInterface {
  page: number;
  per_page: number;
  total: number;
  total_pages: number;
  data: IUser[];
}

export class UserDTO implements IUser {
  id?: number;
  avatar: string = "";
  email: string = "";
  first_name: string = "";
  last_name: string = "";
}

export default class User extends UserDTO {
  constructor(dto: UserDTO) {
    super();
    Object.assign(this, dto);
  }

  get fullName(): string {
    return `${this.first_name} ${this.last_name}`;
  }
}
