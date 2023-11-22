<template>
  <div
    class="p-menuitem"
    label="Toggle"
    @click="toggle"
    aria-haspopup="true"
    aria-controls="overlay_menu"
  >
    <div class="p-menuitem-link">
      Format
      <Menu
        id="overlay_meny"
        ref="menuRef"
        :model="menuButtons"
        :popup="true"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, Ref } from "@vue/reactivity";
import Menu from "primevue/menu";

// global

// data
const menuRef: Ref = ref();
const menuButtons: Ref = ref([]);

// methods
const toggle = (event: Event) => {
  menuRef.value.toggle(event);
};
</script>
