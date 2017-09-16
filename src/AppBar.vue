<template>
<mu-appbar title="Tv Show Poller">
  <mu-text-field class="appbar-search-field" slot="right" hintText="Enter show title" icon="search"/>
</mu-appbar>
</template>

<script>
export default {
  name: 'app-bar',
};
</script>

<style lang="less" scoped>
.appbar-search-field{
  color: #FFF;
  margin-bottom: 0;
  &.focus-state {
    color: #FFF;
  }
  .mu-text-field-hint {
    color: fade(#FFF, 54%);
  }
  .mu-text-field-input {
    color: #FFF;
  }
  .mu-text-field-focus-line {
    background-color: #FFF;
  }
}
</style>
