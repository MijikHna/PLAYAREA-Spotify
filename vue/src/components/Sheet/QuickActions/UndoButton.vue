<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="undoLastAction"
  >
    <Undo :size="16" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import Undo from "vue-material-design-icons/Undo.vue";

const undoLastAction = function () {};
</script>
