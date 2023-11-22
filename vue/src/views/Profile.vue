<template>
  <div class="min-w-full min-h-full border-solid border-primary flex justify-content-center flex-wrap">
    <div class="flex align-self-center align-items-center">
      <Card class="m-5">
        <template #title> Your Profile Settings </template>
        <template #content>
          <div class="p-d-flex p-jc-center">
            <div class="p-d-flex p-flex-column">
              <div class="flex items-center mt-2">
                <Checkbox inputId="dark-theme" v-model="user.profile.dark_theme" :binary="true" />
                <label for="dark-theme" class="ml-3">Dark Theme</label>
              </div>
              <div class="p-d-flex p-ai-center items-center my-2">
                <div class="w-full p-float-label mt-4">
                  <Dropdown inputId="active-image" v-model="user.profile.active_image" :options="user.profile.images"
                    class="w-full" />
                  <label for="active-image" class="ml-2">Image</label>
                </div>
              </div>
              <div class="p-d-flex p-ai-center mt-4">
                <FileUpload name="userImage" accept="image/*" customUpload :maxFileSize="1000000" @uploader="addPicture"
                  class="p-mr-2">
                  <template #empty>
                    <p>Drag and drop files to here to upload.</p>
                  </template>
                </FileUpload>
              </div>
            </div>
          </div>
        </template>
        <template #footer>
          <Button icon="pi pi-check" label="Save" @click="updateProfile" iconPos="right" />
        </template>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import Button from "primevue/button";
import Card from "primevue/card";
import Checkbox from 'primevue/checkbox';
import Dropdown from "primevue/dropdown";
import FileUpload from "primevue/fileupload";

import { useToast } from "primevue/usetoast";

import { AxiosResponse } from "axios";

import { BackendHttpService } from "@/services/BackendHttpService";
import { useUserStore } from "@/store/user";
import { storeToRefs } from "pinia";

//global
const toast = useToast();
const userStore = useUserStore();

// data
const { user } = storeToRefs(userStore);

// methods
const updateProfile = async function (): Promise<void> {
  try {
    const response: AxiosResponse = await BackendHttpService.http.put('/users/profile', {
      id: user.value.profile.id,
      dark_theme: user.value.profile.dark_theme,
      active_image: user.value.profile.active_image,
    });

    if (response.status !== 200) throw new Error(response.data);

    user.value.profile = response.data;
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Your profile couldn't be updated",
      life: 5000,
    });
    throw e;
  }

  toast.add({
    severity: "success",
    summary: "Your profile has been updated",
    life: 5000,
  });
};

const addPicture = async function (event: any): Promise<void> {
  const formData: FormData = new FormData();
  formData.append("image", event.files[0]);
  try {
    const response: AxiosResponse =
      await BackendHttpService.http.post(
        '/users/profile/image',
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

    if (response.status !== 201) throw new Error(response.data);

    user.profile = response.data;
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Your picture couldn't be added",
      life: 5000,
    });
    throw e;
  }

  toast.add({
    severity: "success",
    summary: "Your picture has been added",
    life: 5000,
  });
};
</script>
