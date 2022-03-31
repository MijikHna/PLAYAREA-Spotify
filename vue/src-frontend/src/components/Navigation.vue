<template>
  <header>
    <nav>
      <Menubar :model="menuItems" class="navbar rounded-0">
        <template #start>
          <router-link to="/" class="navbar-brand">Navbar</router-link>
        </template>
        <template #end>
          <Avatar label="P" shape="circle"/>
        </template>
      </Menubar>
    </nav>
  </header>
</template>

<script lang="ts">
import Menubar from "primevue/menubar";
import Avatar from 'primevue/avatar';

import { defineComponent } from "vue";
import { MenuItem } from "../interfaces/baseInterfaces";

export default defineComponent({
  name: "Navigation",
  components: { Menubar, Avatar },
  setup(){
    const menuItems: MenuItem[] = [
      {
        label: "Home",
        icon: "pi pi-fw pi-file",
        url: "/",
      },
      {
        label: "Spotify",
        icon: "pi pi-fw pi-file",
        url: "/spotify"
      },
      {
        label: "Excel",
        icon: "pi pi-fw pi-file",
        url: "/excel"
      }
    ];
    return {
      //attr
      menuItems,
      //methods
    };
  },
});
</script>

<style scoped>
.navbar {
  height: 56px;
}
</style>
