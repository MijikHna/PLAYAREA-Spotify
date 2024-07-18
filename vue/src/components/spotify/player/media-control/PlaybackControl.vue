<template>
  <div class="flex justify-center min-w-full">
    <!-- <div class="flex min-w-full"> -->
      <div class="p-1 mx-1">
        <Button rounded icon="pi" v-tooltip.top="'Random'">
            <FontAwesomeIcon :icon="faShuffle" />
</Button>
      </div>
      <div class=" p-1 mx-1">
        <Button rounded icon="pi" :disabled="!loggedIn" v-tooltip.top="'Backward'"
          @click="playPreviousTrack">
          <FontAwesomeIcon :icon="faBackward" />
        </Button>
      </div>
      <div class=" p-1 mx-1">
        <Button rounded :disabled="!loggedIn" icon="pi" v-tooltip.top="'Play'"
          @click="togglePlay">
            <FontAwesomeIcon :icon="playIcon" />
        </Button>
      </div>
      <div class="p-1 mx-1">
        <Button rounded icon="pi" :disabled="!loggedIn" v-tooltip.top="'Forward'"
          @click="playNextTrack">
            <FontAwesomeIcon :icon="faForward" />
        </Button>
      </div>
      <div class="p-1 mx-1">
        <Button rounded icon="pi" :disabled="!loggedIn" v-tooltip.top="'Replay'">
          <FontAwesomeIcon :icon="faRepeat" />
        </Button>
      </div>
      <div class="p-1 mx-1">
        <Button rounded icon="pi" :disabled="!loggedIn" v-tooltip.top="'Devices'"
          @click="toggleDevices">
          <FontAwesomeIcon :icon="faHeadphonesSimple" />
        </Button>
        <OverlayPanel ref="deviceOp" class="padding-0">
          <Menu :model="devices"> </Menu>
        </OverlayPanel>
      </div>
      <div class="p-1 mx-1">
        <Button rounded :disabled="!loggedIn" icon="pi pi-volume-up" v-tooltip.top="'Volume'"
          @click="toggleVolumePanel">
            <FontAwesomeIcon :icon="faVolumeOff" />
        </Button>
        <OverlayPanel ref="volumeOp" :style="{ width: '200px' }">
          <Slider v-model="volumeLevel" @change="setVolume"></Slider>
        </OverlayPanel>
      <!-- </div> -->
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

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { IconDefinition, faRepeat, faHeadphonesSimple, faVolumeOff, faShuffle, faBackward, faForward, faPlay, faPause } from '@fortawesome/free-solid-svg-icons'

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
  () => spotifyStore.auth.loggedIn,
);
const spotifyPlayer: ComputedRef<any> = computed(
  () => spotifyStore.dom.spotifyPlayer,
);

// data
const playIcon: Ref<IconDefinition> = ref(faPlay);
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
              command: selectDevice.bind(spotifyDevice),
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

  if (state.paused) playIcon.value = faPause;
  else playIcon.value = faPlay;

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

async function selectDevice(this: DeviceResponse): Promise<void> {
  try {
    const response: AxiosResponse =
      await SpotifyHttpService.http.put('/me/player', {
        device_ids: [this.id],
        play: false,
      });

    if (response.status === 204) {
      spotifyStore.player.playerActive =
        this.name === spotifyPlayer.value._options.name;

      toast.add({
        severity: "success",
        summary: `Select Player`,
        detail: `Player ${this.name} has been selected`,
        life: 5000,
      });
    }
  } catch (e) {
    toast.add({
      severity: "error",
      summary: `Select Player`,
      detail: `Player ${this.name} couldn't be selected`,
      life: 5000,
    });
  }
}
</script>

<style>
.padding-0>.p-overlaypanel-content {
  padding: 0;
}
</style>
