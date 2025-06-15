<template>
  <div class="home">
    <NavBar />
    <ClimateBanner :data="data" />
  </div>
</template>

<script>
import ClimateBanner from "@/Components/ClimateBanner.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    NavBar,
    ClimateBanner,
  },
  async created() {
    try {
      const result = await axios.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Criciuma,BR?key=DLP4WSNVQXB9XBY3A8RWXRZCR",
      );

      this.data.temp = parseFloat(
        (((result.data.days[0].temp - 32) * 5) / 9).toFixed(1),
      );
    } catch (error) {
      console.error(error);
    }
  },
  data() {
    return {
      data: {
        temp: 0,
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
