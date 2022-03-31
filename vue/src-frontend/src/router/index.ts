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
  if (!store.state.auth.isAuthenticated && to.path !== "/login") {
    return "/login";
  }

  if (store.state.auth.isAuthenticated && to.path === "/login") {
    return "/";
  }
});

export default router;
