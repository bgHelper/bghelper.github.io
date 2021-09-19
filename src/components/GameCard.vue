<template>
  <q-item>
    <img class="col-2" :src="imgUrl">
    {{id}}
    {{zh}}
    <slot />
  </q-item>
</template>

<script>
export default {
  name: 'GameCard',
  props: {
    id: {
      type: Number,
      required: true
    },
    zh: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      publicPath: process.env.BASE_URL
    }
  },
  computed: {
    imgUrl : function () {
      return "/img/" + this.id + ".jpg"
    }
  }
}
</script>
