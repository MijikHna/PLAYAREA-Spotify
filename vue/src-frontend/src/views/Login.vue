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

<script setup lang="ts">
import Card from 'primevue/card';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';
import Divider from 'primevue/divider';

import RegisterDialog from '@/components/Base/RegisterDialog.vue'

import { computed, ref } from "vue";
import { Router, useRouter } from 'vue-router';

import { useAuthStore } from '@/store/auth';

import { Buffer } from 'buffer';

import axios from 'axios';

import { DecodesUserToken } from '@/interfaces/baseInterfaces';
import { BackendHttpService } from '@/services/BackendHttpService';

//global
const authStore = useAuthStore();
const router: Router = useRouter()

//data
const userName = ref("");
const userPassword = ref("");

//computed
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
    let response = await axios.post(
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

    authStore.setActiveUser(tokenInfo);

    response = await BackendHttpService.getUserProfile(tokenInfo.username);
    authStore.activeUser.userProfile = response.data;

    router.push({name: 'home'});
  }
  catch(e) {
    console.log(e)
  }
}
</script>