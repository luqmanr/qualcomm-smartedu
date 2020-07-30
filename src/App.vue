<template>

  <div>
      <app-header class='header'></app-header>
      <router-view class='main-app'></router-view>
  </div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import LandingPage from './components/LandingPage.vue'
import Header from './components/HeaderComponents/Header.vue' 

export default {
  name: 'App',
  components: {
    "app-header" : Header
    // HelloWorld,
    // LandingPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.header {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-app {
  height: 100vh;
}
</style>
