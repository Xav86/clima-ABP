<template>
  <div>
    <img :src="data.icon" alt="icone_clima" />
    <div>
      <h2>{{ data.temp }}°C</h2>
      <h3>{{ data.datetime }}</h3>
    </div>
    <div>
      <IconList :data="data" />
    </div>
  </div>
</template>

<script>
import IconList from "../List/IconList.vue";

export default {
  props: {
    data: Object,
  },
  components: {
    IconList,
  },
};
</script>

<style scoped></style>
