<template>
  <aside class="sidebar">
    <nav>
      <ul>
        <li><img src="@/assets/icons/location.png" alt="Localização" /></li>
        <li><img src="@/assets/icons/calendar.png" alt="Calendário" /></li>
        <li><img src="@/assets/icons/sun.png" alt="Tempo" class="active" /></li>
        <li><img src="@/assets/icons/book.png" alt="Livro" /></li>
        <li><img src="@/assets/icons/ball.png" alt="Pokébola" /></li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: 'SideBar'
}
</script>

<style scoped>
.sidebar {
  width: 72px;
  background-color: #f5f7fb;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1rem 0;
  box-shadow: 2px 0 6px rgba(0, 0, 0, 0.05);
  /* border-radius: 0 24px 24px 0; */
  height: 100vh;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin: 5.4rem 0;
  cursor: pointer;
}

img {
  width: 28px;
  height: 28px;
  opacity: 0.6;
  transition: opacity 0.3s;
}

img.active,
li:hover img {
  opacity: 1;
}
</style>
