<template>
  <div id = "app">
    <navbar />
    <div class = "main-content">
      <router-view />
    </div>
    <personalFooter class = "footer"/>
  </div>
</template>

<script>

import navbar from './components/NavBar.vue'
import personalFooter from './components/PersonalFooter.vue'


export default {
  name: 'App',
  components: {
    navbar,
    personalFooter,
  }
}
</script>



<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}
body {
font-family: 'Inter', sans-serif;
}
</style>
