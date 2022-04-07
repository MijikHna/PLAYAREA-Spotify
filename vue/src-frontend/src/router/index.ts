import { UtilsServcie } from "@/services/UtilsService";

import { AuthUser } from "@/interfaces/interfaces";
import {
  createRouter,
  createWebHistory,
  Router,
  RouteRecordRaw,
} from "vue-router";

import store from "../store";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/spotify",
    name: "Spotify",
    component: () => import("@/views/Spotify.vue"),
    beforeEnter: (to: any) => {
      if (to.query?.spotify_auth) {
        store.commit(
          "setSpotifyAuthSuccess",
          to.query.spotify_auth.toLowerCase() === "true",
        );

        return { path: to.path, query: {}, hash: to.hash };
      }
    },
  },
  {
    path: "/excel",
    name: "Excel",
    component: () => import("@/views/Excel.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/views/About.vue"),
  },
];

const router: Router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to: any, from: any) => {
  let authToken: AuthUser | null = UtilsServcie.getDecodedAuthCookie();

  if (!authToken && to.path !== "/login") {
    return "/login";
  }

  if (!authToken && to.path === "/login") {
    return;
  }

  const now = new Date();
  const expDate = new Date(authToken.exp * 1000);

  if (now > expDate && to.path !== "/login") {
    return "/login";
  }

  if (!store.state.auth.isAuthenticated) {
    store.commit("setActiveUser", authToken);
    store.commit("setAuth", true);
  }

  if (to.path === "/login") {
    return "/";
  }
});

export default router;
