<template>

  <header>
    <nav class="fixed-top">
      <Menubar :model="menuItems" class="navbar rounded-0">
        <template #start>
          <router-link to="/" class="navbar-brand">
            Navbar
          </router-link>
        </template>
        <template #end>
          <div v-if="isAuthenticated">
            <Avatar :label="activeUser.username.charAt(0)" shape="circle"/>
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

<script lang="ts">
import Menubar from "primevue/menubar";
import Avatar from 'primevue/avatar';
import Button from "primevue/button";

import { defineComponent } from "vue";
import { MenuItem } from "../interfaces/baseInterfaces";
import { useStore } from "vuex";
import { computed } from "@vue/reactivity";
import { useRouter, Router } from "vue-router";

export default defineComponent({
  name: "Navigation",
  components: { Menubar, Avatar, Button },
  setup(){
    const store = useStore();
    const router: Router = useRouter();

    const allMenuItems: MenuItem[] = [
      {
        label: "Home",
        icon: "pi pi-fw pi-home",
        url: "/",
      },
      {
        label: "Spotify",
        icon: "pi pi-fw pi-play",
        url: "/spotify/player"
      },
      {
        label: "Excel",
        icon: "pi pi-fw pi-file",
        url: "/excel"
      }
    ];

    const menuItems = computed(() => {
      if (!isAuthenticated.value) {
        return [];
      }

      return allMenuItems;
    });

    const isAuthenticated = computed(() => {
      return store.state.auth.isAuthenticated;
    });


    const activeUser = computed(() => {

      return store.state.auth.activeUser;
    });

    const logout = function(){
      const expiredDate = new Date(0);

      document.cookie = `Authorization=; expires=${expiredDate.toUTCString()}`

      store.commit("setActiveUser", null);
      store.commit("setAuth", false);

      router.push("/login")
    }

    return {
      menuItems,
      isAuthenticated,
      activeUser,
      //methods
      logout
    };
  },
});
</script>

<style scoped>
.navbar {
  height: 56px;
}
</style>
