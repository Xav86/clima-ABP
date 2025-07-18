<template>
  <div>
    <div class="home">
      <NavBar />
      <div class="title-box">
        <h1>Previsão do tempo de: {{ cityName }}</h1>
      </div>
      <ClimateBanner :data="data" />
      <div>
        <div class="title-box">
          <h2>Previsões da semana</h2>
        </div>
        <div class="week-list">
          <DayCard
            v-for="(day, i) in weekData"
            :key="`${i}-${day}`"
            :data="day"
          />
        </div>
      </div>
    </div>
    <FooterItem />
  </div>
</template>

<script>
import ClimateBanner from "@/Components/ClimateBanner.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";
import DayCard from "@/Components/DayCard/DayCard.vue";
import axios from "axios";
import moment from "moment";
import "moment/locale/pt-br";
import FooterItem from "@/Components/FooterItem.vue";
moment.locale("pt-br");

export default {
  name: "HomeView",
  components: {
    NavBar,
    ClimateBanner,
    DayCard,
    FooterItem,
  },
  async created() {
    try {
      const city = localStorage.getItem("location-selected");
      const cityName = localStorage.getItem("location-name");

      if (city) this.city = city;
      if (cityName) this.cityName = cityName;

      const result = await axios.get(
        `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/${this.city},BR?unitGroup=metric&lang=pt&key=DLP4WSNVQXB9XBY3A8RWXRZCR`,
      );

      this.weekData = result.data.days.slice(0, 7).map((day) => ({
        icon: `/icons/${day.icon}.svg`,
        time: moment().format("LT"),
        temp: day.temp,
        tempmax: day.tempmax,
        tempmin: day.tempmin,
        description: day.description,
        conditions: day.conditions,
        weekday: moment(day.datetime).format("dddd"),
        datetime: moment(day.datetime).format("DD/MM/YYYY"),
        precip: day.precip,
        windspeed: day.windspeed,
        cloudcover: day.cloudcover,
        humidity: day.humidity,
        feelslike: day.feelslike,
        snow: day.snow,
        solarenergy: day.solarenergy,
        uvindex: day.uvindex,
      }));

      this.data.icon = `/icons/${result.data.days[0].icon}.svg`;
      this.data.time = moment().format("LT");
      this.data.temp = result.data.days[0].temp;
      this.data.tempmax = result.data.days[0].tempmax;
      this.data.tempmin = result.data.days[0].tempmin;
      this.data.description = result.data.days[0].description;
      this.data.datetime = moment(result.data.days[0].datetime).format(
        "DD/MM/YYYY",
      );
      this.data.precip = result.data.days[0].precip;
      this.data.windspeed = result.data.days[0].windspeed;
      this.data.cloudcover = result.data.days[0].cloudcover;
      this.data.humidity = result.data.days[0].humidity;
      this.data.feelslike = result.data.days[0].feelslike;
      this.data.snow = result.data.days[0].snow;
      this.data.solarenergy = result.data.days[0].solarenergy;
      this.data.uvindex = result.data.days[0].uvindex;
      this.data.hours = result.data.days[0].hours;
    } catch (error) {
      console.error(error);
    }
  },
  data() {
    return {
      city: "Criciuma",
      cityName: "Criciúma",
      data: {
        icon: "/icons/cloudy.svg",
        time: "00:00",
        temp: 0,
        description: "-",
        datetime: "10/05/2005",
        precip: 0,
        windspeed: 0,
        cloudcover: 0,
        humidity: 0,
        feelslike: 0,
        snow: 0,
        solarenergy: 0,
        uvindex: 0,
        hours: [],
      },
      weekData: [],
    };
  },
};
</script>

<style scoped>
h1 {
  margin: 0;

  color: var(--w-primary);
  font-size: 60px;
}

.title-box {
  width: 70%;
  display: flex;

  padding: 10px 0;
  margin: 0 auto;
}

.home {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.week-list {
  width: 100%;
  display: flex;
  flex-direction: column;

  gap: 22px;
  padding: 0 0 14px 0;
}
</style>
