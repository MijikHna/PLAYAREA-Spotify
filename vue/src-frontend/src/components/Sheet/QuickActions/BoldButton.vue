<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="makeTextBold"
  >
    <FormatBold :size="16" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import FormatBold from "vue-material-design-icons/FormatBold.vue";

const makeTextBold = function () {};
</script>
