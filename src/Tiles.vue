<template v-if="list && list.length">
<div class="gridlist-demo">
  <mu-back-top :height="1" :bottom="100" :right="50" :duration="1000" :callBack="backTopCallBack">
  </mu-back-top>
  <mu-list class="gridlist-demo-container" cols="cols">
    <mu-sub-header>Please select a show</mu-sub-header>
    <mu-list-item v-for="tile, index in list" :key="index" @click="addToCart(index)">
      <img :src="tile.image.medium" class="tile-image"/>
      <span slot="title">{{tile.name}}</span>
      <span>Rating: <b>{{tile.rating.average}}</b></span>
    </mu-list-item>
  </mu-list>
  <mu-infinite-scroll :scroller="scroller" :loading="loading" @load="loadMore" loadingText="Loading"/>
</div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'tiles',
  props: ['updateCartCount'],
  data() {
    return {
      list: [],
      showIndex: [],
      num: 0,
      loading: false,
      scroller: null,
      startingIndex: 0,
      width: 100,
      cols: 6,
    };
  },
  created() {
    this.getApiData();
  },
  mounted() {
    this.scroller = this.$root.$el.children[1];
  },
  methods: {
    getApiData() {
      axios.get(`http://api.tvmaze.com/shows?page=${this.startingIndex}`)
        .then((response) => {
          this.showIndex = response.data;
          for (let i = 0; i < 50 && i < this.showIndex.length; i += 1) {
            this.list.push(this.showIndex[i]);
          }
          this.showIndex = this.showIndex.slice(50, this.showIndex.length);
          this.cols = Math.ceil(window.innerWidth / this.width);
        });
    },
    loadMore() {
      this.loading = true;
      setTimeout(() => {
        for (let i = 0; i < 50 && i < this.showIndex.length; i += 1) {
          this.list.push(this.showIndex[i]);
        }
        this.showIndex = this.showIndex.slice(50, this.showIndex.length);
        if ((!this.showIndex.length)) {
          this.startingIndex += 1;
          this.getApiData();
        }
        this.loading = false;
      }, 2000);
    },
    addToCart(index) {
      const item = this.list[index];
      this.list.splice(index, 1);
      setTimeout(() => {
        this.updateCartCount(item);
      }, 1000);
    },
    backTopCallBack() {

    },
  },
};
</script>

<style scoped>
.gridlist-demo-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  overflow: auto;
}

.gridlist-demo{
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.tile-image {
  width: 100%;
  padding: 2px;
}

.float-button {
  margin-right: 25px;
}

</style>
