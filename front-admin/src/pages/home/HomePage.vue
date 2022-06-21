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

.home {
  background-color: #ebecf0;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

button {
  font-family: "Montserrat", sans-serif;
  letter-spacing: -0.2px;
  font-size: 16px;
  border: 0;
  outline: 0;
  font-size: 16px;
  border-radius: 16px * 20;
  padding: 16px;
  background-color: #ebecf0;
  text-shadow: 1px 1px 0 #fff;
  width: 80vw;
  height: 40vh;
  margin: auto;

}
p {
  color: #babecc;
  text-shadow: 1px 1px 1px #fff;
}



button {
  color: #61677c;
  font-weight: bold;
  box-shadow: -5px -5px 20px #b9bcc9, 5px 5px 20px #9396a2;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  font-weight: 600;
}
</style>
