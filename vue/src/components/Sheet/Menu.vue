<template>
  <MegaMenu class="p-0" :model="menuItems">
    <template #item="{ item }">
      <component :is="item" />
    </template>
  </MegaMenu>
  <DynamicDialog />
</template>

<script setup lang="ts">
  import MegaMenu from "primevue/megamenu";
  import DynamicDialog from "primevue/dynamicdialog";

  import MenuFile from "./MenuEntries/MenuFile.vue";
  import MenuEdit from "./MenuEntries/MenuEdit.vue";
  import MenuInsert from "./MenuEntries/MenuInsert.vue";
  import MenuFormat from "./MenuEntries/MenuFormat.vue";
  import MenuView from "./MenuEntries/MenuView.vue";
  import MenuHelp from "./MenuEntries/MenuHelp.vue";

  const menuItems = [MenuFile, MenuEdit, MenuInsert, MenuFormat, MenuView, MenuHelp];
</script>
