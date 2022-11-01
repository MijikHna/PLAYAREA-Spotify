<template>
  <div
    contenteditable
    ref="theCell"
    @click="selectMode"
    @keydown.tab="selectCell"
    @blur="update"
    @input="updateCellContent"
    class="border overflow-hidden text-nowrap align-middle"
    :value="cellContent"
    :style="{ width: width + 'px', height: height + 'px' }"
  >
    {{ cellContent }}
  </div>
</template>

<script setup lang="ts">
  import { Cell } from "@/constants";
  import { computed, ComputedRef, Ref, ref } from "@vue/reactivity";
  import { onMounted } from "@vue/runtime-core";

  const props = defineProps<{
    cell: Object;
    width: number;
    height: number;
  }>();

  // data
  const cellContent: Ref<string> = ref("");

  // computed
  const editable: ComputedRef = computed(() => {
    return (
      props.cell.mode === Cell.EDIT || props.cell.mode === Cell.SELECT || false
    );
  });

  onMounted(() => {
    cellContent.value = props.cell.content;
  });

  // methods
  const updateCellContent = function (event) {
    cellContent.value = event.target.innerHTML;
  };
</script>
