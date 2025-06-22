<template>
  <div class="daycard">
    <div class="daycard-logo">
      <img :src="data.icon" alt="icon_weather" />
    </div>

    <div class="daycard-primary">
      <h1 class="daycard-temp">{{ data.temp }}ºC</h1>
      <span>
        {{ data.datetime }}
      </span>
    </div>
    <IconList :data="data" />
  </div>
</template>

<script>
import IconList from "@/Components/List/IconList.vue";

export default {
  name: "DayCard",
  props: {
    data: Object,
  },
  components: {
    IconList,
  },
};
</script>

<style scoped>
.daycard {
  width: 70%;
  display: flex;
  align-items: center;
  /* justify-content: space-between; */

  gap: 40px;
  padding: 16px 24px;
  margin: 0 auto;

  color: #2b3a4a;
  background: #f0f4fa;
  border: 1px solid #89a5d7;
  border-radius: 16px;
  box-shadow: 0 4px 12px #0000000d;
}

.daycard-primary {
  width: 150px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.daycard-logo {
  width: 150px;
  height: 100px;
  display: flex;
  justify-content: center;
}
</style>
