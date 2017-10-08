import Vue from 'vue';
import axios from 'axios';
import Router from 'vue-router';
import App from '../App';
import Downloads from '../Downloads';
import Tiles from '../Tiles';

Vue.use(Router);


function Store() {
  this.count = 0;
  this.cart = [];

  function updateCartCount(item) {
    this.count += 1;
    this.cart.push(item);
  }
  function downloadShows() {
    axios.post('http://localhost:6969/download', { showList: this.cart.map(c => c.name) })
    .then(() => {});
  }
  return {
    count: this.count, cart: this.cart, updateCartCount, downloadShows,
  };
}

const s = new Store();

export default new Router({
  routes: [
    {
      path: '/',
      component: App,
      props: { downloadCount: s.cart.length },
      children: [
        {
          path: '/home',
          component: Tiles,
          props: { updateCartCount: s.updateCartCount.bind(s) },
        },
        {
          path: '/downloads',
          name: 'Downloads',
          component: Downloads,
          props: { cart: s.cart, downloadShows: s.downloadShows.bind(s) },
        },
      ],
    },
  ],
});
