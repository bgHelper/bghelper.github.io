<template>
  <q-layout view="hHh lpr lFr">
    <q-header class="bg-primary text-white">
      <q-toolbar>
        <q-btn class="lt-md" dense flat round icon="menu" @click="left = !left" /> 
        <q-toolbar-title>
          <slot name="title">红鹤桌游</slot>
        </q-toolbar-title>
        <q-btn v-if="hasRight" dense flat round icon="more_horiz" @click="right = !right" />
      </q-toolbar>
    </q-header>
    <q-drawer show-if-above v-model="left" side="left" content-class="bg-grey-1"
        :mini="miniState"
        mini-to-overlay
        @mouseover="miniState = false"
        @mouseout="miniState = true"
    >
      <q-list padding>
        <PageLink
          v-for="link in pagesData"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>
    
    <q-drawer v-if="hasRight" show-if-above v-model="right" side="right" content-class="bg-grey-1">
      <slot name="rightList">测试错误</slot>
    </q-drawer>

    <q-page-container>
      <slot name="default">红鹤桌游</slot>
    </q-page-container>
  </q-layout>
</template>

<script>
import PageLink from 'components/PageLink.vue'

const pagesData = [
  {
    title: '列表',
    icon: 'casino',    
    link: '/'
  },
  {
    title: '大厅',
    icon: 'table_restaurant',
    link: '/Hall'
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
  {
    title: '关于',
    icon: 'info',
    link: '/About'
  }
];

export default {
  props: {
    hasRight: {
      type: Boolean,
      default: false
    }
  },
  components: { PageLink },
  data () {
    return {
      miniState: true,
      left: false,
      right: false,
      pagesData
    }
  }
}
</script>
