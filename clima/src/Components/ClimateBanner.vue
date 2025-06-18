<template>
  <div class="banner-container">
    <div class="climate-box">
      <img class="climate-icon" :src="data.icon" alt="climate-icon" />
      <div class="info-container">
        <div class="top-info">
          <div>
            <h1>{{ data.temp }}ºC</h1>
            <span class="secondary-color">{{ data.description }}</span>
          </div>
          <div>
            <h2>{{ data.time }}</h2>
            <span class="secondary-color">{{ data.datetime }}</span>
          </div>
        </div>
        <IconList :data="data" />
      </div>
    </div>
  </div>
</template>

<script>
import IconList from "./List/IconList.vue";

export default {
  name: "ClimateBanner",
  props: {
    data: Object,
  },
  components: {
    IconList,
  },
};
</script>

<style scoped>
h1,
h2 {
  background: -webkit-linear-gradient(var(--white), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

h1 {
  font-size: 54px;
}
h2 {
  font-size: 32px;
}

.banner-container {
  width: 100%;
  display: flex;
  min-height: 300px;
  justify-content: center;
  align-items: center;

  padding: 0 15rem;

  background-color: var(--primary);
  color: var(--cool-white);
  box-shadow: #63636333 0px 2px 8px 0px;
}

.climate-box {
  width: 100%;
  display: flex;

  gap: 10px;
}

.info-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.top-info {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.climate-icon {
  max-width: 250px;
  max-height: 250px;
}

.secondary-color {
  color: var(--secondary);
}
</style>
