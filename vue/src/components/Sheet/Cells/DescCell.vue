<template>
  <div
    v-if="type === DescCellTypes.ROW || type === DescCellTypes.COLUMN"
    class="border"
    :style="{ width: cellWidth + 'px', height: cellHeight + 'px' }"
  >
    {{ number || notation }}
  </div>
  <div v-else v-html="'\xa0'" class="border" :style="{ width: 50 + 'px', height: 25 + 'px' }"></div>
</template>

<script setup lang="ts">
  import { DescCellTypes } from "@/constants";
  import { ref, Ref } from "@vue/reactivity";
  import { onMounted } from "@vue/runtime-core";

  import { column, row } from "@/interfaces/sheetInterfaces";

  const props = defineProps<{
    type: string;
    number?: string;
    notation?: string;
    column?: { type: column; default: null };
    row?: { type: row; default: null };
  }>();

  //global

  // data
  const cellWidth: Ref<number> = ref(50);
  const cellHeight: Ref<number> = ref(25);
  onMounted(() => {
    cellWidth.value = props.column?.width || cellWidth.value;
    cellHeight.value = props.row?.height || cellHeight.value;
  });
</script>
