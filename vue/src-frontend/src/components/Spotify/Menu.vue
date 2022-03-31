<template>
 <div class="container-flex p-1">
    <div class="d-flex justify-content-end">
      <a :href="BACKEND_URL + '/spotify/login'">
        <Button
          icon="pi pi-lock"
          label="Login"
          class="p-button-sm"
        >
          Login to spotify
        </Button>
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";

import Button from "primevue/button";

export default defineComponent({
  name: "Menu",
  components: {
    Button,
  },
  setup(){
    const BACKEND_URL =  import.meta.env.VITE_BACKEND_URL;

    return {
      BACKEND_URL,
    }
  }
});
</script>

<style scoped></style>