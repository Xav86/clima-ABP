<template>
  <div class="banner-container">
    <div class="climate-box">
      <img
        class="climate-icon"
        src="@/assets/icons/NoiteNublada.svg"
        alt="climate-icon"
      />
      <div class="info-container">
        <div class="top-info">
          <div>
            <h1>{{ data.temp }}ºC</h1>
            <span class="secondary-color">Parcialmente Nublado</span>
          </div>
          <div>
            <h2>5:00AM</h2>
            <span class="secondary-color">05/05/2025</span>
          </div>
        </div>
        <div class="extra-info">
          <div class="info-box">
            <img
              src="@/assets/icons/icon_precipitacion.svg"
              alt="precipitation"
              class="icon"
            />
            <span>0%</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_vento.svg"
              alt="wind-speed"
              class="icon"
            />
            <span>6Km/h</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_nuvens.svg"
              alt="clouds"
              class="icon"
            />
            <span>46%</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_humidity.svg"
              alt="humidity"
              class="icon"
            />
            <span>87%</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_feels-like.svg"
              alt="sensation"
              class="icon"
            />
            <span>14°C</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_snowflake.svg"
              alt="snow"
              class="icon"
            />
            <span>0mm</span>
          </div>
          <div class="info-box">
            <img
              src="@/assets/icons/icon_solar_energy.svg"
              alt="solar-energy"
              class="icon"
            />
            <span>0MJ/m²</span>
          </div>
          <div class="info-box">
            <img src="@/assets/icons/icon_UV.svg" alt="UV" class="icon" />
            <span>0</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ClimateBanner",
  props: {
    data: Object,
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

.secondary-color {
  color: var(--secondary);
}
</style>
