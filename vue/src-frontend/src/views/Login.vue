<template>
  <div class="container">
    <div class="row full-height">
      <div class="col d-flex justify-content-center align-items-center">
        <Card>
          <template #title>
            Login
          </template>
          <template #content>
            <div>
              <label class="d-block text-start" for="username">Username</label>
              <InputText class="d-block" id="username" type="username" v-model="userName"/>
            </div>
            <div>
              <label class="d-block text-start" for="password">Password</label>
              <Password class="d-block" :feedback="false" id="password" v-model="userPassword" />
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

import {defineComponent, computed} from "vue";

export default defineComponent({
  name: "Login",
  components: {
    Card,
    InputText,
    Password,
  },
  setup(){
    const userName = "";
    const userPassword = "";
    return {
      userName,
      userPassword,
    }
  }
});
</script>

<style scoped>
.full-height {
  min-height: calc(100vh - 56px - 56px);
}
</style>