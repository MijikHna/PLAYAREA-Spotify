import { EditMode } from "@/constants";

export interface Cell {
  id: number;
  column_id: number;
  row_id: number;
  content: string;
  mode: EditMode;
}

export interface Row {
  id: number;
  number: string;
  height: number;
  cells: Cell[];
}

export interface Column {
  id: number;
  notation: string;
  width: number;
  cells: Cell[];
}

export interface INewSheet {
  name: string;
  columns: number;
  rows: number;
}

export interface TableInfo {
  id: number;
  name: string;
}
export interface Table extends TableInfo {
  rows: Row[];
  columns: Column[];
  cells: Cell[];
  mode: EditMode;
}
