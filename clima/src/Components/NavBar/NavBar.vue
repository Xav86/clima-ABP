<template>
  <nav class="navbar">
    <div class="navbar__logo">
        <img src="@\assets\icons\logo.png" alt="">
    </div>
    <div class="navright">
        <div class="navbar__search">
            <input
                type="text"
                v-model="searchQuery"
                placeholder="Localizar"
                class="search-input"
            />
            <button @click="handleSave" class="save-button">Salvar</button>
        </div>
        <ul class="navbar__links">
        <li><a href="#">Favoritos</a></li>
        <li><a href="#">Sobre nós</a></li>
        </ul>
        <div class="navbar__settings">
            <img class="gear-icon" src="@/assets/icons/gear.png" alt="Configurações" />
        </div>
    </div>  
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      searchQuery: ''
    }
  },
  methods: {
    handleSave() {
      console.log('Busca salva:', this.searchQuery)
      this.$emit('search', this.searchQuery)
    }
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 24px;
  background-color: #fff;
  border-bottom: 2px solid #e5e7eb;
}

.navbar__logo {
  display: flex;
  align-items: center;
  padding-left: 68px;
}

.navright {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: right;
  padding-right: 68px;
}

.navbar__logo img {
  height: 36px;
  width: auto;
  margin-right: 16px;
}

.navbar__search {
  display: flex;
  align-items: center;
  background: #f6f7fa;
  border-radius: 8px;
  padding: 4px 8px;
  flex: 1;
  max-width: 380px;
  margin: 0 32px;
  border: 1px solid #e5e7eb;
}

.search-input {
  border: none;
  background: transparent;
  padding: 8px 12px;
  font-size: 1rem;
  color: #14213d;
  outline: none;
  flex: 1;
}

.search-input::placeholder {
  color: #b0b3b8;
  font-weight: 600;
}

.save-button {
  background-color: #1E293B99;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 18px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  margin-left: 8px;
  transition: background 0.2s;
}

.save-button:hover {
  background-color: #4b5563;
}

.navbar__links {
  display: flex;
  gap: 24px;
  list-style: none;
  margin: 0 16px 0 0;
  padding: 0;
}

.navbar__links a {
  color: #14213d;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: color 0.2s;
}

.navbar__links a:hover {
  color: #fca311;
}

.navbar__settings {
  cursor: pointer;
  color: #14213d;
  margin-left: 8px;
}
.navbar__settings img {
  width: 24px;
  height: 24px;
}

.gear-icon {
  vertical-align: middle;
}
</style>
