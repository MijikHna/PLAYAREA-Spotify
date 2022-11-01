<template>
  <Card class="m-5">
    <template #title> Your Profile Settings </template>
    <template #content>
      <div class="d-inline-block">
        <div>
          <div class="d-inline-block p-float-label my-2">
            <Dropdown id="theme" v-model="theme" :options="themeOptions" />
            <label for="theme">Theme</label>
          </div>
        </div>
        <div>
          <div class="d-inline-block p-float-label my-2">
            <Dropdown id="image" v-model="image" :options="imageOptions" />
            <label for="image">Image</label>
          </div>
        </div>
        <div>
          <FileUpload
            name="userImage"
            accept="image/*"
            :maxFileSize="1000000"
            customUpload
            @uploader="addPicture"
          >
            <template #empty>
              <p>Drag and drop files to here to upload.</p>
            </template>
          </FileUpload>
        </div>
      </div>
    </template>
    <template #footer>
      <Button
        icon="pi pi-check"
        label="Save"
        @click="updateProfile"
        iconPos="right"
      />
      <!-- <Button icon="pi pi-times" label="Cancel" iconPos="right" class="p-button-secondary" style="margin-left: .5em" /> -->
    </template>
  </Card>
</template>

<script setup lang="ts">
import Card from "primevue/card";
import Dropdown from "primevue/dropdown";
import FileUpload from "primevue/fileupload";
import Button from "primevue/button";
import { useToast } from "primevue/usetoast";

import { Ref, ref } from "@vue/reactivity";
import { onMounted } from "@vue/runtime-core";

import { AxiosResponse } from "axios";

import { useAuthStore } from "@/store/auth";
import { BackendHttpService } from "@/services/BackendHttpService";

//global
const toast = useToast();
const authStore = useAuthStore();

// data
const pictureUrl: Ref<string> = ref(
  `${window.location.hostname}:8000/api/profiles/picture`,
);
const profileId: Ref<number> = ref(null);
const theme: Ref<string> = ref("");
const themeOptions: Ref<string[]> = ref([]);
const image: Ref<string> = ref("");
const imageOptions: Ref<string[]> = ref([]);

onMounted(() => {
  profileId.value = authStore.activeUser.profile.id;
  theme.value = authStore.activeUser.profile.theme;
  themeOptions.value = authStore.activeUser.profile.theme_options;
  image.value = authStore.activeUser.profile.image;
  imageOptions.value = authStore.activeUser.profile.image_options;
});

// methods
const updateProfile = async function (): Promise<void> {
  try {
    const response: AxiosResponse = await BackendHttpService.updateUserProfile({
      id: profileId.value,
      theme: theme.value,
      image: image.value,
      user_id: authStore.activeUser.profile.user_id,
    });

    authStore.activeUser.profile = response.data;
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Your profile couldn't be updated",
      life: 5000,
    });
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
    const response: AxiosResponse = await BackendHttpService.addPicture(
      formData,
    );
    console.log(response.data);
    authStore.activeUser.profile = response.data;
    console.log(authStore.activeUser.profile.value);
  } catch (e) {
    toast.add({
      severity: "error",
      summary: "Your picture couldn't be added",
      life: 5000,
    });
  }

  toast.add({
    severity: "success",
    summary: "Your picture has been added",
    life: 5000,
  });
};
</script>
