<template>
  <div id="nav">
    <router-link to="/">Home</router-link>|
    <router-link to="/categories">Categorias</router-link>|
    <router-link to="/cart">Carrito</router-link>
  </div>
  <router-view />
</template>

<style scoped>
#nav{
  background-color: red;
  height: 1vh;
}
</style>