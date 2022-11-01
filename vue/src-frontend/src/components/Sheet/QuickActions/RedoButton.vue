<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="redoLastAction"
  >
    <Redo :size="16" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import Redo from "vue-material-design-icons/Redo.vue";

const redoLastAction = function () {};
</script>
