<template>
  <div id="app">
    <header>
      <img src="./assets/logo.png">
    </header>
    <router-view/>
  </div>
</template>

<script>
const SocialSharing = require('vue-social-sharing');

export default {
  components: {
    SocialSharing,
  },
  name: 'App',
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Teko', 'sans-serif';
    text-transform: uppercase;
    text-align: center;
}

html,
body {
    font-size: 24px;
    text-rendering: optimizeLegibility;
    height: 100vh;
}

.row,
header {
  width: 1140px;
  margin: 0 auto;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  height: 42px;
  position: relative;
  border-bottom: 1px solid darkgrey;
  padding: 6px;
  margin: 0 auto;
  width: 80%;
}

header img {
  display: relative;
  margin: 0 auto;
  height: 80%;
  color: white;
}
</style>
