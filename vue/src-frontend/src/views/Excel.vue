<template>
  <Button label="Test" v-tooltip.right.click="'Tadfest'"></Button>
</template>

<script lang="ts">
import { defineComponent } from "@vue/runtime-core";
import Button from "primevue/button";
export default defineComponent({
  name: 'Excel',
  components: {
    Button,
  },
})
</script>