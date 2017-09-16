<!-- <template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->


<template>
<div>
  <app-bar/>
  <tiles/>
  <nav-bar/>
</div>
</template>

<script>

import AppBar from './AppBar';
import Tiles from './Tiles';
import NavBar from './NavBar';

export default {
  name: 'app',
  components: {
    AppBar,
    Tiles,
    NavBar,
  },
};
</script>
