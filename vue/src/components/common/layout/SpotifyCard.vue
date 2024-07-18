<template>
  <div class="flex flex-col justify-between bg-surface-100 hover:bg-blue-200 border-solid border-1 border-surface-200 p-2 rounded-md">
    <div class="mb-4">
      <div class="relative mx-auto m-1">
        <slot name="header-image" />
      </div>
    </div>
    <div class="mb-4 font-medium">
      <slot></slot>
    </div>
    <div class="text-center">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
