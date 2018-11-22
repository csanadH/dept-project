<template>
  <div id="app">
    <header>
      <img src="./assets/logo.png">
    </header>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
body,
html {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  height: 30px;
  position: relative;
  padding: 0px 20px;
  border-bottom: 1px solid darkgrey;
  padding: 6px;
  margin: 0px 64px;
}

header img {
  margin: 0 auto;
  height: 100%;
  color: white;
  filter: saturate(3);
}
</style>
