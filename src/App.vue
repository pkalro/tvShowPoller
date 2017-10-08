<template>
<div class='layout'>
  <app-bar/>
  <left-menu :download-count = "downloadCount"/>
  <div class="content-right">
  <!-- <mu-flat-button label="Download the selected shows" class="demo-flat-button" icon="folder" secondary @click="downloadShows"/> -->
   <!-- <downloads :cart="cart" :is-download-section-visible="isDownloadSectionVisible"/> -->
   <!-- <downloads :cart="cart" />
  <tiles :update-cart-count = "updateCartCount"/> -->
  <router-view></router-view>
</div>
  <!-- <nav-bar :download-count = "count"/> -->
</div>
</template>

<script>
import axios from 'axios';
import AppBar from './AppBar';
import Tiles from './Tiles';
import NavBar from './NavBar';
import Downloads from './Downloads';
import LeftMenu from './LeftMenu';

export default {
  name: 'app',
  components: {
    AppBar,
    LeftMenu,
    Tiles,
    NavBar,
    Downloads,
  },
  props: ['downloadCount'],
  // data() {
  //   return {
  //     count: 0,
  //     cart: [],
  //   };
  // },
  methods: {
    updateCartCount(item) {
      this.count += 1;
      this.cart.push(item);
    },
    showDownloadSection() {
      this.isDownloadSectionVisible = true;
    },
    downloadShows() {
      axios.post('http://localhost:6969/download', { showList: this.cart.map(c => c.name) })
      .then(() => {});
    },
  },
};
</script>

<style scoped>

.layout {
  height: 100%;
}

.content-right{
  width: 70%;
  display: inline-block;
  float: right;
  background-color: rgb(236, 236, 236);
}

</style>
