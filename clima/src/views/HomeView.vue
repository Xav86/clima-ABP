<template>
  <div class="home">
    <NavBar />
    <ClimateBanner :data="data" />
    <CardSimpleWeather :data="data" />
  </div>
</template>

<script>
import CardSimpleWeather from "@/Components/Card/CardSimpleWeather.vue";
import ClimateBanner from "@/Components/ClimateBanner.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";
import axios from "axios";
import moment from "moment";

export default {
  name: "HomeView",
  components: {
    NavBar,
    ClimateBanner,
    CardSimpleWeather,
  },
  async created() {
    try {
      const result = await axios.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Criciuma,BR?unitGroup=metric&lang=pt&key=DLP4WSNVQXB9XBY3A8RWXRZCR",
      );

      this.data.icon = `/icons/${result.data.days[0].icon}.svg`;
      this.data.time = moment().format("LT");
      this.data.temp = result.data.days[0].temp;
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
