<template>
  <!-- <div id="anker"></div> -->
  <Dropdown id="sheetName" v-model="selectedSheet" :options="tables" class="mx-4" optionLabel="name" placeholder="Select your sheet" />
</template>

<script setup lang="ts">
  import { ref, Ref } from "@vue/reactivity";
  import { h } from "@vue/runtime-core";
  import { inject } from "@vue/runtime-core";

  import Button from "primevue/button";
  import Dropdown from "primevue/dropdown";

  import { useSheetStore } from "@/store/sheet";
  import { onMounted } from "@vue/runtime-core";
  import { DynamicDialogInstance } from "primevue/dynamicdialogoptions";
  import { AxiosResponse } from "axios";
  import { BackendHttpService } from "@/services/BackendHttpService";
  import { useToast } from "primevue/usetoast";
  import { Table, TableInfo } from "@/interfaces/sheetInterfaces";

  // global
  const dialogRef: Ref<DynamicDialogInstance> = inject("dialogRef");
  const sheetStore = useSheetStore();
  const toast = useToast();

  // data
  const tables: Ref<TableInfo[]> = ref([]);
  const selectedSheet: Ref<TableInfo> = ref();

  onMounted(async () => {
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
              label: "Open",
              icon: "pi pi-",
              onClick: () => openSheet(dialogRef),
              autofocus: true,
            }),
          ];
        },
      },
    };

    // get sheet and save it to sheetStore
    try {
      const res: AxiosResponse<TableInfo[]> = await BackendHttpService.getUserTables();

      console.log(res.data);

      if (res.status === 200) tables.value = res.data;
    } catch (e) {
      toast.add({
        severity: "error",
        summary: `Open Sheet`,
        detail: `Unable to get your sheets`,
        life: 5000,
      });
    }
  });

  // methods
  const cancelDialog = function (dialog: Ref<DynamicDialogInstance>) {
    console.log("cancel OpenSheet");
    dialog.value.close({ canceled: true });
  };
  const openSheet = async function (dialog: Ref<DynamicDialogInstance>) {
    sheetStore.table = null;

    try {
      const res: AxiosResponse<Table> = await BackendHttpService.getTable(selectedSheet.value.id);

      if (res.status === 200) sheetStore.prepareTable(res.data);
    } catch (err) {
      console.log(err);
      toast.add({
        severity: "error",
        summary: `Open Sheet`,
        detail: `Unable to get your sheets`,
        life: 5000,
      });
    }

    dialog.value.close({ canceled: false });
  };
</script>

<style>
  .p-dropdown-panel {
    display: block !important;
  }
  /* #anker {
    position: absolute;
    top: 0px;
    left: 0px;
  } */
</style>
