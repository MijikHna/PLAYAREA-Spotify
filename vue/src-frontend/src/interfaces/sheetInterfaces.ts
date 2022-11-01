export interface Cell {
  id: number;
  content: string;
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

export interface Table {
  id: number;
  name: string;
  rows: Row[];
  columns: Column[];
  cells: Cell[];
}
