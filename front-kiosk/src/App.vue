<template>
  <div id="nav">
    <p @click="goToHome">Home</p>
    <p @click="goToCategories">Categorías</p>
    <p @click="goToCart">Cart</p>
  </div>
  <router-view />
</template>
<script>
export default {
  methods: {
    goToHome() {
      this.$router.push("/");
    },
    goToCategories() {
      this.$router.push("/categories");
    },
    goToCart() {
      this.$router.push("/cart");
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@200&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#nav {
  background-color: rgb(22, 32, 67);
  color: rgb(218, 213, 181);
  margin: 0;
  height: 2vh;
  display: flex;
  justify-content: space-between;
  font-family: "Roboto Mono", monospace;
  font-size: 20px;
  font-weight: 800;
}
</style>
