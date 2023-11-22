<script setup lang="ts">
import Button from "primevue/button";
import Card from "primevue/card";
import Divider from "primevue/divider";
import InputText from "primevue/inputtext";
import Password from "primevue/password";

import RegisterDialog from "@/components/Base/RegisterDialog.vue";

import { computed, ref } from "vue";
import { Router, useRouter } from "vue-router";


import { Buffer } from "buffer";

import { BackendHttpService } from "@/services/BackendHttpService";
import { DecodedUserToken, UserTokenResponse } from "@/types/auth.types";

import { useToast } from "primevue/usetoast";

//global
const router: Router = useRouter();
const toast = useToast();


//data
const userName = ref("");
const userPassword = ref("");


//computed
const BASE_URL = computed(() => process.env.VUE_APP_BACKEND_URL);

//methods
const login = async function () {
  if (!userName && !userPassword) {
    console.log("fill the fields");
    return;
  }

  try {
    // get token
    let response = await BackendHttpService.http.post(`${BASE_URL.value}/auth/token`, {
      login_identifier: userName.value,
      password: userPassword.value,
    });

    const responseData = response.data as UserTokenResponse;

    const tokenInfo: DecodedUserToken =
      JSON.parse(Buffer.from(responseData.access_token.split(".")[1], "base64").toString("utf-8"));
    const authCoookieExpDate = new Date(tokenInfo.exp * 1000).toUTCString();

    document.cookie = `Authorization=${responseData.access_token}; expires=${authCoookieExpDate}`;



    router.push({ name: "home" });
  } catch (e) {
    const error: Error = e as Error;

    document.cookie = `Authorization=; expires=${new Date(0).toUTCString()}`;

    toast.add({
      severity: "error",
      summary: "Error on login",
      detail: error.message,
      life: 5000,
    });
  }
};
</script>

<template>
  <div class="min-w-full min-h-full border-solid border-primary flex justify-content-center flex-wrap">
    <div class="flex align-self-center align-items-center">
      <Card>
        <template #title> Login </template>
        <template #content>
          <div id="login-form">
            <div class="p-fluid">
              <div class="p-field p-float-label mt-2">
                <InputText id="username" type="username" v-model="userName" @keyup.enter="login" />
                <label class="p-d-block text-start" for="username">Username</label>
              </div>
              <div class="p-field p-float-label mt-4">
                <Password :feedback="false" id="password" v-model="userPassword" @keyup.enter="login" />
                <label class="p-d-block text-start" for="password">Password</label>
              </div>
              <Button label="Login" @click="login" class="mt-3" />
            </div>
            <Divider />
            <div>
              <div>
                <span>You don't have an account</span>
              </div>
              <div class="mt-2">
                <RegisterDialog />
              </div>
            </div>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>
