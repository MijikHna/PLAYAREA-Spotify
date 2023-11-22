<template>
  <div class="container-fluid p-0">
    <div class="row mx-0">
      <SheetInfo />
    </div>
    <div class="row mx-0">
      <Menu />
    </div>
    <div class="row mx-0">
      <QuickAction />
    </div>
    <div class="row mx-0">
      <Table v-if="table" />
    </div>
  </div>
</template>

<script setup lang="ts">
  import SheetInfo from "../components/Sheet/SheetInfo.vue";

  import Menu from "../components/Sheet//Menu.vue";
  import QuickAction from "../components/Sheet/QuickAction.vue";
  import Table from "../components/Sheet/Table.vue";

  import { useSheetStore } from "@/store/sheet";
  import { computed, ComputedRef } from "@vue/reactivity";

  const sheetStore = useSheetStore();

  // computed
  const table: ComputedRef = computed(() => sheetStore.table);
</script>
