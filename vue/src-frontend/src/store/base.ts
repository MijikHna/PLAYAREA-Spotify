import { BaseState } from "@/interfaces/baseInterfaces";

export const base = {
  state() {
    return {
      theme: "light",
    };
  },
  mutations: {
    setTheme(state: BaseState, theme: string) {
      state.theme = theme;
    },
  },
};
