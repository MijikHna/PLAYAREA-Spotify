import { defineStore } from "pinia";

export const useDiscoverStore = defineStore('discoverStore', {
  state: () => ({
    discoverMenuItemSelected: '' as string,
  }),
});
