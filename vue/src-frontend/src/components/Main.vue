<template>
    <main class="flex-shrink-0">
      <div class="container-fluid p-0">
        <div class="row full-height m-0">
          <div class="col justify-content-center p-0">
            <router-view></router-view>
          </div>
        </div>
      </div>
    </main>
    <Toast />
</template>

<script setup lang="ts">
import Toast from 'primevue/toast';
</script>

<style scoped></style>
