import { Cell, EditMode } from "@/constants";
import { Table } from "@/interfaces/sheetInterfaces";
import { defineStore } from "pinia";

export const useSheetStore = defineStore("sheetStore", {
  state: () => ({
    table: null as Table,
  }),
  actions: {
    prepareTable(tableData: Table) {
      tableData.cells.forEach((cell) => (cell.mode = EditMode.NONE));
      this.table = tableData;
    },
  },
});
