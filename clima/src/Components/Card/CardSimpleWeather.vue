<template>
  <div class="wather-container">
    <img class="weather-icon" :src="data.icon" alt="icone_clima" />
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

<style scoped>
h2 {
  background: -webkit-linear-gradient(var(--w-light-primary), var(--w-white));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.wather-container {
  display: flex;
  justify-content: center;
  align-items: center;

  gap: 4px;
  padding: 7px 14px;

  background-color: var(--w-light-primary);
  border-radius: 15px;
  opacity: 50%;
  border: 1px solid var(--w-light-primary);
  color: var(--w-ligth-secondary);
}

.weather-icon {
  width: 70px;
  height: 70px;
}
</style>
