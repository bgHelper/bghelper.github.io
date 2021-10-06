<template>
  <MainLayout :hiddenRightDrawer="true" :title="title">
    <q-page class="flex flex-center">
      本页面测试用
    </q-page>
  </MainLayout>
</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
const title = "关于"

export default {
  name: 'About',
  components : {
    MainLayout
  },
  data() {
    return {
      title
    }
  },
  meta : {
    title
  }
}
</script>
