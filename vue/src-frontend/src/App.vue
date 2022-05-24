<template>
  <Navigation></Navigation>
  <Main></Main>
  <Footer></Footer>
</template>

<script lang="ts">
import Navigation from "@/components/Navigation.vue";
import Main from "@/components/Main.vue";
import Footer from "@/components/Footer.vue";
import { computed, ComputedRef } from "@vue/reactivity";
import { useStore, Store } from "vuex";
import { defineComponent } from "@vue/runtime-core";
import LightTheme from "primevue/resources/themes/bootstrap4-light-blue/theme.css";
import DarkTheme from "primevue/resources/themes/bootstrap4-dark-blue/theme.css";
import { onMounted } from "@vue/runtime-core";
import { watch } from "@vue/runtime-core";

export default defineComponent({
  components: {
    Navigation,
    Main,
    Footer,
  },

  setup() {
    //global
    let store: Store<any> = useStore();

    // computed
    const theme: ComputedRef<string> = computed(() => store.state.base.theme );

    // watch
    watch(
      theme,
      (newValue: string) => {
        setTheme(newValue)
      }
    )

    // data
    const themeDOMElem: HTMLStyleElement = document.createElement("style");

    // // mounted
    onMounted(async () => {
      themeDOMElem.setAttribute('type', 'text/css');
      document.getElementsByTagName('head')[0].append(themeDOMElem);

      setTheme(theme.value);
    });

    // methods
    const setTheme = function(theme: string){
      themeDOMElem.innerHTML='';
      if (theme === 'dark'){
        themeDOMElem.append(DarkTheme);
      }
      else{
        themeDOMElem.append(LightTheme);
      }
    }

    return {
      //computed
      theme,
    }
  }
});
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
