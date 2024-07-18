import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";


import "@/assets/css/main.css";
import "@/assets/css/variables.css";

import "primeicons/primeicons.css";

import PrimeVue from "primevue/config";
import Auro from "@primevue/themes/aura";
import Tooltip from "primevue/tooltip";
import Ripple from "primevue/ripple";

import ToastService from "primevue/toastservice";
import DialogService from "primevue/dialogservice";

const piniaStore = createPinia();

const app = createApp(App);

app.use(piniaStore);
app.use(router);
app.use(PrimeVue, { 
  theme: { 
    preset: Auro, 
    options: { 
      darkModeSelector: ".app-dark",
    }, 
  },
  ripple: true });

app.use(ToastService);
app.use(DialogService);

app.directive("tooltip", Tooltip);
app.directive("ripple", Ripple);

app.mount("#app");
