<template>
  <Navigation></Navigation>
  <Main></Main>
  <Footer></Footer>
</template>

<script setup lang="ts">
import Footer from "@/components/Footer.vue";
import Main from "@/components/Main.vue";
import Navigation from "@/components/Navigation.vue";

import { computed, ComputedRef } from "@vue/reactivity";
import { onMounted, watch } from "@vue/runtime-core";
import { useUserStore } from "./store/user";

// global
const userStore = useUserStore();
// computed
const theme: ComputedRef<string> = computed(() => userStore.activeUser?.profile?.theme);

// watch
watch(theme, (newValue: string) => {
  // setTheme(newValue);
});

// data
const themeDOMElem: HTMLStyleElement = document.createElement("style");

// // mounted
onMounted(async () => {
  // set User Theme
  themeDOMElem.setAttribute("type", "text/css");
  document.getElementsByTagName("head")[0].append(themeDOMElem);

  // setTheme(theme.value);
});

// methods
// const setTheme = function (theme: string) {
//   themeDOMElem.innerHTML = "";
//   if (theme === "dark") themeDOMElem.append(DarkTheme);
//   else themeDOMElem.append(LightTheme);
// };
</script>
<style>
</style>
