<template>
  <div class="home">
    <button @click="goToCategories">MENU</button>
    <button @click="goToOrders">ORDERS</button>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    goToCategories() {
      this.$router.push("/categories");
    },
    goToOrders() {
      this.$router.push("/orders");
    },
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
button {
  width: 50vw;
  height: 30vh;
  margin: 5%;
}
</style>
