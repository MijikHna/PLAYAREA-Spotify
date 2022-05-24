<template>
  <div class="container">
    <div class="row full-height">
      <div class="col d-flex justify-content-center align-items-center">
        <Card>
          <template #title>
            Login
          </template>
          <template #content>
            <div id="login-form">
              <div>
                <label class="d-block text-start" for="username">Username</label>
                <InputText class="d-block" id="username" type="username" v-model="userName" @keyup.enter="login"/>
              </div>
              <div>
                <label class="d-block text-start" for="password">Password</label>
                <Password class="d-block" :feedback="false" id="password" v-model="userPassword" @keyup.enter="login" />
              </div>
              <Button label="Login" @click="login" class="mt-3" />
            </div>
            <Divider />
            <div>
              <div>
                <span>You don't have an account</span>
              </div>
              <div class="mt-2">
                <Button
                  label="Create an account"
                  @click="showRegisterDialog = !showRegisterDialog">
                </Button>
                <RegisterDialog
                  :show="showRegisterDialog"
                  @hide="showRegisterDialog=false"
                />
              </div>
            </div>
          </template>
        </Card>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Card from 'primevue/card';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';
import Divider from 'primevue/divider';

import RegisterDialog from '@/components/Base/RegisterDialog.vue'

import {defineComponent, computed, ref } from "vue";
import { Store, useStore } from 'vuex';
import { Buffer } from 'buffer';

import axios from 'axios';
import { Router, useRouter } from 'vue-router';
import { DecodesUserToken } from '@/interfaces/baseInterfaces';
import RegisterDialog from '../components/Base/RegisterDialog.vue';

export default defineComponent({
  name: "Login",
  components: {
    Card,
    InputText,
    Password,
    Button,
    Divider,
    RegisterDialog
},
  setup(){
    //global
    const store: Store<any> = useStore();
    const router: Router = useRouter()

    //data
    const userName = ref("");
    const userPassword = ref("");
    const BASE_URL = computed(() => {
      return process.env.VUE_APP_BACKEND_URL
    });
    const showRegisterDialog = ref(false);

    //methods
    const login = async function() {
      if (!userName && !userPassword ) {
        console.log("fill the fields");
        return;
      }
      try {
        const response = await axios.post(
          `${BASE_URL.value}/auth/token`,
          {
            username: userName.value,
            password: userPassword.value
          },
        )

        const tokenInfo: DecodesUserToken = JSON.parse(
          Buffer
            .from(response.data.access_token.split('.')[1], 'base64')
            .toString('utf-8')
        );

        document.cookie = `Authorization=${JSON.stringify(response.data)}; expires=${new Date(tokenInfo.exp * 1000).toUTCString()}`;

        // const logoutTimerId = setTimeout(store.commit('setActiveUser', null), );
        store.commit("setActiveUser", tokenInfo);
        store.commit("setAuth", true);
        // store.commit("setActiveUserLogoutTimer", logoutTimerId)

        router.push({name: 'home'});
      }
      catch(e) {
        console.log(e)
      }
    }

    return {
      //data
      userName,
      userPassword,
      showRegisterDialog,
      //methods
      login
    }
  }
});
</script>