<template>
  <div class="p-menuitem" label="Toggle" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu">
    <div class="p-menuitem-link">
      File
      <Menu id="overlay_meny" ref="menuRef" :model="menuButtons" :popup="true" />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, Ref } from "@vue/reactivity";

  import Menu from "primevue/menu";

  import { DynamicDialogInstance } from "primevue/dynamicdialogoptions";
  import { useDialog } from "primevue/usedialog";

  import OpenSheetDialog from "./MenuFileDialogs/OpenSheetDialog.vue";
  import CreateSheetDialog from "./MenuFileDialogs/CreateSheetDialog.vue";
  import DeleteSheetDialog from "./MenuFileDialogs/DeleteSheetDialog.vue";

  // global
  const dialog = useDialog();
  let dialogRef: DynamicDialogInstance = null;

  // data
  const menuRef: Ref = ref();
  const menuButtons = ref([
    {
      label: "New",
      // icon: "pi pi-refresh",
      command: () => openCreateSheetDialog(),
    },
    {
      label: "Open",
      // icon: "pi pi-times",
      command: () => openOpenSheetDialog(),
    },
    {
      label: "Save",
      // icon: "pi pi-times",
      command: () => saveSheet(),
    },
    {
      label: "Delete",
      // icon: "pi pi-times",
      command: () => openDeleteSheetDialog(),
    },
    {
      label: "Close",
      // icon: "pi pi-times",
      command: () => openCloseSheetDialog(),
    },
  ]);

  // methods
  const toggle = (event: Event) => {
    menuRef.value.toggle(event);
  };

  const openCreateSheetDialog = async function () {
    dialogRef = dialog.open(CreateSheetDialog, {
      props: {
        header: "Create Sheet",
        style: { width: "75vw" },
        breakpoints: {
          "960px": "75vw",
          "640px": "90vw",
        },
        draggable: false,
        modal: true,
        dismissableMask: false,
      },
    });
  };
  const openOpenSheetDialog = async function () {
    dialogRef = dialog.open(OpenSheetDialog, {
      props: {
        header: "Open Sheet",
        // style: { width: "75vw" },
        // breakpoints: {
        //   "960px": "75vw",
        //   "640px": "90vw",
        // },
        modal: true,
        draggable: false,
        dismissableMask: true,
      },
    });
  };
  const saveSheet = async function () {
    console.log("save Sheet");
  };
  const openDeleteSheetDialog = async function () {
    dialogRef = dialog.open(DeleteSheetDialog, {
      props: {
        header: "Open Sheet",
        style: { width: "75vw" },
        breakpoints: {
          "960px": "75vw",
          "640px": "90vw",
        },
        modal: true,
        dismissableMask: true,
      },
    });
  };
  const openCloseSheetDialog = async function () {};
</script>
