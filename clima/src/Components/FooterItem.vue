<template>
  <div class="footer-item">
    <div class="footer-c">
      <img
        class="opacity-80"
        src="@\assets\icons\icon _telescope.svg"
        alt="logo_icon"
      />
      <span class="opacity-80">©2025 Clima Delivery</span>
    </div>
    <span>Feito com Vue e muito &#x1F499;</span>
  </div>
</template>

<style scoped>
.footer-item {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  gap: 4px;
  padding: 10px 0;

  border-top: 1px solid #bebebe;
  background-color: #f6f8fa;
}

.footer-c {
  display: flex;
}

.opacity-80 {
  opacity: 80%;
}
</style>
