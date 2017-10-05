<template>
  <mu-paper class="bottom-nav">
    <mu-bottom-nav :value="bottomNav" @change="handleChange">
      <mu-bottom-nav-item value="tv" title="TV Shows" icon="ondemand_video"/>
      <mu-badge v-bind:content="downloadCount" circle secondary>
        <mu-bottom-nav-item value="downloads" title="Download cart" icon="folder" @click="showDownloads"/>
      </mu-badge>
    </mu-bottom-nav>
  </mu-paper>

</template>

<script>
export default {
  name: 'nav-bar',
  props: ['downloadCount', 'showDownloadSection'],
  data() {
    return {
      bottomNav: 'tv',
      bottomNavColor: 'tv',
    };
  },
  methods: {
    handleChange(val) {
      this.bottomNav = val;
    },
    showDownloads() {
      this.showDownloadSection();
    },
  },
};
</script>

<style scoped>
  .bottom-nav {
    padding-top: 10px;
  }
</style>
