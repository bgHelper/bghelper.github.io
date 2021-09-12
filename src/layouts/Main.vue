<template>
  <q-layout view="hHh lpr lFr">
    <q-header class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          红鹤桌游
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="right = !right" />
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" content-class="bg-grey-1"
        :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
    >
      <q-list>
        <PageLink
          v-for="link in pagesData"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-drawer show-if-above v-model="right" side="right" content-class="bg-grey-1">
      右侧列表测试
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import PageLink from 'components/PageLink.vue'

const pagesData = [
  {
    title: '找游戏',
    icon: 'casino',    
    link: '/'
  },  
  {
    title: '关于',
    icon: 'info',
    link: '/About'
  }
];

export default {  
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
