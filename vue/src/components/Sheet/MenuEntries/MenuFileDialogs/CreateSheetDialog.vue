<template>
  <div class="row justify-content-center">
    <div class="col-12 pt-2">
      <span class="p-float-label">
        <InputText
          id="sheetName"
          type="text"
          v-model="sheetName"
          class="w-100"
        />
        <label for="sheetName">Sheet name</label>
      </span>
    </div>

    <div class="col-2">
      <label for="rows" style="display: block">Horizontal</label>
      <InputNumber
        inputId="rows"
        v-model="rows"
        mode="decimal"
        showButtons
        buttonLayout="vertical"
        style="width: 4rem"
        decrementButtonClass="p-button-secondary"
        incrementButtonClass="p-button-secondary"
        incrementButtonIcon="pi pi-plus"
        decrementButtonIcon="pi pi-minus"
      />
    </div>
    <div class="col-2">
      <label for="columns" style="display: block">Vertical</label>
      <InputNumber
        inputId="columns"
        v-model="columns"
        mode="decimal"
        showButtons
        buttonLayout="vertical"
        style="width: 4rem"
        decrementButtonClass="p-button-secondary"
        incrementButtonClass="p-button-secondary"
        incrementButtonIcon="pi pi-plus"
        decrementButtonIcon="pi pi-minus"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { Ref, ref } from "@vue/reactivity";
  import { onMounted } from "@vue/runtime-core";
  import { h } from "@vue/runtime-core";
  import { inject } from "@vue/runtime-core";

  import { useToast } from "primevue/usetoast";

  import { useSheetStore } from "@/store/sheet";

  import { DynamicDialogInstance } from "primevue/dynamicdialogoptions";
  import Button from "primevue/button";
  import InputText from "primevue/inputtext";
  import InputNumber from "primevue/inputnumber";
  import { AxiosResponse } from "axios";
  import { BackendHttpService } from "@/services/BackendHttpService";

  import { INewSheet, Table } from "@/interfaces/sheetInterfaces";

  // global
  const dialogRef: Ref<DynamicDialogInstance> = inject("dialogRef");
  const sheetStore = useSheetStore();

  const toast = useToast();

  // data
  const sheetName: Ref<string> = ref("");
  const rows: Ref<number> = ref(0);
  const columns: Ref<number> = ref(0);

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
              label: "Create",
              icon: "pi pi-check",
              onClick: () => openSheet(dialogRef),
              autofocus: true,
            }),
          ];
        },
      },
    };
  });

  // methods
  const cancelDialog = function (dialog: Ref<DynamicDialogInstance>) {
    console.log("cancel OpenSheet");
    dialog.value.close({ canceled: true });
  };
  const openSheet = async function (dialog: Ref<DynamicDialogInstance>) {
    // get sheet and save it to sheetStore
    const newSheet: INewSheet = {
      name: sheetName.value,
      rows: rows.value,
      columns: columns.value,
    };

    try {
      const res: AxiosResponse<Table> = await BackendHttpService.createSheet(
        newSheet,
      );

      if (res.status === 201) {
        toast.add({
          severity: "success",
          summary: `Create Sheet`,
          detail: `Your sheet ${res.data.name} has been created`,
          life: 5000,
        });

        console.log(res.data);
        sheetStore.table = res.data;
      }
    } catch (e) {
      toast.add({
        severity: "error",
        summary: `Create Sheet`,
        detail: `Your sheet coulden't be created`,
        life: 5000,
      });
    }

    dialog.value.close({ canceled: false });
  };
</script>
