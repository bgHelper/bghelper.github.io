<template>
  <q-btn class="col-5 text-h5" :icon="icon" :label="title" :to="link" stack :color="color"/>
</template>

<script>
export default {
  name: 'IndexButton',
  props: {
    title: {
      type: String,
      required: true
    },

    link: {
      type: String,
      required: true
    },

    icon: {
      type: String,
      default: ''
    },

    color: {
      type: String,
      default: 'primary'
    }
  },
}
</script>
