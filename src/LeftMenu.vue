<template>
<div class="content-left">
      <div class="logo">
        TVP
      </div>
      <mu-list>
        <mu-list-item title="Show list" value="list1" >
          <mu-icon slot="left" value="send" />
        </mu-list-item>
        <mu-list-item title="Download cart" value="list2">
          <mu-badge v-bind:content="downloadCount.toString()" secondary slot="after" />
        </mu-list-item>
      </mu-list>
</div>
</template>

<script>

export default {
  name: 'left-menu',
  props: ['downloadCount'],
};
</script>

<style scoped>

.content-left{
width: 30%;
float: left;
background-color: rgb(225, 225, 225);
margin-bottom: -4000px;
padding-bottom: 4000px;
}


</style>
