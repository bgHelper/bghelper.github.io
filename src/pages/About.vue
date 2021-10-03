<template>
  <MainLayout :hiddenRight="true">
    <template v-slot:title>
      {{title}}
    </template>

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
