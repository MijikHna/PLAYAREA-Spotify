import { Buffer } from "buffer";

import { createRouter, createWebHistory, RouteLocationNormalizedGeneric, Router, RouteRecordRaw } from "vue-router";

import { useUserStore } from "@/store/user";

import { UtilsService } from "@/services/UtilsService";
import { BackendHttpService } from "@/services/BackendHttpService";
import { DecodedUserToken } from "@/types/auth.types";
import { ToastServiceMethods } from "primevue/toastservice";
import { useToast } from "primevue/usetoast";
import { AxiosResponse } from "axios";
import { Profile } from "@/types/user.types";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "spotify",
    component: () => import("@/views/Spotify.vue"),
    redirect: { name: "home" },
    children: [
      {
        path: "/home",
        name: "home",
        component: () => import("@/views/Home.vue"),
      },
      {
        path: "/player",
        name: "player",
        component: () => import("@/views/Player.vue"),
      },
      {
        path: "/library",
        name: "library",
        component: () => import("@/views/Library.vue"),
      },
      {
        path: "/stats",
        name: "stats",
        redirect: { name: "my-top" },
        component: () => import("@/views/Stats.vue"),
        children: [
          {
            name: "my-top",
            path: "my-top",
            component: () => import("@/components/spotify/Stats/UserStats.vue"),
          },
          {
            name: "playlist-stats",
            path: "playlist-stats",
            component: () => import("@/components/spotify/Stats/PlaylistStats.vue"),
          },
        ],
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/Login.vue"),
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
];

const router: Router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to: RouteLocationNormalizedGeneric) => {
  // check if token is expired

  let authToken: DecodedUserToken | null = UtilsService.decodeCookieToken("Authorization");

  // if no token or token expired, check if refresh token exists
  if (!authToken || UtilsService.isTokenExpired(authToken.exp)) {
    const refreshToken = UtilsService.getCookieValue("RefreshToken");
    if (!refreshToken) {
      const userStore = useUserStore();
      userStore.setUser(null);

      if (to.path !== "/login") return { name: "login" };
      if (to.path === "/login") return;
    }

    // refresh token
    console.log("token expired, refreshing...");
    try {
      const response = await BackendHttpService.http.post("/auth/token_renew", {
        refresh_token: refreshToken,
      });
      if (response.status === 200) {
        const tokenInfo: DecodedUserToken = JSON.parse(Buffer.from(response.data.access_token.split(".")[1], "base64").toString("utf-8"));
        const authCoookieExpDate = new Date(tokenInfo.exp * 1000).toUTCString();
        document.cookie = `Authorization=${response.data.access_token}; expires=${authCoookieExpDate}`;

        const refreshTokenInfo: any = JSON.parse(Buffer.from(response.data.refresh_token.split(".")[1], "base64").toString("utf-8"));
        const refreshCookieExpDate = new Date(refreshTokenInfo.exp * 1000).toUTCString();
        document.cookie = `RefreshToken=${response.data.refresh_token}; expires=${refreshCookieExpDate}`;

        const profileResponse: AxiosResponse<Profile> = await BackendHttpService.http.get(`/user/profile/${tokenInfo.id}`);

        if (profileResponse.status === 200) {
          const profile: Profile = profileResponse.data;
          console.log("profile", profile);
          const userStore = useUserStore();
          userStore.setUser({
            id: tokenInfo.id,
            email: tokenInfo.user_identifier,
            profile: profile,
          });

          if (to.path !== "/name") return { name: "home" };
          return;
        }
      }
    } catch (error) {
      UtilsService.deleteCookie("Authorization");
      UtilsService.deleteCookie("RefreshToken");
      return { name: "login" };
    }
  }
});

export default router;
