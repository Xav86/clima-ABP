<template>
  <div id="app">
    <SideBar />
    <!-- o resto da sua aplicação -->
  </div>
</template>

<script>
import SideBar from './Components/SideBar.vue'

export default {
  name: 'App',
  components: {
    SideBar
  }
}
</script>
