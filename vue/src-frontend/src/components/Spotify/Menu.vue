<template>
 <div class="my-1">
    <div class="d-flex justify-content-end">
        <Button
          v-if="!spotifyAuthSuccess"
          icon="pi pi-lock"
          label="Login"
          class="p-button-sm"
          @click="loginToSpotify"
        >
          Login To Spotify
        </Button>
        <Button
          v-if="spotifyAuthSuccess"
          icon="pi pi-lock"
          label="Login"
          class="p-button-sm"
          @click="logoutFromSpotify"
        >
          Logout From Spotify
        </Button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import Button from "primevue/button";
import { useStore, Store } from "vuex";
import { computed } from "@vue/reactivity";
import { BackendHttpService } from "@/services/BackendHttpService";

export default defineComponent({
  name: "Menu",
  components: {
    Button,
  },
  setup(){
    const store: Store<any> = useStore();

    const BACKEND_URL =  import.meta.env.VITE_BACKEND_URL;

    const spotifyAuthSuccess = computed(() => store.getters.getSpotifyAuthSuccess);

    const loginToSpotify = async function(){
      const backendHttpSrv =  new BackendHttpService();
      const response = await backendHttpSrv.loginToSpotify();

      if (response.status === 200) {
        window.location.href = response.data.url;

        return;
      }

      console.log(response);
    }

    const logoutFromSpotify = function() {

    }

    return {
      spotifyAuthSuccess,
      loginToSpotify,
      logoutFromSpotify
    }
  }
});
</script>

<style scoped></style>