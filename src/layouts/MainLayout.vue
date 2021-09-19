<template>
  <q-layout view="hHh lpr lFr">
    <q-header class="bg-primary text-white">
      <q-toolbar>
        <q-btn :class="{ invisible : hiddenLeft }" dense flat round icon="arrow_back" @click="$router.go(-1)" /> 
        <q-toolbar-title class="text-center">
          <slot name="title">未配置标题</slot>
        </q-toolbar-title>
        <q-btn :class="{ invisible : hiddenRight }" dense flat round icon="more_horiz" @click="right = !right" /> 
      </q-toolbar>
    </q-header>
    <q-drawer v-if="!hiddenRight" show-if-above v-model="right" side="right" content-class="bg-grey-1">
      <slot name="rightList">未配置右边栏</slot>
    </q-drawer>

    <q-page-container>
      <slot class="text-center" name="default" >未配置内容</slot>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name : "MainLayout",
  props: {
    hiddenLeft: {
      type: Boolean,
      default: false
    },
    hiddenRight: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      right: false,
    }
  }
}
</script>
