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

<script lang="ts">
import { defineComponent } from "vue";
import Toast from 'primevue/toast';

export default defineComponent({
  name: "Main",
  components: {
    Toast,
  }
})
</script>
<style scoped></style>

<!--
<template>
<div class="container">
  <div class="row">
    <div class="col">
      <h1 class="mt-5">Sticky footer with fixed navbar</h1>
      <p class="lead">Pin a footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS. A fixed navbar has been added with <code class="small">padding-top: 60px;</code> on the <code class="small">main &gt; .container</code>.</p>
      <p>Back to <a href="/docs/5.0/examples/sticky-footer/">the default sticky footer</a> minus the navbar.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatibus, deserunt ea consequatur culpa quae nihil id totam, error cum eius autem et temporibus? Sit earum voluptate fugit odio tempora.</p>
    </div>
  </div>
</div>

</template>
-->