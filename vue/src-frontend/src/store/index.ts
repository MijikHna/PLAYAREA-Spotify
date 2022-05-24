import { createStore, Store } from "vuex";

import { spotify } from "./spotify";
import { auth } from "./auth";
import { base } from "./base";

const store: Store<any> = createStore({
  modules: {
    base: base,
    auth: auth,
    spotify: spotify,
  },
});

export default store;
