<template>
  <div
    :class="
      isDay
        ? 'banner-container-day banner-container'
        : 'banner-container-night banner-container'
    "
  >
    <div class="climate-box">
      <img
        class="climate-icon"
        :src="data.icon ? `${currentWeather.icon}` : '/icons/cloudy.svg'"
        alt="climate-icon"
      />
      <div class="info-container">
        <div class="basic-info">
          <div class="top-info">
            <div>
              <h1 :class="isDay ? 'transition-day' : 'transition-night'">
                {{ currentWeather.temp }}ºC
              </h1>
              <span :class="isDay ? 'color-day' : 'color-night'">{{
                currentWeather.conditions
              }}</span>
            </div>
            <div>
              <h2 :class="isDay ? 'transition-day' : 'transition-night'">
                {{ currentWeather.time }}
              </h2>
              <span :class="isDay ? 'color-day' : 'color-night'">{{
                currentWeather.datetime
              }}</span>
            </div>
          </div>
          <div class="d-flex gap-3">
            <h3 :class="isDay ? 'color-day' : 'color-night'">
              Max: {{ currentWeather.tempmax }}
            </h3>
            <h3 :class="isDay ? 'color-day' : 'color-night'">
              Min: {{ currentWeather.tempmin }}
            </h3>
          </div>
        </div>
        <IconList :data="currentWeather" />
      </div>
    </div>
  </div>
</template>

<script>
import IconList from "./List/IconList.vue";
import moment from "moment";

export default {
  created() {
    const hour = moment().hour();
    if (hour >= 6 && hour < 18) this.isDay = true;
    else this.isDay = false;
  },
  name: "ClimateBanner",
  props: {
    data: Object,
  },
  components: {
    IconList,
  },
  data() {
    return {
      isDay: true,
    };
  },
  computed: {
    currentWeather() {
      if (!this.data || typeof this.data !== "object") return null;
      if (!Array.isArray(this.data.hours) || !this.data.hours.length)
        return this.data;

      const now = moment();

      const closestHour = this.data.hours.reduce((closest, hour) => {
        const hourMoment = moment(hour.datetime, "HH:mm:ss");
        const diff = Math.abs(now.diff(hourMoment, "minutes"));

        const closestDiff = Math.abs(
          now.diff(moment(closest.datetime, "HH:mm:ss"), "minutes"),
        );

        return diff < closestDiff ? hour : closest;
      }, this.data.hours[0]);

      return {
        ...this.data,
        icon: `/icons/${closestHour.icon || this.data.icon}.svg`,
        temp: closestHour.temp ?? this.data.temp,
        feelslike: closestHour.feelslike ?? this.data.feelslike,
        conditions: closestHour.conditions ?? this.data.conditions,
        windspeed: closestHour.windspeed ?? this.data.windspeed,
        humidity: closestHour.humidity ?? this.data.humidity,
        cloudcover: closestHour.cloudcover ?? this.data.cloudcover,
        precip: closestHour.precip ?? this.data.precip,
        uvindex: closestHour.uvindex ?? this.data.uvindex,
        snow: closestHour.snow ?? this.data.snow,
        solarenergy: closestHour.solarenergy ?? this.data.solarenergy,
        time: moment().format("LT"),
      };
    },
  },
};
</script>

<style scoped>
.transition-night {
  background: -webkit-linear-gradient(var(--w-white), var(--w-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.transition-day {
  background: -webkit-linear-gradient(
    var(--w-secondary),
    var(--w-ligth-secondary)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

h1 {
  font-size: 54px;
}
h2 {
  font-size: 32px;
}
span {
  font-size: 20px;
}

.color-night {
  color: var(--w-secondary);
}
.color-day {
  color: var(--w-ligth-secondary);
}

.banner-container {
  width: 100%;
  display: flex;
  min-height: 300px;
  justify-content: center;
  align-items: center;

  box-shadow: #63636333 0px 2px 8px 0px;
}

.banner-container-night {
  background-color: var(--w-primary);
  color: var(--w-cool-white);
}

.banner-container-day {
  background-color: var(--w-light-primary);
  color: var(--w-ligth-secondary);
}

.climate-box {
  width: 65%;
  display: flex;

  gap: 10px;
  margin: 0 auto;
}

.info-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.basic-info {
  width: 100%;
  display: flex;
  flex-direction: column;

  gap: 4px;
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
</style>
