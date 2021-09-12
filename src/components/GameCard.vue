<template>
  <q-item>
    <q-item-section
      avatar
    >
      <q-icon name="person" />
    </q-item-section>

    <q-item-section>
      <q-item-label>
        <slot>1</slot>
      </q-item-label>
      <q-item-label>
        <slot name="text2">2</slot>
      </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'GameCard'
}
</script>
