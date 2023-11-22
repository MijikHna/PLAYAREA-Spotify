<template>
  <div>
    <div class="flex min-w-full justify-content-between align-items-center">
      <div class="col-p-0 p-1">
        <Button class="p-button-raised p-button-rounded" icon="pi pi-question" :disabled="true"
          v-tooltip.top="'Random'"></Button>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" icon="pi pi-backward" :disabled="!loggedIn" v-tooltip.top="'Backward'"
          @click="playPreviousTrack"></Button>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" :disabled="!loggedIn" :icon="playIcon" v-tooltip.top="'Play'"
          @click="togglePlay"></Button>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" icon="pi pi-forward" :disabled="!loggedIn" v-tooltip.top="'Forward'"
          @click="playNextTrack"></Button>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" icon="pi pi-replay" :disabled="!loggedIn" v-tooltip.top="'Replay'"></Button>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" icon="pi pi-tablet" :disabled="!loggedIn" v-tooltip.top="'Devices'"
          @click="toggleDevices"></Button>
        <OverlayPanel ref="deviceOp" class="padding-0">
          <Menu :model="devices"> </Menu>
        </OverlayPanel>
      </div>
      <div class="col-p-0 p-1">
        <Button class="p-button-rounded" :disabled="!loggedIn" icon="pi pi-volume-up" v-tooltip.top="'Volume'"
          @click="toggleVolumePanel"></Button>
        <OverlayPanel ref="volumeOp" :style="{ width: '200px' }">
          <Slider v-model="volumeLevel" @change="setVolume"></Slider>
        </OverlayPanel>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ComputedRef } from "@vue/reactivity";
import { ref, Ref } from "vue";

import Button from "primevue/button";
import Menu from "primevue/menu";
import OverlayPanel from "primevue/overlaypanel";
import Slider from "primevue/slider";
import { useToast } from "primevue/usetoast";

import { useSpotifyStore } from "@/store/spotify";

import { SpotifyHttpService } from "@/services/SpotifyHttpService";

import { AxiosResponse } from "axios";

import { DeviceResponse } from "@/types/spotify/device.types";
import { DeviceMenuEntry } from "@/types/spotify/app.types";

// global
const spotifyStore = useSpotifyStore();
const toast = useToast();

// template refs
const deviceOp = ref(null);
const volumeOp = ref(null);

//computed
const loggedIn: ComputedRef<boolean> = computed(
  () => spotifyStore.loggedIn,
);
const spotifyPlayer: ComputedRef<any> = computed(
  () => spotifyStore.spotifyPlayer,
);

// data
const playIcon: Ref<string> = ref("pi pi-play");
const devices: Ref<DeviceMenuEntry[]> = ref([]);
const volumeLevel: Ref<number> = ref(50);

//methods
const toggleDevices = function (event: Event): void {
  if (!loggedIn.value) {
    deviceOp.value.toggle(event);
    return;
  }

  // TODO: Progress spinner

  SpotifyHttpService.http
    .get('/me/player/devices')
    .then((response: AxiosResponse) => response.data.devices)
    .then(async (spotifyDevices: DeviceResponse[]) => {
      devices.value = await Promise.all(
        spotifyDevices.map(
          (spotifyDevice) => {
            return {
              deviceId: spotifyDevice.id,
              active: spotifyDevice.is_active,
              key: spotifyDevice.id,
              label: spotifyDevice.name,
              icon: "pi pi-tablet",
              command: async function (): Promise<void> {
                try {
                  const response: AxiosResponse =
                    await SpotifyHttpService.http.put('/me/player', {
                      device_ids: [this.deviceId],
                      play: false,
                    });

                  if (response.status === 204) {
                    spotifyStore.playerActive =
                      this.label === spotifyPlayer.value._options.name;

                    toast.add({
                      severity: "success",
                      summary: `Select Player`,
                      detail: `Player ${this.label} has been selected`,
                      life: 5000,
                    });
                  }
                } catch (e) {
                  toast.add({
                    severity: "error",
                    summary: `Select Player`,
                    detail: `Player ${this.label} couldn't be selected`,
                    life: 5000,
                  });
                }
              },
            };
          },
        )
      );
    })
    .catch((error) => {
      console.log(error);
    });

  deviceOp.value.toggle(event);
};

const toggleVolumePanel = function (event: Event) {
  volumeOp.value.toggle(event);
};

// FIXME: pause button shows state correctly only if actions triggered here
const togglePlay = async function () {
  const state = await spotifyPlayer.value.getCurrentState();

  if (!state) {
    console.log("Another Spotify Player is playing");
    return;
  }

  if (state.paused) playIcon.value = "pi pi-pause";
  else playIcon.value = "pi pi-play";

  spotifyPlayer.value.togglePlay();
};

const playPreviousTrack = async function () {
  await spotifyPlayer.value.previousTrack();
};

const playNextTrack = async function () {
  await spotifyPlayer.value.nextTrack();
};

const setVolume = async function (volume: number) {
  if (!spotifyPlayer.value) return;
  await spotifyPlayer.value.setVolume(volume / 100);
};
</script>

<style>
.padding-0>.p-overlaypanel-content {
  padding: 0;
}
</style>
