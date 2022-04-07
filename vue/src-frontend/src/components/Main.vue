<template>
    <main class="container-fluid p-0">
      <div class="row full-height m-0">
        <div class="col justify-content-center p-0">
          <router-view></router-view>
        </div>
      </div>
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Main",
})
</script>
<style scoped></style>