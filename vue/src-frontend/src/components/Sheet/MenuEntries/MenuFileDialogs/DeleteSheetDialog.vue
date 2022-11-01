<template>
  <div class="row">
    <div class="col text-center">
      <span class="fs-4 text-danger">
        Are your really want to delete Sheet
        <span class="fs-3 fw-bolder"> {{ sheetName }}</span>
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ComputedRef, ref, Ref } from "@vue/reactivity";
import { h } from "@vue/runtime-core";
import { inject } from "@vue/runtime-core";

import Button from "primevue/button";

import { useSheetStore } from "@/store/sheet";
import { onMounted } from "@vue/runtime-core";
import { DynamicDialogInstance } from "primevue/dynamicdialogoptions";

// global
const dialogRef: Ref<DynamicDialogInstance> = inject("dialogRef");
const sheetStore = useSheetStore();

// data
const sheetName: Ref<string> = ref("Test");

onMounted(() => {
  dialogRef.value.options = {
    templates: {
      footer: () => {
        return [
          h(Button, {
            label: "Cancel",
            icon: "pi pi-times",
            onClick: () => cancelDialog(dialogRef),
            class: "p-button-text",
          }),
          h(Button, {
            label: "Save",
            icon: "pi pi-check",
            onClick: () => openSheet(dialogRef),
            autofocus: true,
          }),
        ];
      },
    },
  };
});

// computed
const sheets: ComputedRef<string> = computed(() => sheetStore.table?.name);

// methods
const cancelDialog = function (dialog: Ref<DynamicDialogInstance>) {
  console.log("cancel OpenSheet");
  dialog.value.close({ canceled: true });
};
const openSheet = async function (dialog: Ref<DynamicDialogInstance>) {
  // get sheet and save it to sheetStore
  console.log("open OpenSheet");
  dialog.value.close({ canceled: false });
};
</script>
