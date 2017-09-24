<template>
  <div class="gridlist-demo-container">
    <mu-grid-list class="gridlist-inline-demo">
      <mu-grid-tile v-for="tile, index in cart" :key="index">
        <img :src="tile.image.medium" class="tile-image"/>
        <span slot="title">{{tile.name}}</span>
        <span slot="subTitle">Rating: <b>{{tile.rating.average}}</b></span>
        <mu-icon-button icon="star_border" slot="action"/>
      </mu-grid-tile>
    </mu-grid-list>
  </br>
     <mu-divider/>
   </br>
  </div>
</template>

<script>
export default {
  name: 'downloads',
  props: ['cart'],
};
</script>

<style>
.gridlist-demo-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.gridlist-inline-demo{
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
  overflow-x: auto;
}

</style>
