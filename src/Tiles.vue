<template>
<div class="gridlist-demo-container">
  <mu-grid-list class="gridlist-demo" cols="4">
    <mu-sub-header>Please select a show</mu-sub-header>
    <mu-grid-tile v-for="tile, index in list" :key="index">
      <img :src="tile.image" class="tile-image"/>
      <span slot="title">{{tile.title}}</span>
      <span slot="subTitle">by <b>{{tile.author}}</b></span>
      <mu-float-button secondary mini icon="add" slot="action" class="float-button"/>
    </mu-grid-tile>
  </mu-grid-list>
</div>

</template>

<script>

import narcos from './narcos.jpg';
import batman from './batman.jpg';

export default {
  name: 'tiles',
  data() {
    return {
      list: [{
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      {
        image: narcos,
        title: 'Breakfast',
        author: 'Myron',
      }, {
        image: batman,
        title: 'Burger',
        author: 'Linyu',
      },
      ],
    };
  },
};
</script>

<style scoped>
.gridlist-demo-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.gridlist-demo{
  width: 100%;
  height: 700px;
  overflow-y: auto;
}

.tile-image {
  width: 100%;
  padding: 5px;
}

.float-button {
  margin-right: 12px;
}
</style>
