<template>
  <MainLayout :title="title">
    <template #rightList>
      <div class="q-pa-md">
        <q-input v-model="filter.name" label="名称筛选" />
        <q-input v-model.number="filter.players.min" min="1" :max="filter.players.max" type="number" label="最小人数" />
        <q-input v-model.number="filter.players.max" :min = "filter.players.min" max="10" type="number" label="最大人数" />
        <q-select
          multiple
          v-model="filter.mechanic.include"
          label="包含机制"
          :options="gameData.mechanic"
          use-chips
        />
        <q-select
          multiple
          v-model="filter.mechanic.exclude"
          label="排除机制"
          :options="gameData.mechanic"
          use-chips
        />
        <q-select
          v-model="filter.sort.key"
          label="排序"
          :options="sortList"
        />
        <q-toggle          
          v-model="filter.sort.reverse"
          :label="filter.sort.reverse ? '递减' : '递增'"
        />
        
        <q-input borderless v-model="gameData.update" label="数据更新时间" readonly/>
      </div>
    </template>
    <q-page v-if="showList.length == 0" class="text-h5 flex flex-center row items-start justify-evenly content-center">
      无符合条件的游戏
    </q-page>
    <q-page v-else class="flex row items-start justify-start content-start">
      <GameCard
        v-for="item in showList"
        :key="item.id"
        :item="item"
        v-model="selectId"
      />
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
import GameCard from 'components/GameCard.vue'
import gameData from '../assets/gameList'
const title = "列表"

const sortList = [
  {
    "value": "year",
    "label": "年份"
  },
  {
    "value": "rates",
    "label": "评分"
  },
  {
    "value": "weight",
    "label": "重度"
  },
]

export default {
  components : {
    MainLayout,
    GameCard
  },
  name: 'List',
  meta: {
    title ,
  },
  computed : {
    showList : function()  {
      let listFilter = this.filter
      return this.gameData.list.filter(function(item) {
        if (!item.en.toLowerCase().includes(listFilter.name.toLowerCase()) && !item.zh.includes(listFilter.name)) {
          return false
        }
        if (item.maxplayers < listFilter.players.min) {
          return false
        }
        if (item.minplayers > listFilter.players.max) {
          return false
        }
        if (listFilter.mechanic.include) {
          for (var idx = 0; idx < listFilter.mechanic.include.length; idx++) {
            var id = listFilter.mechanic.include[idx]
            if (!item.mechanic.includes(id)) {
              return false
            }
          }
        }
        if (listFilter.mechanic.exclude) {
          for (var idx = 0; idx < listFilter.mechanic.exclude.length; idx++) {
            var id = listFilter.mechanic.exclude[idx]
            if (item.mechanic.includes(id)) {
              return false
            }
          }
        }
        return true
      }).sort(function(a, b) {
        let value = listFilter.sort.key.value
        let diff = a[value] - b[value]
        if (diff == 0) {
          diff = a.id - b.id
        }
        if (listFilter.sort.reverse) {
          diff = -diff
        }
        return diff
      })
    },
  },
  data () {
    return {
      title,
      gameData,
      sortList,
      selectId: 0,
      filter : {
        name : "",
        players: {
          min: 1,
          max: 10
        },
        mechanic : {
          include : [],
          exclude : [],
        },
        sort : {
          key : sortList[0],
          reverse : false
        }
      }
    }
  }
}
</script>
