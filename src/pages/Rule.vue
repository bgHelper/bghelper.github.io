<template>
  <MainLayout>
    <template v-slot:title>
      {{title}}
    </template>
    <template v-slot:rightList>
      规则列表
    </template>
    <q-page class="flex flex-center row items-start justify-evenly content-center">
      规则详情
    </q-page>
  </MainLayout>

</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'
import gameData from '../assets/gameList'
const title = "列表"

export default {
  components : {
    MainLayout,
  },
  name: 'List',
  meta() {
    return {
      title : this.$route.params.gid,
    }    
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
        if (filter.mechanic.include) {
          for (var idx = 0; idx < filter.mechanic.include.length; idx++) {
            var id = filter.mechanic.include[idx].value
            if (!item.mechanic.includes(id)) {
              return false
            }
          }
        }
        if (filter.mechanic.exclude) {
          for (var idx = 0; idx < filter.mechanic.exclude.length; idx++) {
            var id = filter.mechanic.exclude[idx].value
            if (item.mechanic.includes(id)) {
              return false
            }
          }
        }
        return true
      }).sort(function(a, b) {
        return a.id - b.id
      })
    }
  },
  data () {
    //$route.params
    return {
      title : this.$route.params.gid,
      gameData,
      sortKey : "ranks",      
      filter : {
        name : "",
        players: {
          min: 1,
          max: 6
        },
        mechanic : {
          include : [],
          exclude : [],
        }
      }
    }
  }
}
</script>
