<template>
  <mu-paper class="bottom-nav">
    <mu-bottom-nav :value="bottomNav" @change="handleChange">
      <mu-bottom-nav-item value="tv" title="TV Shows" icon="ondemand_video"/>
      <mu-badge v-bind:content="downloadCount" circle secondary>
        <mu-bottom-nav-item value="downloads" title="Download cart" icon="music_note"/>
      </mu-badge>
    </mu-bottom-nav>
  </mu-paper>

</template>

<script>
export default {
  name: 'nav-bar',
  props: ['downloadCount'],
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
  },
};
</script>

<style scoped>
  .bottom-nav {
    margin-bottom: 10px;
  }
</style>
