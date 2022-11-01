import { defineStore } from "pinia";
import { DecodesUserToken, Profile, User } from "../interfaces/baseInterfaces";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    activeUser: {
      user: null,
      profile: null,
    } as { user: User; profile: Profile },
  }),
  actions: {
    setActiveUser(authUser: DecodesUserToken) {
      this.activeUser.user = authUser;
    },
    setActiveUserProfile(userProfile: Profile) {
      this.activeUser.profile = userProfile;
    },
  },
});
