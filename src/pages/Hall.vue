<template>
  <MainLayout :title="title">
    <q-page class="flex flex-center">
      空空如野
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
const title = "大厅"

export default {
  components : {
    MainLayout
  },
  name: 'Hall',
  meta : {
    title,
  },
  data () {
    return {
      title
    }
  }
}
</script>
