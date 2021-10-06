<template>
  <div class="flex row">
    <div :class="itemClass">
      出版：<q-chip>{{item.year}}</q-chip>
    </div>
    <div :class="itemClass">
      人数：<q-chip>{{disp.player}}</q-chip>
    </div >
    <div :class="itemClass">
      时间：<q-chip>{{disp.time}}</q-chip>
    </div>
    <div :class="itemClass">
      重度：<q-chip>{{disp.weight}}</q-chip>
    </div >
    <div :class="itemClass">
      评分：<q-chip>{{disp.rates}}</q-chip>
    </div >
    <div :class="itemClass">
      年龄：<q-chip>{{item.minage}}+</q-chip>
    </div >
    <div class="col-12">
      排名：
      <q-chip v-if="item.ranks.length == 0">无</q-chip>
      <span v-else v-for="(r,index) in item.ranks" :key="index">
        <span v-if="index != 0"> / </span>
        <q-chip>{{r.label}} : {{r.val}}</q-chip>
      </span>
    </div>
    <div class="col-12">
      机制：
      <span v-for="(m, index) in item.mechanic" :key="index">
        <span v-if="index != 0"> / </span>
        <q-chip>{{m}}</q-chip>
      </span>
    </div>
  </div>
</template>

<script>

export default {
  name: 'GameCardItems',
  props: {
    item: {
      type: Object,
      required: true
    },
    disp: {
      type: Object,
      required: true
    },
    isExpand: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      itemClass: "col-xs-6 col-md-4"
    }
  }
}
</script>
