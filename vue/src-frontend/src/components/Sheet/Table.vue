<template>
  <div v-if="table" ref="tableRef" class="container-fluid sheet">
    <div class="row">
      <DescCell :type="DescCellTypes.EMPTY" />
      <DescCell
        v-for="(column, index) in table.columns"
        :key="index"
        :type="DescCellTypes.COLUMN"
        :notation="column.notation"
        :column="column"
      />
    </div>

    <div v-for="(row, indexRow) in table.rows" :key="indexRow" class="row">
      <DescCell :type="DescCellTypes.ROW" :number="row.number" :row="row" />

      <Cell
        v-for="(column, indexColumn) in table.columns"
        :cell="table.cells[indexRow * table.columns.length + indexColumn]"
        :width="column.width"
        :height="row.height"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed, ComputedRef, Ref, ref } from "@vue/reactivity";

  import AddCell from "./Cells/AddCell.vue";
  import DescCell from "./Cells/DescCell.vue";
  import Cell from "./Cells/Cell.vue";

  import { DescCellTypes } from "@/constants";
  import { useAuthStore } from "@/store/auth";
  import { useSheetStore } from "@/store/sheet";

  // global
  const sheetStore = useSheetStore();

  // data
  const tableRef: Ref = ref();

  // computed
  const table: ComputedRef = computed(() => sheetStore.table);
</script>

<style scoped>
  .sheet {
    overflow-x: auto;
  }
</style>
