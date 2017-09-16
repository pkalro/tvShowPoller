<template>
  <mu-paper class="bottom-nav">
    <mu-bottom-nav :value="bottomNav" @change="handleChange">
      <mu-bottom-nav-item value="movies" title="TV Shows" icon="ondemand_video"/>
      <mu-bottom-nav-item value="music" title="Download cart" icon="music_note"/>
    </mu-bottom-nav>
  </mu-paper>

</template>

<script>
export default {
  name: 'nav-bar',
  data() {
    return {
      bottomNav: 'movies',
      bottomNavColor: 'movies',
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
