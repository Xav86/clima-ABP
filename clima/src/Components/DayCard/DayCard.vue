<template>
  <div>
    <div class="day">
      <h3>{{ data.weekday }}</h3>
    </div>
    <div class="daycard">
      <div class="daycard-logo">
        <img :src="data.icon" alt="icon_weather" />
      </div>
      <div class="daycard-primary">
        <h1 class="daycard-temp transition-day">{{ data.temp }}ºC</h1>
        <h5>&uArr; {{ data.tempmax }} / {{ data.tempmin }} &dArr;</h5>
        <span>
          {{ data.datetime }}
        </span>
      </div>
      <IconList :data="data" />
    </div>
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
h3 {
  color: var(--w-ligth-secondary);
}

.day {
  width: 70%;

  margin: 0 auto;
}

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
  width: 170px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--w-ligth-secondary);
}

.transition-day {
  background: -webkit-linear-gradient(
    var(--w-secondary),
    var(--w-ligth-secondary)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.daycard-logo {
  width: 150px;
  height: 100px;
  display: flex;
  justify-content: center;
}
</style>
