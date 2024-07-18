export interface App {
  name: string;
  url: string;
  image: string;
}

export interface MenuItem {
  label: string;
  icon: string;
  hasSubmenu?: boolean;
  // TODO: exactly one of these should be defined
  route?: string;
  items?: MenuItem[];
}

class Test {
      constructor() { }
}
