<template>
  <div class="row mx-0 justify-content-between align-items-center">
    <div class="col" >
      <Button
        class="p-button-raised p-button-rounded"
        icon="pi pi-question"
        :disabled="true"
        v-tooltip.top="'Random'"
      ></Button>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        icon="pi pi-backward"
        :disabled="!spotifyAuthSuccess"
        v-tooltip.top="'Backward'"
        @click="playPreviousTrack"
      ></Button>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        :disabled="!spotifyAuthSuccess"
        :icon="playIcon"
        v-tooltip.top="'Play'"
        @click="togglePlay"
      ></Button>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        icon="pi pi-forward"
        :disabled="!spotifyAuthSuccess"
        v-tooltip.top="'Forward'"
        @click="playNextTrack"
      ></Button>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        icon="pi pi-replay"
        :disabled="!spotifyAuthSuccess"
        v-tooltip.top="'Replay'"
      ></Button>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        icon="pi pi-tablet"
        :disabled="!spotifyAuthSuccess"
        v-tooltip.top="'Devices'"
        @click="toggleDevices"
      ></Button>
      <OverlayPanel ref="deviceOp" class="padding-0">
        <Menu
          :model="devices"
        >
        </Menu>
      </OverlayPanel>
    </div>
    <div class="col">
      <Button
        class="p-button-rounded"
        :disabled="!spotifyAuthSuccess"
        icon="pi pi-volume-up"
        v-tooltip.top="'Volume'"
        @click="toggleVolumePanel"
      ></Button>
      <OverlayPanel ref="volumeOp" :style="{width: '200px'}">
          <Slider v-model="volumeLevel" @change="setVolume"></Slider>
      </OverlayPanel>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, Ref } from "vue";

import Button from "primevue/button";
import Menu from "primevue/menu";
import OverlayPanel from 'primevue/overlaypanel';
import Slider from 'primevue/slider';
import { useToast } from 'primevue/usetoast';

import { computed, ComputedRef } from "@vue/reactivity";
import { Store, useStore } from "vuex";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";

import { IDeviceMenuEntry } from "@/interfaces/spotifyInterfaces";

import { AxiosResponse } from "axios";


export default defineComponent({
  components: {
    Button,
    Menu,
    Slider,
    OverlayPanel
  },
  setup(){
    // global
    const store: Store<any> = useStore();
    const toast = useToast();


    // template refs
    const deviceOp = ref(null);
    const volumeOp = ref(null);

    //computed
    const spotifyAuthSuccess: ComputedRef<boolean> = computed(() => store.getters.getSpotifyAuthSuccess)
    const spotifyPlayer: ComputedRef<any> = computed(() => store.state.spotify.spotifyPlayer);

    // data
    const playIcon: Ref<string> = ref('pi pi-play');
    const devices: Ref<any[]> = ref([]);
    const volumeLevel: Ref<number> = ref(50);


    //methods
    const toggleDevices = function(event: Event): void {
      if (!spotifyAuthSuccess.value){
        deviceOp.value.toggle(event);
        return;
      }

      // TODO: Progress spinner

      SpotifyHttpService.getAvailableDevices().then(spotifyDevices => {
        const deviceMenuEntries: IDeviceMenuEntry[] = spotifyDevices.map(spotifyDevice => {
          return {
            deviceId: spotifyDevice.id,
            label: spotifyDevice.name,
            icon: 'pi pi-tablet',
          }
        });


        deviceMenuEntries.forEach(device => {
          device.command = async function(): Promise<void>{
            try{
              const response: AxiosResponse = await SpotifyHttpService.selectPlayer([device.deviceId])

              if (response.status === 204) {
                // store.commit("setThisPlayerActive", device.label === spotifyPlayer.value._options.name);

                toast.add({
                  severity: 'success',
                  summary: `Select Player`,
                  detail: `Player ${device.label} has been selected`,
                  life: 5000,
                });
              }
            }
            catch(e){
              toast.add({
                severity: 'error',
                summary: `Select Player`,
                detail: `Player ${device.label} couldn't be selected`,
                life: 5000,
              })
            }
          }
        });

        devices.value = deviceMenuEntries;
      });

      deviceOp.value.toggle(event);
    }

    const toggleVolumePanel = function (event: Event) {
      volumeOp.value.toggle(event)
    }

    const togglePlay = async function(){
      const state = await spotifyPlayer.value.getCurrentState();

      if (!state) {
        console.log('Another Spotify Player is playing');
        return;
      }

      console.log(state);

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

    const setVolume = async function (volume: number) {
      if (!spotifyPlayer.value) {
        return;
      }
      await spotifyPlayer.value.setVolume(volume/100);

    }

    return {
      //refs
      deviceOp,
      volumeOp,
      // data
      playIcon,
      devices,
      volumeLevel,
      // computed
      spotifyAuthSuccess,
      spotifyPlayer,
      // methods
      toggleDevices,
      toggleVolumePanel,
      togglePlay,
      playPreviousTrack,
      playNextTrack,
      setVolume
    }
  }
});
</script>

<style>
  .padding-0 > .p-overlaypanel-content {
    padding: 0;
  }
</style>
