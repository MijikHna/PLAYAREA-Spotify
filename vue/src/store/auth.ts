import { DecodesUserToken } from "@/interfaces/auth.types";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    activeUser: null,
  }),
  actions: {
    setActiveUser(authUser: DecodesUserToken) {
      this.activeUser = authUser;
    },
  },
});
