<template>
  <div class="home">
    <NavBar />
    <ClimateBanner :data="data" />
    <CardSimpleWeather :data="data" />
    <DayCard v-for="(day, idx) in weekData" :key="idx" :data="day" />
  </div>
</template>

<script>
import CardSimpleWeather from "@/Components/Card/CardSimpleWeather.vue";
import ClimateBanner from "@/Components/ClimateBanner.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";
import DayCard from "@/Components/DayCard/DayCard.vue";
import axios from "axios";
import moment from "moment";

export default {
  name: "HomeView",
  components: {
    NavBar,
    ClimateBanner,
    CardSimpleWeather,
    DayCard,
  },
  async created() {
    try {
      const result = await axios.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Criciuma,BR?unitGroup=metric&lang=pt&key=DLP4WSNVQXB9XBY3A8RWXRZCR",
      );

      // Preenche o array weekData com os 7 primeiros dias
      this.weekData = result.data.days.slice(0, 7).map((day) => ({
        icon: `/icons/${day.icon}.svg`,
        time: moment().format("LT"),
        temp: day.temp,
        description: day.description,
        conditions: day.conditions,
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

      this.data = {
        icon: `/icons/${result.data.days[0].icon}.svg`,
        time: moment().format("LT"),
        temp: result.data.days[0].temp,
        description: result.data.days[0].description,
        conditions: result.data.days[0].conditions,
        datetime: moment(result.data.days[0].datetime).format("DD/MM/YYYY"),
        precip: result.data.days[0].precip,
        windspeed: result.data.days[0].windspeed,
        cloudcover: result.data.days[0].cloudcover,
        humidity: result.data.days[0].humidity,
        feelslike: result.data.days[0].feelslike,
        snow: result.data.days[0].snow,
        solarenergy: result.data.days[0].solarenergy,
        uvindex: result.data.days[0].uvindex,
      };
    } catch (error) {
      console.error(error);
    }
  },
  data() {
    return {
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
      },
      weekData: [], // novo array para os 7 dias
    };
  },
};
</script>

<style scoped>
.home {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
