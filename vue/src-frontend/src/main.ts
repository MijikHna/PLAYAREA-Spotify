import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import "@/assets/css/default.css";

// import "primevue/resources/themes/bootstrap4-dark-blue/theme.css";
// import "primevue/resources/themes/bootstrap4-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import PrimeVue from "primevue/config";
import Tooltip from "primevue/tooltip";
import ToastService from "primevue/toastservice";

const app = createApp(App);

app.use(store);
app.use(router);
app.use(PrimeVue, { ripple: true });

app.use(ToastService);

app.directive("tooltip", Tooltip);

app.mount("#app");
