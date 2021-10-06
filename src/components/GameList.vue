<template>
  <div class="col-xs-12 col-md-6 col-xl-4 q-pa-xs">
    <q-card flat bordered>
      <q-card-section horizontal>
        <q-img class="col-2" :src="imgUrl" :ratio="1"  />
      </q-card-section>
    </q-card> 
  </div>
</template>

<script>
//import GameItems from 'src/components/GameItems.vue'

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
    //GameItems
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
      if (val != this.item.id) {
        this.showExpanded = false
      }
    }
  },
  methods:{
    show() {
      this.$emit('input', this.item.id)
      if (this.$q.screen.gt.xs) {
        this.showDialog = true
      } else {
        if (this.showExpanded) {
          this.showExpanded = false
        }
        else {
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