<template>
  <div class="col-xs-12 col-sm-6 col-md-4 q-pa-xs">
    <q-card flat bordered>
      <q-img :src="imgUrl" :ratio="2" @click="show()">
        <div class="absolute-bottom text-subtitle1">
          {{item.zh}} <span class="text-caption">({{item.year}})</span>
          <div class="text-caption">
            <q-icon name="extension"/>{{disp.weight}}
            <q-icon name="people"/>{{disp.player}}
            <q-icon name="schedule"/>{{disp.ime}}
          </div>
        </div>
        <div class="absolute-top-left">
          {{disp.rates}}
        </div>
      </q-img>
      <q-slide-transition>
        <div v-show="showExpanded">
          <q-card-section>
            <GameItems :item="item" :disp="disp" :isExpand="true"/>
          </q-card-section>
          <q-separator />
          <q-card-section v-html="item.description" />
          <q-separator />
          <q-card-actions>
            <q-btn flat dense color="primary" icon="zoom_in" label="大图" @click="showImg = true"/>
            <q-space />
            <q-btn flat dense icon="explore" label="规则" :to="'/'+item.id+'/Rule'"/>
            <q-btn flat dense icon="table_restaurant" label="试玩" :to="'/'+item.id+'/Play'"/>
          </q-card-actions>
        </div>
      </q-slide-transition>
    </q-card>
    <q-dialog class="gt-xs" v-model="showDialog">
      <q-card class="my-card" style="width: 700px; max-width: 80vw;">
        <q-card-section horizontal>
          <q-img class="col-4" :src="imgUrl" @click="showImg = true" />        
          <q-card-section class="col-8">
            <div class="text-h5">
              {{ item.zh }}
            </div>
            <GameItems :item="item" :disp="disp" />
          </q-card-section>
        </q-card-section>
        <q-separator />
        <q-card-section v-html="item.description" />
        <q-separator />
          <q-card-actions>
            <q-btn flat dense color="primary" icon="zoom_in" label="大图" @click="showImg = true"/>
            <q-space />
            <q-btn flat dense icon="explore" label="规则" :to="'/'+item.id+'/Rule'"/>
            <q-btn flat dense icon="table_restaurant" label="试玩" :to="'/'+item.id+'/Play'"/>
          </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="showImg" auto-close>
      <q-img :src="imgUrl"/>
    </q-dialog>
  </div>
</template>

<script>
import GameItems from 'src/components/GameItems.vue'

function timeToDisp(t) {
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

function numToDisp(n) {
  return (Math.round(n * 10) / 10).toFixed(1)
}

export default {
  name: 'GameCard',
  components: {
    GameItems
  },
  props: {
    item: {
      type: Object,
      required: true
    },
    value:{
      type: Number,
      required: true
    }
  },
  data() {
    return {
      showDialog : false,
      showImg : false,
      showExpanded: false,
      imgUrl : '/img/' + this.item.id + '.jpg',
      disp: {
        weight: numToDisp(this.item.weight),
        rates: numToDisp(this.item.rates),
        player:  this.item.minplayers + ((this.item.minplayers == this.item.maxplayers) ? "" : ("-" + this.item.maxplayers)),
        time: timeToDisp(this.item.minplaytime) + ((this.item.minplaytime == this.item.maxplaytime) ? "" : ("-" + timeToDisp(this.item.maxplaytime))),
      }
    }
  },
  watch: {
    value : function (val, oldVal) {
      if (val == 0) {
        this.showCard = true
      }
      else if (val != this.item.id) {
        this.showCard = false
        this.showExpanded = false        
      }
    }
  },
  methods:{
    show() {
      if (this.showExpanded) {
        this.$emit('input', 0)
        this.showExpanded = false
      }
      else {
        if (this.$q.screen.gt.xs) {
          this.showDialog = true
        }
        else {
          this.$emit('input', this.item.id)
          this.showExpanded = true
        }
      }
    }
  }
}
</script>

<style>
.q-img__content > div {
  padding: 6px;
}
</style>