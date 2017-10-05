<template>
<div>
  <app-bar/>
   <downloads :cart="cart" :is-download-section-visible="isDownloadSectionVisible"/>
  <tiles :update-cart-count = "updateCartCount"/>
  <nav-bar :download-count = "count"/>
</div>
</template>

<script>
import AppBar from './AppBar';
import Tiles from './Tiles';
import NavBar from './NavBar';
import Downloads from './Downloads';

export default {
  name: 'app',
  components: {
    AppBar,
    Tiles,
    NavBar,
    Downloads,
  },
  data() {
    return {
      count: 0,
      cart: [],
      isDownloadSectionVisible: false,
    };
  },
  methods: {
    updateCartCount(item) {
      this.count += 1;
      this.cart.push(item);
    },
    showDownloadSection() {
      this.isDownloadSectionVisible = true;
    },
  },
};
</script>
