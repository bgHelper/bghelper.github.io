<template>
  <q-layout view="hHh lpr lFr">
    <q-header class="bg-primary text-white">
      <q-toolbar>
        <q-btn :class="{ invisible : hiddenBack }" dense flat round :icon="hasBack ? 'arrow_back' : 'home'"
          @click="hasBack ? $router.go(-1) : $router.push('/')" /> 
        <q-toolbar-title class="text-center">
          <slot name="title">{{title}}</slot>
        </q-toolbar-title>
        <q-btn :class="{ invisible : hiddenRightDrawer }" dense flat round icon="more_horiz" @click="right = !right" /> 
      </q-toolbar>
    </q-header>
    <q-resize-observer @resize="onPageResize" />
    <q-drawer v-if="!hiddenRightDrawer" show-if-above v-model="right" side="right" content-class="bg-grey-1">
      <q-scroll-area style="width:100%;height:100%">
        <slot name="rightList">未配置右边栏</slot>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <q-scroll-area :style="'width:100%;height:' + (pageSize.height - 50) + 'px'">
        <slot class="text-center" name="default" >未配置内容</slot>
      </q-scroll-area>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name : "MainLayout",
  props: {
    hiddenBack: {
      type: Boolean,
      default: false
    },
    hiddenRightDrawer: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      default: "未配置标题"
    }
  },
  data () {
    const hasBack = history.length > 2
    return {
      right : false,
      pageSize : { width: '0', height: '0' },
      hasBack
    }
  },
  methods :{
    onPageResize(size) {
      this.pageSize = size
    }
  }
}
</script>
