import { User } from "@/types/user.types";
import { Store, defineStore } from "pinia";

export const useUserStore: () => Store<"userStore", UserState, any, UserActions> = defineStore("userStore", {
  state: () => ({
    user: null as User | null,
  }),
  actions: {
    setUser(user: User) {
      this.user = user;
    },
  },
});

export interface UserState {
  user: User;
}

export interface UserActions {
  setUser(user: User): void;
}
