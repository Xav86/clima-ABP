<template>
  <div class="daycard">
    <div class="daycard-logo">
      <img :src="data.icon" alt="" />
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
  display: flex;
  background: #f0f4fa;
  padding: 16px 24px;
  justify-content: space-between;
  gap: 40px;
  align-items: center;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  font-family: "Segoe UI", sans-serif;
  color: #2b3a4a;
  margin: 0 auto;
  width: 70%;
  border: 1px solid #89a5d7;
}

.daycard-primary {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 16px;
}

.daycard-logo {
  margin-bottom: 12px;
  display: flex;
  justify-content: center;
  height: 100px;
}
</style>
