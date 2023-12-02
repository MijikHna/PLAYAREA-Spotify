import { Buffer } from "buffer";

import { createRouter, createWebHistory, RouteLocationNormalized, Router, RouteRecordRaw } from "vue-router";

import { useAuthStore } from "@/store/auth";
import { useUserStore } from "@/store/user";

import { UtilsService } from "@/services/UtilsService";
import { BackendHttpService } from "@/services/BackendHttpService";
import { DecodedUserToken } from "@/types/auth.types";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "app",
    component: () => import("@/views/AppHome.vue"),
    redirect: { name: "home" },
    beforeEnter: async (to: RouteLocationNormalized, from: RouteLocationNormalized) => {
      // check if cookie "Authorization" exists
      console.log('to home');
      const userToken = document.cookie.split(";").find((item) => item.trim().startsWith("Authorization="));

      if (!userToken) return { name: "login" };

      // set active user and user profile
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
            redirect: { name: "my-top" },
            component: () => import("@/views/Spotify/Stats.vue"),
            children: [
              {
                name: "my-top",
                path: "my-top",
                component: () => import("@/components/Spotify/Stats/UserStats.vue"),
              },
              {
                name: "playlist-stats",
                path: "playlist-stats",
                component: () => import("@/components/Spotify/Stats/PlaylistStats.vue"),
              },
            ],
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
  console.log('before each');
  const authStore = useAuthStore();

  let authToken: DecodedUserToken | null = UtilsService.getDecodedAuthCookie();
  let tokenExpired = false;

  // check if token is expired
  if (authToken) {
    const now = new Date();
    const expDate = new Date(authToken.exp * 1000);

    tokenExpired = now > expDate;
  }

  if (!authToken || tokenExpired) {
    // if no token or token expired, check if refresh token exists
    const refreshToken = window.localStorage.getItem('refreshToken');

    if (!refreshToken) {
      authStore.setActiveUser(null);
      document.cookie = `Authorization=; expires=${new Date().toUTCString()}`;

      if (to.path !== '/login') return { name: "login" };
      if (to.path === '/login') return;
    }
    // refresh token
    console.log('token expired, refreshing...')
    const response = await BackendHttpService.http.post("/auth/token_renew", { refresh_token: window.localStorage.getItem('refreshToken') });

    if (response.status === 200) {
      const tokenInfo: DecodedUserToken =
        JSON.parse(Buffer.from(response.data.access_token.split(".")[1], "base64").toString("utf-8"));

      const authCoookieExpDate = new Date(tokenInfo.exp * 1000).toUTCString();

      document.cookie = `Authorization=${response.data.access_token}; expires=${authCoookieExpDate}`;

      // handle refresh token
      window.localStorage.setItem("refreshToken", response.data.refresh_token);

      return from.path;
    }

    window.localStorage.removeItem('refreshToken');

    if (to.path !== '/login') return { name: "login" };
    if (to.path === '/login') return;
  }

  // go to home if on login page (already logged in)
  if (to.path === "/login") return { name: "home" };
});

export default router;
