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
  --primary: #121e3d;
  --secondary: #6e85c1;
  --cool-white: #f2f2f2;
  --white: #fff;
}

.icon {
  width: 35px;
  height: 35px;
}
</style>
