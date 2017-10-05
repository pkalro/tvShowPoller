<template v-if="isDownloadSectionVisible && cart.length">
  <div class="gridlist-demo-container">
    <mu-flat-button label="Download the selected shows" class="demo-flat-button" icon="folder" secondary/>
    <mu-divider/>
    <mu-grid-list class="gridlist-inline-demo">
      <mu-grid-tile v-for="tile, index in cart" :key="index">
        <img :src="tile.image.medium" class="tile-image"/>
        <span slot="title">{{tile.name}}</span>
        <span slot="subTitle">Rating: <b>{{tile.rating.average}}</b></span>
        <mu-icon-button icon="star_border" slot="action"/>
      </mu-grid-tile>
    </mu-grid-list>
      <mu-divider/>
  </div>
</template>

<script>
export default {
  name: 'downloads',
  props: ['cart', 'isDownloadSectionVisible'],
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
  overflow-x: auto;
}

.demo-flat-button {
  margin: 12px;
}

</style>
