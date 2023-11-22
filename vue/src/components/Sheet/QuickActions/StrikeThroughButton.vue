<template>
  <Button
    class="p-button-rounded p-button-secondary p-button-sm"
    @click="strikeThrough"
  >
    <FormatStrikethrough :size="16" />
  </Button>
</template>

<script setup lang="ts">
import Button from "primevue/button";
// import StrikethroughS from "vue-material-design-icons/StrikethroughS.vue";
import FormatStrikethrough from "vue-material-design-icons/FormatStrikethrough.vue";

const strikeThrough = function () {};
</script>
