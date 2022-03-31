<script lang="ts">
import { defineComponent } from "vue";

import Navigation from "@/components/Navigation.vue";
import Main from "@/components/Main.vue";
import Footer from "@/components/Footer.vue";

export default defineComponent({
  name: "App",
  components: {Navigation, Main, Footer}
});
</script>

<template>
  <Navigation></Navigation>
  <Main></Main>
  <Footer></Footer>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
