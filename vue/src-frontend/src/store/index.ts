import { createStore, Store } from "vuex";

import { spotify } from "./spotify";
import { auth } from "./auth";

const store: Store<any> = createStore({
  modules: {
    auth: auth,
    spotify: spotify,
  },
});

export default store;
