<template>
  <q-item
    :to="link"
    :class = "showColor"
  >
    <q-item-section
      v-if="icon"
      avatar
    >
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'PageLink',
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
    }
  },
  computed: {
    showColor() {
      if (this.$route.path == this.link) {
        return "bg-primary text-white"
      }
      return "text-primary"
    }
  }
}
</script>
