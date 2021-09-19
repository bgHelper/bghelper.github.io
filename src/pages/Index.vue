<template>
  <MainLayout :hiddenLeft="true" :hiddenRight="true">
    <template v-slot:title>
      {{title}} <span class= "text-caption"> {{version}} </span>
    </template>
    <q-page class="flex flex-center">      
      <div class="fit row wrap justify-center q-gutter-md">
        <IndexButton
          v-for="link in buttonData"
          :key="link.title"
          v-bind="link"
        />
      </div>
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
import IndexButton from 'components/IndexButton.vue'

const title = "红鹤桌游"
const buttonData = [
  {
    title: '列表',
    icon: 'casino',    
    link: '/List'
  },
  {
    title: '大厅',
    icon: 'table_restaurant',
    link: '/Hall'
  },
  /*
  {
    title: '收藏',
    icon: 'star',
    link: '/Favorites'
  },
  {
    title: '账户',
    icon: 'person',
    link: '/Account'
  },
  {
    title: '设定',
    icon: 'settings',
    link: '/Setting'
  },
  */
  {
    title: '关于',
    icon: 'info',
    link: '/About'
  }
];

export default {
  components : {
    MainLayout,
    IndexButton
  },
  name: 'Index',
  meta : {
    title
  },
  data () {
    return {
      title,
      version : "v1.0",
      buttonData
    }
  }
}
</script>
