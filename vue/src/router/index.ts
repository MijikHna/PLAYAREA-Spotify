import { UtilsService } from "@/services/UtilsService";

import { createRouter, createWebHistory, RouteLocationNormalized, Router, RouteRecordRaw } from "vue-router";

import { BackendHttpService } from "@/services/BackendHttpService";
import { useAuthStore } from "@/store/auth";
import { useUserStore } from "@/store/user";
import { DecodedUserToken } from "@/types/auth.types";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "app",
    component: () => import("@/views/AppHome.vue"),
    redirect: { name: "home" },
    beforeEnter: async (to: RouteLocationNormalized, from: RouteLocationNormalized) => {
      // check if cookie "Authorization" exists
      const userToken = document.cookie.split(";").find((item) => item.trim().startsWith("Authorization="));

      if (!userToken) return { name: "login" };

      const authStore = useAuthStore();
      const userStore = useUserStore();

      const decodedToken = UtilsService.getDecodedAuthCookie();

      // set active user from cookie in auth store
      authStore.setActiveUser(decodedToken);

      // get user profile from backend
      const response = await BackendHttpService.http.get(`/users/profile/${decodedToken.id}`);

      userStore.setUser({ id: decodedToken.id });
      userStore.setUserProfile(response.data);
    },
    children: [
      {
        path: "/home",
        name: "home",
        component: () => import("@/views/Home.vue"),
      },
      {
        path: "/spotify",
        name: "spotify",
        component: () => import("@/views/Spotify.vue"),
        children: [
          {
            path: "player",
            name: "player",
            component: () => import("@/views/Spotify/Player.vue"),
          },
          {
            path: "discover",
            name: "discover",
            redirect: { name: "playlists" },
            component: () => import("@/views/Spotify/Discover.vue"),
            children: [
              {
                path: "playlists",
                name: "playlists",
                component: () => import("@/components/Spotify/Discover/PlayListList.vue"),
              },
              {
                path: "artists",
                name: "artists",
                component: () => import("@/components/Spotify/Discover/ArtistList.vue"),
              },
              {
                path: "albums",
                name: "albums",
                component: () => import("@/components/Spotify/Discover/AlbumList.vue"),
              },
              {
                path: "tracks",
                name: "tracks",
                component: () => import("@/components/Spotify/Discover/TrackList.vue"),
              },
              // NOTE: maybe Search
            ],
          },
          {
            name: "stats",
            path: "stats",
            component: () => import("@/views/Spotify/Stats.vue"),
          },
        ],
      },
      {
        path: "/sheet",
        name: "sheet",
        component: () => import("@/views/Sheet.vue"),
      },
      {
        path: "/about",
        name: "about",
        component: () => import("@/views/About.vue"),
      },
      {
        path: "/profile",
        name: "profile",
        component: () => import("@/views/Profile.vue"),
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/test",
    name: "test",
    component: () => import("@/views/Test.vue"),
  },
];

const router: Router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to: any, from: any) => {
  // check if token is expired
  const authStore = useAuthStore();

  let authToken: DecodedUserToken | null = UtilsService.getDecodedAuthCookie();

  // go to login if no token
  if (!authToken && to.path !== "/login") return { name: "login" };
  if (!authToken && to.path === "/login") return;

  // go to login if token expired
  const now = new Date();
  const expDate = new Date(authToken.exp * 1000);

  if (now > expDate && to.path !== "/login") {
    authStore.setActiveUser(null);
    document.cookie = `Authorization=; expires=${now.toUTCString()}`;
    return { name: "login" };
  }

  // go to home if on login page (already logged in)
  if (to.path === "/login") return { name: "home" };
});

export default router;
