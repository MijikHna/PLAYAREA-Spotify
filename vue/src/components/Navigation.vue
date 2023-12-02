<template>
  <header class="sticky top-0">
    <nav class="fixed-top">
      <Menubar :model="menuItems" class="navbar">
        <template #start>
          <router-link to="/" class="p-ml-2 text-2xl text-white bg-blue-600 border-round p-2 mr-2 no-underline"> Navbar
          </router-link>
        </template>
        <template #end>
          <div v-if="user" class="p-d-flex p-ai-center p-mr-2">
            <Avatar
              :image="user?.profile?.image ? (BACKEND_URL + '/static/' + user.profile.user_id + '/' + user.profile.image) : null"
              :label="!user?.profile?.image ? activeUser.user_identifier.charAt(0) : null" shape="circle"
              @click="goToProfile" class="mr-1 cursor-pointer" />
            <Button label="Logout" class="p-button-sm p-ml-2" @click="logout"></Button>
          </div>
        </template>
      </Menubar>
    </nav>
  </header>
</template>

<script setup lang="ts">
import Avatar from "primevue/avatar";
import Button from "primevue/button";
import Menubar from "primevue/menubar";

import { BackendHttpService } from "@/services/BackendHttpService";
import { useAuthStore } from "@/store/auth";
import { useUserStore } from "@/store/user";
import { computed } from "@vue/reactivity";
import { Router, useRouter } from "vue-router";
import { MenuItem } from "../types/app.types";

// global
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const router: Router = useRouter();
const userStore = useUserStore();
const authStore = useAuthStore();

const allMenuItems: MenuItem[] = [
  {
    label: "Home",
    icon: "pi pi-fw pi-home",
    url: "/",
  },
  {
    label: "Spotify",
    icon: "pi pi-fw pi-play",
    url: "/spotify/player",
  },
  {
    label: "Sheet",
    icon: "pi pi-fw pi-file",
    url: "/sheet",
  },
];

const menuItems = computed(() => {
  if (!user.value) return [];

  return allMenuItems;
});

const user = computed(() => userStore.user);
const activeUser = computed(() => authStore.activeUser);

const logout = async function () {
  const response = await BackendHttpService.http.post(`${BACKEND_URL}/auth/logout`);
  if (response.status !== 200) console.error("Error logging out")

  const expiredDate = new Date(0);

  document.cookie = `Authorization=; expires=${expiredDate.toUTCString()}`;
  //BackendHttpService.http.defaults.headers.common["Authorization"] = "";

  window.localStorage.removeItem("refreshToken");



  userStore.setUser(null);
  router.push("/login");
};

const goToProfile = function () {
  router.push({ name: "profile" });
};
</script>

<style scoped>
.navbar {
  height: 56px;
}
</style>
