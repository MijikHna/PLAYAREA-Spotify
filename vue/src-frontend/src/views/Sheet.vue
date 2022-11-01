<template>
  <div class="container-fluid p-0">
    <div class="row">
      <SheetInfo />
    </div>
    <div class="row">
      <Menu />
    </div>
    <div class="row">
      <QuickAction />
    </div>
    <div class="row">
      <Table />
    </div>
  </div>
  <DynamicDialog />
</template>

<script setup lang="ts">
import SheetInfo from "../components/Sheet/SheetInfo.vue";
import DynamicDialog from "primevue/dynamicdialog";

import Menu from "../components/Sheet//Menu.vue";
import QuickAction from "../components/Sheet/QuickAction.vue";
import Table from "../components/Sheet/Table.vue";

import { useAuthStore } from "@/store/auth";
import { useSheetStore } from "@/store/sheet";
</script>
