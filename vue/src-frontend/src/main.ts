import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import "@/assets/css/default.css";

import PrimeVue from "primevue/config";
import "primeicons/primeicons.css";
// import "primevue/resources/primevue.min.css";
import "primevue/resources/themes/bootstrap4-light-blue/theme.css";
import "primevue/resources/themes/bootstrap4-dark-blue/theme.css";

import Tooltip from "primevue/tooltip";

const app = createApp(App);

app.use(store);
app.use(router);
app.use(PrimeVue);

app.directive("tooltip", Tooltip);

app.mount("#app");