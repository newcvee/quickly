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
  font-family: "Roboto Mono", monospace;
  font-size: 2.5rem;
  font-weight: 900;
  color: rgb(22, 32, 67);
  letter-spacing: 1px;
  padding: 13px 50px 13px;
  outline: 0;
  border: thick double rgb(22, 32, 67);
  border-radius: 10px;
  cursor: pointer;
  position: relative;
  background-color: rgb(109,154,149);
  width: 30vw;
  height: 20vh;
}

</style>
