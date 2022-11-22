<template>
  <Dialog
    v-model:visible="show"
    position="right"
    closable
    closeOnEscape
    modal
    dismissableMask
    ref="dialog"
  >
    <template #header>
      <h3>Welcome to PLAYAREA3</h3>
    </template>

    <div class="container px-5">
      <div class="row text-start">
        <div class="row my-2">
          <InputText id="username" type="text" v-model="userCreate.username" />
          <label for="username">Username</label>
        </div>
        <div class="row my-2">
          <InputText id="email" type="text" v-model="userCreate.email" />
          <label for="email">Email</label>
        </div>
        <div class="row my-2">
          <Password class="px-0" id="password" v-model="userCreate.password" />
          <label for="password">Password</label>
        </div>
        <div class="row my-2">
          <Password
            class="px-0"
            id="password_confirm"
            v-model="userCreate.password_confirm"
          />
          <label for="password">Confirm password</label>
        </div>
      </div>
    </div>

    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="$emit('hide')"
      />
      <Button
        label="Create Account"
        icon="pi pi-check"
        autofocus
        @click="registerUser"
      />
    </template>
  </Dialog>
</template>

<script setup lang="ts">
  import Dialog from "primevue/dialog";
  import Button from "primevue/button";
  import InputText from "primevue/inputtext";
  import Password from "primevue/password";
  import { useToast } from "primevue/usetoast";

  import { ref, Ref } from "vue";

  import { User, UserCreate } from "@/interfaces/baseInterfaces";
  import { BackendHttpService } from "@/services/BackendHttpService";

  defineProps<{
    show: boolean;
  }>();

  // global
  const toast = useToast();

  // data
  const userCreate: Ref<UserCreate> = ref({
    username: "",
    email: "",
    password: "",
    password_confirm: "",
  });

  const dialog = ref();

  // methods
  const registerUser = async function () {
    dialog.value.close();

    try {
      const response = await BackendHttpService.createUser(userCreate.value);
      const user: User = response.data;
      toast.add({
        severity: "success",
        summary: `You account has been created`,
        detail: `Username: ${user.username}, Email: ${user.email}`,
        life: 5000,
      });
    } catch (e) {
      toast.add({
        severity: "error",
        summary: `You account couldn't be created`,
        detail: `????`,
        life: 5000,
      });

      return;
    }
  };
</script>
