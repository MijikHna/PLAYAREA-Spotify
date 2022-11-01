<template>
  <div class="row px-0 mx-0">
    <div class="col">
      <MegaMenu class="pt-0" :model="quickActions">
        <template #item="{ item }">
          <component :is="item"></component>
        </template>
      </MegaMenu>
    </div>
  </div>
</template>

<script setup lang="ts">
import MegaMenu from "primevue/megamenu";
import UndoButton from "./QuickActions/UndoButton.vue";
import RedoButton from "./QuickActions/RedoButton.vue";
import BoldButton from "./QuickActions/BoldButton.vue";
import ItalicButton from "./QuickActions/ItalicButton.vue";
import StrikeThroughButton from "./QuickActions/StrikeThroughButton.vue";
import TextColorButton from "./QuickActions/TextColorButton.vue";

import { useAuthStore } from "@/store/auth";
import { useSheetStore } from "@/store/sheet";

const quickActions = [
  UndoButton,
  RedoButton,
  BoldButton,
  ItalicButton,
  StrikeThroughButton,
  TextColorButton,
];
</script>
