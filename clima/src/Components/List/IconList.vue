<template>
  <div class="extra-info">
    <div class="info-box">
      <img
        src="@/assets/icons/icon_precipitacion.svg"
        alt="precipitation"
        class="icon"
      />
      <span>{{ data.precip }}%</span>
    </div>
    <div class="info-box">
      <img src="@/assets/icons/icon_vento.svg" alt="wind-speed" class="icon" />
      <span>{{ data.windspeed }}Km/h</span>
    </div>
    <div class="info-box">
      <img src="@/assets/icons/icon_nuvens.svg" alt="clouds" class="icon" />
      <span>{{ data.cloudcover }}%</span>
    </div>
    <div class="info-box">
      <img src="@/assets/icons/icon_humidity.svg" alt="humidity" class="icon" />
      <span>{{ data.humidity }}%</span>
    </div>
    <div class="info-box">
      <img
        src="@/assets/icons/icon_feels-like.svg"
        alt="sensation"
        class="icon"
      />
      <span>{{ data.feelslike }}°C</span>
    </div>
    <div class="info-box">
      <img src="@/assets/icons/icon_snowflake.svg" alt="snow" class="icon" />
      <span>{{ data.snow }}mm</span>
    </div>
    <div class="info-box">
      <img
        src="@/assets/icons/icon_solar_energy.svg"
        alt="solar-energy"
        class="icon"
      />
      <span>{{ data.solarenergy }}MJ/m²</span>
    </div>
    <div class="info-box">
      <img src="@/assets/icons/icon_UV.svg" alt="UV" class="icon" />
      <span>{{ data.uvindex }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "IconList",
  props: {
    data: Object,
  },
};
</script>

<style scoped>
.extra-info {
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.info-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
