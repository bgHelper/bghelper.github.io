<template>
  <MainLayout v-bind:hasRight="true">
    <q-page class="flex flex-center">
      右侧列表测试
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'

export default {
  components : {
    MainLayout
  },
  name: 'Index',
  meta : {
    title: '游戏列表',
  }
}
</script>
