<template>
  <div class="container p-0 bg-color">
    <div class="row mx-0">
      <div class="col d-flex text-start align-items-center">
        <span class="d-inline-block mx-4">
          <Avatar class="d-flex p-2" :image="sheetImgUrl" shape="circle" size="large" />
        </span>
        <span class="d-inline-block col">Sheet name: {{ tableName }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ComputedRef, computed } from "@vue/reactivity";

  import Avatar from "primevue/avatar";

  import { useAuthStore } from "@/store/auth";
  import { useSheetStore } from "@/store/sheet";

  import sheetImgUrl from "@/assets/images/sheet-icon.png";

  const authStore = useAuthStore();
  const sheetStore = useSheetStore();

  const tableName: ComputedRef<string> = computed(() => sheetStore.table?.name);
</script>

<style scoped>
  .bg-color {
    background-color: var(--bluegray-200);
  }
</style>
