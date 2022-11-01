<template>
  <Dropdown
    id="sheetName"
    v-model="selectedSheet"
    :options="tables"
    optionLabel="name"
    placeholder="Select your sheet"
  ></Dropdown>
  <label for="sheetName"></label>
</template>

<script setup lang="ts">
  import { computed, ComputedRef, ref, Ref } from "@vue/reactivity";
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

  // global
  const dialogRef: Ref<DynamicDialogInstance> = inject("dialogRef");
  const sheetStore = useSheetStore();
  const toast = useToast();

  // data
  const tables: Ref<string[]> = ref([]);
  const selectedSheet: Ref<string> = ref("");

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
              label: "Save",
              icon: "pi pi-check",
              onClick: () => openSheet(dialogRef),
              autofocus: true,
            }),
          ];
        },
      },
    };

    // get sheet and save it to sheetStore
    try {
      const res: AxiosResponse<string[]> =
        await BackendHttpService.getUserTables();

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

  // computed
  const sheets: ComputedRef<string> = computed(() => sheetStore.table?.name);

  // methods
  const cancelDialog = function (dialog: Ref<DynamicDialogInstance>) {
    console.log("cancel OpenSheet");
    dialog.value.close({ canceled: true });
  };
  const openSheet = async function (dialog: Ref<DynamicDialogInstance>) {
    console.log("open OpenSheet");
    dialog.value.close({ canceled: false });
  };
</script>
