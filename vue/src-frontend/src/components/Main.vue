<template>
    <main class="flex-shrink-0">
        <router-view></router-view>
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Main",
})
</script>
<style scoped></style>