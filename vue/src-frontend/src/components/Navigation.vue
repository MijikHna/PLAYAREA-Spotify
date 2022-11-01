<template>
  <header>
    <nav class="fixed-top">
      <Menubar :model="menuItems" class="navbar rounded-0">
        <template #start>
          <router-link to="/" class="navbar-brand"> Navbar </router-link>
        </template>
        <template #end>
          <div v-if="activeUser.user">
            <div class="d-inline-block pointer" @click="goToProfile">
              <Avatar
                v-if="activeUser.profile?.image"
                :image="
                  BACKEND_URL +
                  '/static/' +
                  activeUser.profile.user_id +
                  '/' +
                  activeUser.profile.image
                "
                shape="circle"
              />
              <Avatar
                v-else
                :label="activeUser.user.username.charAt(0)"
                shape="circle"
              />
            </div>
            <Button
              label="Logout"
              class="ms-3 p-button-sm"
              @click="logout"
            ></Button>
          </div>
        </template>
      </Menubar>
    </nav>
  </header>
</template>

<script setup lang="ts">
import Menubar from "primevue/menubar";
import Avatar from "primevue/avatar";
import Button from "primevue/button";

import { useAuthStore } from "@/store/auth";

import { MenuItem } from "../interfaces/baseInterfaces";
import { computed } from "@vue/reactivity";
import { useRouter, Router } from "vue-router";

// global
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const router: Router = useRouter();
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
  if (!activeUser.value) return [];

  return allMenuItems;
});

const activeUser = computed(() => authStore.activeUser);

const logout = function () {
  const expiredDate = new Date(0);

  document.cookie = `Authorization=; expires=${expiredDate.toUTCString()}`;

  authStore.setActiveUser(null);
  authStore.setActiveUserProfile(null);

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
.pointer {
  cursor: pointer;
}
</style>
