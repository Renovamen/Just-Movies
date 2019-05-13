<template>
  <div id="app">
    <web-banner></web-banner>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
  import WebBanner from './components/Banner.vue'
  export default {
    name: 'App',
    components: {
      WebBanner
    }
  }
</script>

<style>
  
</style>
