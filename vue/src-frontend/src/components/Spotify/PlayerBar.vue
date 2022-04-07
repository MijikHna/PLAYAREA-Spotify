<template>
  <div class="row mx-0 justify-content-between align-items-center">
    <div class="col" >
      <Button icon="pi pi-question" v-tooltip.top="'Random'" class="p-button-raised p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button
        icon="pi pi-backward"
        v-tooltip.top="'Backward'"
        class="p-button-rounded"
        @click="playPreviousTrack"
      ></Button>
    </div>
    <div class="col">
      <Button
        :icon="playIcon"
        v-tooltip.top="'Play'"
        class="p-button-rounded"
        @click="togglePlay"
      ></Button>
    </div>
    <div class="col">
      <Button
        icon="pi pi-forward"
        v-tooltip.top="'Forward'"
        class="p-button-rounded"
         @click="playNextTrack"
      ></Button>
    </div>
    <div class="col">
      <Button icon="pi pi-replay" v-tooltip.top="'Replay'" class="p-button-rounded"></Button>
    </div>
    <div class="col">
      <Button
        icon="pi pi-tablet"
        v-tooltip.top="'Devices'"
        class="p-button-rounded"
        @click="toggleDevices"
      ></Button>
      <Menu
        ref="menu"
        :model="items"
        :popup="true"
      >
        <!-- <template #item="{item}">
          {{item.label}}
        </template> -->
      </Menu>
    </div>
    <div class="col">
      <Button icon="pi pi-volume-up" v-tooltip="'Volume'" class="p-button-rounded"></Button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

import Button from "primevue/button";
import Menu from "primevue/menu";
import { computed } from "@vue/reactivity";
import { Store, useStore } from "vuex";
import { SpotifyHttpService } from "@/services/SpotifyHttpService";

export default defineComponent({
  name: "PlayerBar",
  components: {
    Button,
    Menu,
  },
  setup(){
    // global
    const store: Store<any> = useStore();

    // template refs
    const menu = ref(null);

    // data
    const playIcon = ref('pi pi-play');
    const items = [];

    //computed
    const spotifyAuthSuccess = computed(() => store.getters.getSpotifyAuthSuccess)
    const spotifyPlayer = computed(() => store.state.spotify.spotifyPlayer);

    //methods
    const toggleDevices = async function(event) {
      const spotifyHttpSrv: SpotifyHttpService = new SpotifyHttpService();
      const devices = await spotifyHttpSrv.getAvailableDevices();
      console.log(devices)
      items.length = 0;
      devices.forEach((device: any) => {
        items.push({label: device.name, id: device.id});
      });
      menu.value.toggle(event);
    }

    const togglePlay = async function(){
      const state = await spotifyPlayer.value.getCurrentState();

      if (!state) {
        console.log('Another Spotify Player is playing');
        return;
      }

      if (state.paused) {
        playIcon.value = 'pi pi-pause';
      }else {
        playIcon.value = 'pi pi-play';
      }

      spotifyPlayer.value.togglePlay();
    }

    const playPreviousTrack = async function() {
      await spotifyPlayer.value.previousTrack();
    }

    const playNextTrack = async function () {
      await spotifyPlayer.value.nextTrack();
    }

    return {
      //refs
      menu,
      // data
      playIcon,
      items,
      // computed
      spotifyPlayer,
      // methods
      toggleDevices,
      togglePlay,
      playPreviousTrack,
      playNextTrack
    }
  }
});
</script>

<style scoped></style>