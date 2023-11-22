<template>
  <div>
    <Button label="Test" @click="test = !test"></Button>
    <ScrollPanel v-if="test" class="size custombar p-0">
      <div class="container">
        <div class="row">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt odit repellendus magnam vel quidem architecto neque pariatur, fuga,
          reiciendis officia nihil laudantium earum sint, rerum fugit voluptate id quibusdam maxime? Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Quam repellendus voluptates debitis cum amet inventore vel et ratione ipsam nisi? Ducimus blanditiis impedit
          quos excepturi soluta pariatur nobis animi deleniti! Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo,
          obcaecati, nisi deleniti repellendus totam architecto provident quibusdam libero similique ad possimus repellat cumque earum
          impedit neque. Voluptatem officiis inventore aperiam! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed itaque, totam
          ullam nam officia reprehenderit amet iste suscipit culpa debitis velit excepturi autem voluptate impedit! Dolorum hic unde quidem
          omnis?
        </div>
        <div class="row">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt odit repellendus magnam vel quidem architecto neque pariatur, fuga,
          reiciendis officia nihil laudantium earum sint, rerum fugit voluptate id quibusdam maxime? Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Quam repellendus voluptates debitis cum amet inventore vel et ratione ipsam nisi? Ducimus blanditiis impedit
          quos excepturi soluta pariatur nobis animi deleniti! Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo,
          obcaecati, nisi deleniti repellendus totam architecto provident quibusdam libero similique ad possimus repellat cumque earum
          impedit neque. Voluptatem officiis inventore aperiam! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed itaque, totam
          ullam nam officia reprehenderit amet iste suscipit culpa debitis velit excepturi autem voluptate impedit! Dolorum hic unde quidem
          omnis?
        </div>
        <div class="row">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt odit repellendus magnam vel quidem architecto neque pariatur, fuga,
          reiciendis officia nihil laudantium earum sint, rerum fugit voluptate id quibusdam maxime? Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Quam repellendus voluptates debitis cum amet inventore vel et ratione ipsam nisi? Ducimus blanditiis impedit
          quos excepturi soluta pariatur nobis animi deleniti! Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo,
          obcaecati, nisi deleniti repellendus totam architecto provident quibusdam libero similique ad possimus repellat cumque earum
          impedit neque. Voluptatem officiis inventore aperiam! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed itaque, totam
          ullam nam officia reprehenderit amet iste suscipit culpa debitis velit excepturi autem voluptate impedit! Dolorum hic unde quidem
          omnis?
        </div>
      </div>
    </ScrollPanel>
  </div>
</template>

<script setup lang="ts">
  import ScrollPanel from "primevue/scrollpanel";
  import Button from "primevue/button";
  import { ref } from "@vue/reactivity";

  const test = ref(false);
</script>

<style lang="scss" scoped>
  ::v-deep(.p-scrollpanel) {
    &.custombar {
      .p-scrollpanel-wrapper {
        border-right: 9px solid var(--surface-ground);
      }

      .p-scrollpanel-bar {
        background-color: var(--primary-color);
        opacity: 1;
        transition: background-color 0.2s;

        &:hover {
          background-color: #007ad9;
        }
      }
    }
  }
  .size {
    width: calc(200px + 50px);
    height: calc(200px + 50px);
  }
</style>
