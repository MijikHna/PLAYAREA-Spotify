import { AuthState } from "@vue/runtime-dom";
import { stat } from "fs";
import { DecodesUserToken } from "../interfaces/baseInterfaces";

export const auth = {
  state: () => ({
    activeUser: null,
    logoutTimer: null,
    isAuthenticated: false,
  }),
  getters: {
    activeUser(state: any) {
      return state.activeUser;
    },
    isAuthenticated(state: any) {
      return state.isAuthenticated;
    },
    logoutTimer(state: any) {
      return state.logoutTimer;
    },
  },
  mutations: {
    setAuth(state: any, authenticated: boolean) {
      state.isAuthenticated = authenticated;
    },
    setActiveUser(state: any, authUser: DecodesUserToken) {
      state.activeUser = authUser;
    },
    setActiveUserLogoutTimer(state: any, logoutTimerId: number) {
      state.logoutTimer = logoutTimerId;
    },
  },
};
