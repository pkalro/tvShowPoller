<template>
<div>
  <app-bar/>
  <tiles :update-cart-count = "updateCartCount"/>
  <nav-bar :download-count = "count"/>
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
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    updateCartCount() {
      this.count += 1;
    },
  },
};
</script>
