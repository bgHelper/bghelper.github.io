<template>
  <MainLayout>
    <template v-slot:title>
      关于
    </template>

    <q-page class="flex flex-center">
      本页面测试用
    </q-page>
  </MainLayout>
</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'

export default {
  name: 'About',
  components : {
    MainLayout
  },
  meta : {
    title: '关于',
  }
}
</script>
