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
h1 {
  font-style: italic;
}
</style>
