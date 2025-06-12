<template>
  <div class="home">
    <NavBar />
    <ClimateBanner />
  </div>
</template>

<script>
import ClimateBanner from "@/Components/ClimateBanner.vue";
import NavBar from "@/Components/NavBar/NavBar.vue";

export default {
  name: "HomeView",
  components: {
    NavBar,
    ClimateBanner,
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
