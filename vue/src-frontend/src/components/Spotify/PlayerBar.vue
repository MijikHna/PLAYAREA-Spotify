<template>
  <div class="row mx-0 justify-content-between align-items-center">
    <div class="col" >
      <Button icon="pi pi-question" v-tooltip.top="'Random'" class="p-button-raised p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-backward" v-tooltip.right="'Backward'" class="p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-play" v-tooltip.bottom="'Play'" class="p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-forward" v-tooltip.left="'Forward'" class="p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-replay" v-tooltip="'replay'" class="p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-tablet" v-tooltip="'replay'" class="p-button-rounded" @click="toggle"></Button>
      <Menu ref="menu" :model="items" :popup="true"></Menu>
    </div>
    <div class="col">
      <Button icon="pi pi-volume-up" v-tooltip="'replay'" class="p-button-rounded"></Button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

import Button from "primevue/button";
import Menu from "primevue/menu";

export default defineComponent({
  name: "PlayerBar",
  components: {
    Button,
    Menu,
  },
  setup(){
    const menu = ref(null);

    const items = [
      {
        label: 'Delete',
  			icon: 'pi pi-times'
      },
      {
        label: 'Delete',
  			icon: 'pi pi-times'
      }
    ];
    const toggle = function(event) {
      menu.value.toggle(event);
    }

    return {
      menu,
      items,
      toggle,
    }
  }
});
</script>

<style scoped></style>