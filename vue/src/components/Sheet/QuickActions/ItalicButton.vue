<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="makeTextItalic"
  >
    <FormatItalic :size="16" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import FormatItalic from "vue-material-design-icons/FormatItalic.vue";

const makeTextItalic = function () {};
</script>
