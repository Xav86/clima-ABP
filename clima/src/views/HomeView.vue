<template>
  <div class="home">
    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus esse
      magnam possimus debitis mollitia reiciendis? Inventore voluptatem
      perspiciatis molestiae similique? Modi quas quos iusto reiciendis incidunt
      unde suscipit, vitae distinctio!
    </p>
    <ClimateBanner />
  </div>
</template>

<script>
import ClimateBanner from "@/Components/ClimateBanner.vue";

export default {
  name: "HomeView",
  components: {
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
