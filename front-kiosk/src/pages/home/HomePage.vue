<template>
  <div class="home">
    <button @click="goToCategories">START ORDER</button>
  </div>
</template>

<script>

export default {
  name: 'Home',
  methods: {
    goToCategories(){
      this.$router.push("/categories")
    }
  }


}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@200&display=swap');
.home{
  background-image: url('https://wallpaperbat.com/img/263325-japanese-pc-wallpaper-top-free-japanese-pc-background.jpg');
  margin: 0;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  font-family: "Roboto Mono", monospace;
}
button{
  margin: 50px;
  font-family: inherit;
  font-size: 20px;
  font-weight: 200;
  color: rgb(22, 32, 67);
  letter-spacing: 1px;
  padding: 13px 50px 13px;
  outline: 0;
  border: 1px solid rgb(22, 32, 67);
  cursor: pointer;
  position: relative;
  background-color: white;
}
button::after{
  content: "";
  background-color: rgb(22, 32, 67);
  width: 100%;
  z-index: -1;
  position: absolute;
  height: 100%;
  top: 7px;
  left: 7px;
}
</style>
