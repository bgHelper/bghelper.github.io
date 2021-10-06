<template>
  <MainLayout :title="title">
    <template #rightList>
      <q-list>
        <q-item class="text-h5" v-for="(line, index) in data.content" :key="index" clickable v-ripple @click="play(line)">
          {{line.title}}
        </q-item>
      </q-list>
    </template>
    
    <q-page class="flex row items-start justify-evenly content-start">
      <q-scroll-observer @scroll="scrollHandler" />
      <q-card v-for="(line, index) in data.content" :key="index" flat @click="play(line)" class="col-12">
        <q-card-section class="center">
          <div class="text-h4">
            {{line.title}}
          </div>
          <div class="text-h5"> 
            {{line.text}}
          </div>
        </q-card-section>
      </q-card>
    </q-page>
    
  </MainLayout>
</template>

<script>
import MainLayout from 'layouts/MainLayout.vue'

function importFile(params) {
  return import("../assets/"+params.gid+"/Rule")
}

let gameData = {
  zh : "秦棋攻略",
  content : [
    {
      title : "简介",
      text : "《秦棋攻略》还原秦王沙盘推演战局，是模拟战国战场的抽象棋。玩家使用20枚棋子，在8x8棋盘上排兵布阵。与传统象棋不同的是:获胜条件为达阵而非擒王。"
    },    
    {
      title : "配件",
      text : "两色棋子共四十枚，棋盘一个，提示屏风两张，沙漏两个，规则书一本，收纳袋两个。"
    }
  ]
}
export default {
  components : {
    MainLayout,
  },
  name: 'Rule',  
  data () {
    return {
      title : "未配置",
      data: gameData,
    }
  },
  beforeRouteEnter(to, from, next) {
    console.log(to.meta())
    importFile(to.params).then(
      module => {
        next(vm => vm.setData(module.default))
      }
    ).catch(
      err => {
        //next({name: "Error404"})
        next(vm => vm.setData(gameData))
      }
    )
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to.meta())
    
    importFile(to.params).then(
      module => {
        this.setData(module.default)
        next()
      }
    ).catch(
      err => {
        this.setData(gameData)
        //next({name: "Error404"})
        next()
      }
    )
  },
  methods: {
    setData(data) {
      this.data = data
      let title = "规则：" + this.data.zh;
      this.title = title
      document.title = title
    },
    play(line) {
      //console.log(Obj.srcElement.innerText)
      console.log(line)
      let url = "https://tts.baidu.com/text2audio?cuid=baike&lan=ZH&ie=utf-8&ctp=1&pdt=301&vol=9&rate=32&per=1&tex=" 
      + line.title + "：" + line.text
      new Audio(url).play()
      //console.log("aaa")
    },
    scrollHandler(pos) {
      console.log(pos)
    }
  }  
}
</script>