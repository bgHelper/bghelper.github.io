<template>
  <MainLayout>
    <template v-slot:title>
      {{title}}
    </template>
    <template v-slot:rightList>
      <div class="q-pa-md">
        <q-input v-model="filter.name" label="名称筛选" />
        <q-input v-model="filter.players.min" label="最小人数" />
        <q-input v-model="filter.players.max" label="最大人数" />
      </div>
    </template>
    <q-page class="flex flex-center">
      <GameCard
        v-for="item in showItems(filter)"
        :key = "item.id"
        v-bind="item"
      >
      </GameCard>
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
import GameCard from 'components/GameCard.vue'
import gameData from './gameData'
const title = "列表"

export default {
  components : {
    MainLayout,
    GameCard
  },
  name: 'List',
  meta : {
    title,
  },
  methods : {
    showItems(filter) {
      return this.gameData.list.filter(function(item) {
        if (!item.en.toLowerCase().includes(filter.name.toLowerCase()) && !item.zh.includes(filter.name)) {
          return false
        }
        if (item.maxplayers < filter.players.min) {
          return false
        }
        if (item.minplayers > filter.players.max) {
          return false
        }
        return true
      }).sort(function(a, b) {
        return a.id - b.id
      })
    }
  },
  data () {
    return {
      title,
      gameData,
      sortKey : "ranks",      
      filter : {
        name : "",
        players: {
          min: 1,
          max: 6
        }
      }
    }
  }
}
</script>
