<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --w-primary: #121e3d;
  --w-secondary: #6e85c1;
  --w-light-primary: #b7cbff;
  --w-ligth-secondary: #296399;
  --w-cool-white: #f2f2f2;
  --w-white: #fff;
}

.icon {
  width: 35px;
  height: 35px;
}
</style>
