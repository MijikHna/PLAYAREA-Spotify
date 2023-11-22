<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="strikeThrough"
  >
    <Palette :size="18" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import Palette from "vue-material-design-icons/Palette.vue";

const strikeThrough = function () {};
</script>
