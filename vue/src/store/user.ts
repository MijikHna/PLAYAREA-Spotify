import { Profile, User } from "@/types/user.types";
import { Store, defineStore } from "pinia";

export const useUserStore: () => Store<"userStore", State>
  = defineStore<"userStore", State>("userStore", {
    state: (): State => ({
      user: null as User | null,
    }),
    actions: {
      setUser(user: User) {
        this.user = user;
      },
      setUserProfile(userProfile: Profile) {
        this.user.profile = userProfile;
      },
    },
  });

export interface State {
  user: User | null;
}
