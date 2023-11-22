import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { createPinia } from "pinia";

import "@/assets/css/default.css";

import 'primeflex/primeflex.scss';

import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import PrimeVue from "primevue/config";
import Tooltip from "primevue/tooltip";
import Ripple from "primevue/ripple";

import ToastService from "primevue/toastservice";
import DialogService from "primevue/dialogservice";

const piniaStore = createPinia();

const app = createApp(App);

app.use(piniaStore);
app.use(router);
app.use(PrimeVue, { ripple: true });

app.use(ToastService);
app.use(DialogService);

app.directive("tooltip", Tooltip);
app.directive("ripple", Ripple);

app.mount("#app");
