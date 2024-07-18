<script setup lang="ts">
  import FloatLabel from "primevue/floatlabel";

  import Button from "primevue/button";
  import Card from "primevue/card";
  import Divider from "primevue/divider";
  import InputText from "primevue/inputtext";
  import Password from "primevue/password";

  import RegisterDialog from "@/components/common/form/RegisterDialog.vue";

  import { computed, ref } from "vue";
  import { Router, useRouter } from "vue-router";

  import { Buffer } from "buffer";

  import { BackendHttpService } from "@/services/BackendHttpService";
  import { DecodedUserToken, UserTokenResponse } from "@/types/auth.types";

  import { useToast } from "primevue/usetoast";
  import { useUserStore } from "@/store/user";
  import { UtilsService } from "@/services/UtilsService";

  //global
  const router: Router = useRouter();
  const userStore = useUserStore();
  const toast = useToast();

  //data
  const userName = ref("");
  const userPassword = ref("");

  //computed
  const BASE_URL = computed(() => process.env.VUE_APP_BACKEND_URL);

  //methods
  const login = async function () {
    if (!userName && !userPassword) {
      // TODO: add validation and user feedback
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

      // handle tokens, set auth cookie
      const tokenInfo: DecodedUserToken = JSON.parse(Buffer.from(responseData.access_token.split(".")[1], "base64").toString("utf-8"));
      const authCoookieExpDate = new Date(tokenInfo.exp * 1000).toUTCString();
      document.cookie = `Authorization=${responseData.access_token}; expires=${authCoookieExpDate}`;

      //  handle refresh token, set refresh token cookie
      const refreshTokenInfo = JSON.parse(Buffer.from(responseData.refresh_token.split(".")[1], "base64").toString("utf-8"));
      const refreshTokenCookieExpDate = new Date(refreshTokenInfo.exp * 1000).toUTCString();
      document.cookie = `RefreshToken=${responseData.refresh_token}; expires=${refreshTokenCookieExpDate}`;
      router.push({ name: "home" });
    } catch (e) {
      const error: Error = e as Error;
      UtilsService.deleteCookie("Authorization");
      UtilsService.deleteCookie("RefreshToken");

      window.localStorage.removeItem("refreshToken");

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
  <div class="min-w-full min-h-full border-solid border-primary flex justify-center text-center">
    <div class="grid grid-cols-1 grid-rows-1">
      <Card class="self-center">
        <template #title> Login </template>
        <template #content>
          <div id="login-form">
            <div class="p-fluid">
              <FloatLabel class="mt-2">
                <InputText id="username" type="username" v-model="userName" @keyup.enter="login" />
                <label for="username">Username</label>
              </FloatLabel>
              <FloatLabel class="mt-6">
                <Password :feedback="false" id="password" v-model="userPassword" @keyup.enter="login" />
                <label for="password">Password</label>
              </FloatLabel>
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
        </template>
      </Card>
    </div>
  </div>
</template>
