<template>
  <router-link :to="'/' + item.id" class="col-xs-12 col-sm-6 col-md-4 q-pa-xs">
  <q-card flat bordered>
    <q-img :src="'/img/' + item.id + '.jpg'" :ratio="2">
      <div class="absolute-bottom text-subtitle1">
        {{item.zh}} <span class="text-caption">({{item.year}})</span>
        <div class="text-caption">
          <q-icon name="extension"/>{{dispNum(item.weight)}}
          <q-icon name="people"/>{{item.minplayers}}<span v-if="item.minplayers != item.maxplayers">-{{item.maxplayers}}</span>{{" "}}
          <q-icon name="schedule"/>{{dispTime(item.minplaytime)}}<span v-if="item.minplaytime != item.maxplaytime">-{{dispTime(item.maxplaytime)}}</span>
        </div>
      </div>
      <div class="absolute-top-left">
        {{dispNum(item.rates)}}
      </div>
    </q-img>      
  </q-card>
  </router-link>
</template>

<script>
export default {
  name: 'GameCard',
  props: {
    item: {
      type: Object,
      required: true
    },
    dispData: {
      type: Object,
      required: true
    }
  },
  methods: {
    dispNum(num) {
      return (Math.round(num * 10) / 10).toFixed(1)
    },
    dispTime(t) {
      let h = t / 60
      let m = t % 60
      let output = ""
      if (h != 0) {
        output = h + "h"
      }
      if (m != 0) {
        output = m + "m"
      }
      return output
    }
  },
}
</script>
