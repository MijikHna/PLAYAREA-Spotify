<template>
  <div>
    <ScrollPanel class="table-size custombar p-0">
      <div
        ref="tableRef"
        class="container-fluid px-0"
        tabindex="0"
        @keydown.left="moveLeft"
        @keydown.right="moveRight"
        @keydown.down="moveDown"
        @keydown.up="moveUp"
        @keydown.enter="setMode($event, EditMode.EDIT)"
        @keydown.esc="setMode($event, EditMode.SELECT)"
        @keydown.tab="selectMode($event)"
      >
        <div class="row p-0 flex-nowrap">
          <DescCell :type="DescCellTypes.EMPTY" class="" />
          <DescCell
            v-for="(column, index) in table.columns"
            :key="index"
            :type="DescCellTypes.COLUMN"
            :notation="column.notation"
            :column="column"
            class=""
          />
        </div>

        <div v-for="(row, indexRow) in table.rows" :key="indexRow" class="row p-0 flex-nowrap">
          <DescCell :type="DescCellTypes.ROW" :number="row.number" :row="row" class="" />

          <Cell
            v-for="(column, indexColumn) in table.columns"
            :id="table.cells[indexRow * table.columns.length + indexColumn].id"
            :cell="table.cells[indexRow * table.columns.length + indexColumn]"
            :width="column.width"
            :height="row.height"
            class=""
            :ref="setCellsRef"
          />
        </div>
      </div>
    </ScrollPanel>
  </div>
</template>

<script setup lang="ts">
  import { computed, ComputedRef, Ref, ref } from "@vue/reactivity";

  import ScrollPanel from "primevue/scrollpanel";

  import AddCell from "./Cells/AddCell.vue";
  import DescCell from "./Cells/DescCell.vue";
  import Cell from "./Cells/Cell.vue";

  import { DescCellTypes } from "@/constants";
  import { useSheetStore } from "@/store/sheet";

  import { EditMode } from "@/constants";
  import { onMounted } from "@vue/runtime-core";
  import { Cell as ICell } from "@/interfaces/sheetInterfaces";

  // global
  const sheetStore = useSheetStore();

  // data
  const tableRef: Ref = ref();
  const cells: Ref<any[]> = ref([]);

  // computed
  const table: ComputedRef = computed(() => sheetStore.table);
  const currentCell: Ref<ICell> = ref(table.value.cells[0]);

  onMounted(() => {
    currentCell.value.mode = EditMode.SELECT;
    cells.value[0].focus();
  });

  // methods
  const setCellsRef = (el: any) => {
    console.log(el.$el);
    cells.value.push(el.$el);
  };

  const moveLeft = function () {
    console.log("left");
    if (currentCell.value.mode === EditMode.EDIT) return;

    // find current Column
    let currentColumn = table.value.columns.find((column) => column.id === currentCell.value.column_id);

    if (currentColumn.notation === "A") return;

    currentCell.value.mode = EditMode.NONE;
    currentCell.value = table.value.cells.find(
      (cell: ICell) => cell.column_id === currentColumn.id - 1 && cell.row_id === currentCell.value.row_id,
    );

    currentCell.value.mode = EditMode.SELECT;
    const focusCellEl: HTMLElement = cells.value.find((cell) => cell.id === String(currentCell.value.id));

    focusCellEl.focus();
  };
  const moveRight = function () {
    console.log("right");
    if (currentCell.value.mode === EditMode.EDIT) return;
    let currentColumn = table.value.columns.find((column) => column.id === currentCell.value.column_id);

    if (currentColumn.notation === table.value.columns[table.value.columns.length - 1].notation) return;

    currentCell.value.mode = EditMode.NONE;
    currentCell.value = table.value.cells.find(
      (cell: ICell) => cell.column_id === currentColumn.id + 1 && cell.row_id === currentCell.value.row_id,
    );

    currentCell.value.mode = EditMode.SELECT;
    const focusCellEl: HTMLElement = cells.value.find((cell) => cell.id === String(currentCell.value.id));

    focusCellEl.focus();
  };
  const moveUp = function () {
    console.log("up");
    if (currentCell.value.mode === EditMode.EDIT) return;
    let currentRow = table.value.rows.find((row) => row.id === currentCell.value.row_id);

    if (currentRow.number === "1") return;

    currentCell.value.mode = EditMode.NONE;
    currentCell.value = table.value.cells.find(
      (cell: ICell) => cell.row_id === currentRow.id - 1 && cell.column_id === currentCell.value.column_id,
    );

    currentCell.value.mode = EditMode.SELECT;
    const focusCellEl: HTMLElement = cells.value.find((cell) => cell.id === String(currentCell.value.id));

    focusCellEl.focus();
  };

  const moveDown = function () {
    console.log("down");
    let currentRow = table.value.rows.find((row) => row.id === currentCell.value.row_id);

    if (currentRow.number === table.value.rows[table.value.rows.length - 1].number) return;

    currentCell.value.mode = EditMode.NONE;
    currentCell.value = table.value.cells.find(
      (cell: ICell) => cell.row_id === currentRow.id + 1 && cell.column_id === currentCell.value.column_id,
    );

    currentCell.value.mode = EditMode.SELECT;
    const focusCellEl: HTMLElement = cells.value.find((cell) => cell.id === String(currentCell.value.id));

    focusCellEl.focus();
  };

  const setMode = function (event: KeyboardEvent, mode: EditMode) {
    console.log(event);
    console.log(mode);
    console.log("esc, enter");

    if (event.key === "Enter" && currentCell.value.mode === EditMode.EDIT) return;
    if (event.key === "Escape" && currentCell.value.mode === EditMode.SELECT) return;

    if (mode === EditMode.EDIT) currentCell.value.mode = EditMode.EDIT;
    if (mode === EditMode.SELECT) currentCell.value.mode = EditMode.SELECT;
  };
  const selectMode = function (event: any) {
    console.log(cells.value);
    console.log(tableRef.value);
  };
</script>

<script lang="ts"></script>

<style lang="scss" scoped>
  ::v-deep(.p-scrollpanel) {
    &.custombar {
      .p-scrollpanel-wrapper {
        border-right: 9px solid var(--surface-ground);
      }

      .p-scrollpanel-bar {
        background-color: var(--primary-color);
        opacity: 1;
        transition: background-color 0.2s;

        &:hover {
          background-color: #007ad9;
        }
      }
    }
  }
  .table-size {
    width: calc(100vw - 18px);
    height: calc(100vh - 56px - 56px - 149px - 18px);
  }
</style>
