import { AuthState } from "@vue/runtime-dom";

export const auth = {
  state: () => ({
    isAuthenticated: false,
  }),
  mutations: {
    setAuth(state: AuthState, authenticated: boolean) {
      state.isAuthenticated = authenticated;
    },
  },
};
