<template>
  <div
    :contenteditable="cell.mode === EditMode.EDIT"
    ref="theCell"
    @click="selectMode"
    @keydown.tab="selectCell"
    @blur="update"
    @input="updateCellContent"
    class="border overflow-hidden text-nowrap align-middle"
    :class="modeClassObj"
    :value="cellContent"
    :style="{ width: width + 'px', height: height + 'px' }"
    tabindex="1"
  >
    {{ cellContent }}
  </div>
</template>

<script setup lang="ts">
  import { Cell } from "@/constants";
  import { computed, ComputedRef, Ref, ref } from "@vue/reactivity";
  import { onMounted } from "@vue/runtime-core";

  import { EditMode } from "@/constants";

  const props = defineProps<{
    cell: Object;
    width: number;
    height: number;
  }>();

  // data
  const cellContent: Ref<string> = ref("");

  // computed
  const modeClassObj: ComputedRef = computed(() => {
    let classValue = "border border-left-0";

    switch (props.cell.mode) {
      case EditMode.EDIT:
        classValue = "edit-border";
        break;
      case EditMode.SELECT:
        classValue = "select-border";
        break;
      default:
        classValue = "border border-left-0";
        break;
    }
    return classValue;
  });

  onMounted(() => {
    cellContent.value = props.cell.content;
  });

  // methods
  const updateCellContent = function (event) {
    cellContent.value = event.target.innerHTML;
  };
</script>

<style>
  .edit-border {
    border: 1px solid blue;
    box-shadow: inset 1px 1px blue, inset -1px -1px blue;
    padding-left: 1px;
    padding-right: 1px;
  }
  .select-border {
    border: 1px solid green;
    box-shadow: inset 1px 1px green, inset -1px -1px green;
    padding-left: 1px;
    padding-right: 1px;
  }
  [contenteditable] {
    outline: none;
  }
</style>
