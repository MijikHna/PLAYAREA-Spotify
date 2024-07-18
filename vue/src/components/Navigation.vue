<template>
  <header class="sticky top-0 z-50">
    <nav>
      <Menubar :model="menuItems" class="navbar">
        <template #start>
          <router-link to="/" class="rounded-lg no-underline">
            <i class="pi pi-fw pi-home"></i>
          </router-link>
        </template>
        <template #item="{ item, props, hasSubmenu }">
          <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
              <span :class="item.icon" />
              <span class="ml-2"> {{ item.label }}</span>
            </a>
          </router-link>
          <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
            <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down ml-2" />
          </a>
        </template>
        <template #end>
          <div v-if="user" class="p-d-flex p-ai-center p-mr-2">
            <Avatar
              :image="user?.profile?.image ? BACKEND_URL + '/static/' + user.profile.user_id + '/' + user.profile.image : null"
              :label="!user?.profile?.image ? user.email.charAt(0) : null"
              shape="circle"
              @click="goToProfile"
              class="mr-1 cursor-pointer"
            />
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
  import { useUserStore } from "@/store/user";
  import { computed } from "@vue/reactivity";
  import { Router, useRouter } from "vue-router";
  import { MenuItem } from "../types/app.types";
  import { useSpotifyStore } from "@/store/spotify";
import { Ref } from "vue";
import { ref } from "vue";

  // global
  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

  const router: Router = useRouter();
  const userStore = useUserStore();
  const spotifyStore = useSpotifyStore();

  // data
  const allMenuItems: Ref<MenuItem[]> = ref<MenuItem[]>([
    {
      label: "Spotify",
      icon: "pi pi-fw pi-play",
      hasSubmenu: true,
      items: [
        {
          label: "Player",
          icon: "pi pi-fw pi-volume-up",
          route: "/player",
        },
        {
          label: "Library",
          icon: "pi pi-fw pi-list",
          route: "/library",
        },
        {
          label: "Stats",
          icon: "pi pi-fw pi-star",
          route: "/stats",
        },
      ],
    },
    {
      label: "About",
      icon: "pi pi-fw pi-info-circle",
      route: "/about",
    },
    {
      label: "Profile",
      icon: "pi pi-fw pi-user",
      route: "/profile",
    },
  ]);

  // computed
  const menuItems = computed(() => {
    if (!user.value || !spotifyStore.auth.loggedIn) return [];

    return allMenuItems.value;
  });

  const user = computed(() => userStore.user);

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
