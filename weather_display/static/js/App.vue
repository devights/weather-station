<template>
  <div class="base">
    <navbar/>
    <main class="main" ref="main">
      <router-view />
    </main>

  </div>
</template>

<script>
  import Navbar from "./components/nav.vue"

  export default {
    name: "App",
    components: {
      Navbar
    },
    data(){
      return {
      };
    },
    computed: {
    },
    watch: {
    },
    mounted() {
    },
    methods: {

    }
  };
</script>

<style lang="scss">
  .main {
    padding: 320px;
  }
</style>
