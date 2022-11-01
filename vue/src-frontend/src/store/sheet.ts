import { Cell } from "@/constants";
import { defineStore } from "pinia";

export const useSheetStore = defineStore("sheetStore", {
  state: () => ({
    table: null,
    // table: {
    //   id: 1,
    //   name: "One",
    //   rows: [
    //     {
    //       id: 1,
    //       number: 1,
    //       height: 25,
    //       cells: [
    //         {
    //           id: 1,
    //           content: "1A",
    //         },
    //         {
    //           id: 2,
    //           content: "1B",
    //         },
    //       ],
    //     },
    //     {
    //       id: 2,
    //       number: 2,
    //       height: 25,
    //       cells: [
    //         {
    //           id: 3,
    //           content: "2A",
    //         },
    //         {
    //           id: 4,
    //           content: "2B",
    //         },
    //       ],
    //     },
    //   ],
    //   columns: [
    //     {
    //       id: 1,
    //       notation: "A",
    //       width: 100,
    //       cells: [
    //         {
    //           id: 1,
    //           content: "1A",
    //         },
    //         {
    //           id: 3,
    //           content: "2A",
    //         },
    //       ],
    //     },
    //     {
    //       id: 2,
    //       notation: "B",
    //       width: 100,
    //       cells: [
    //         {
    //           id: 2,
    //           content: "1B",
    //         },
    //         {
    //           id: 4,
    //           content: "2B",
    //         },
    //       ],
    //     },
    //   ],
    //   cells: [
    //     {
    //       id: 1,
    //       content: "1A",
    //       mode: Cell.SELECT,
    //     },
    //     {
    //       id: 2,
    //       content: "1B",
    //       mode: Cell.SELECT,
    //     },
    //     {
    //       id: 3,
    //       content: "2A",
    //       mode: Cell.SELECT,
    //     },
    //     {
    //       id: 4,
    //       content: "2B",
    //       mode: Cell.SELECT,
    //     },
    //   ],
    // },
  }),
  actions: {},
});
