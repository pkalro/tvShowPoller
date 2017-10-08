<template v-if="isDownloadSectionVisible && cart.length">
  <div class="gridlist-demo-container">
    <mu-divider/>
    <mu-grid-list class="gridlist-inline-demo" cols=Number(5) >
      <mu-grid-tile v-for="tile, index in cart" :key="index">
        <img :src="tile.image.medium" class="tile-image"/>
        <span slot="title">{{tile.name}}</span>
        <span slot="subTitle">Rating: <b>{{tile.rating.average}}</b></span>
        <mu-icon-button icon="star_border" slot="action"/>
      </mu-grid-tile>
    </mu-grid-list>
      <mu-divider/>
      <mu-raised-button label="Download" class="demo-raised-button" secondary @click="downloadShows"/>
  </div>
</template>

<script>
export default {
  name: 'downloads',
  props: ['cart', 'downloadShows'],
};
</script>

<style>
.gridlist-demo-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.gridlist-demo{
  width: 500px;
  height: 100%;
  overflow-y: auto;
}

.demo-flat-button {
  margin: 12px;
}

</style>
