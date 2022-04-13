<template>
  <div class="home">
    <button @click="goToCategories">START ORDER</button>
  </div>
</template>

<script>

export default {
  name: 'Home',
  mounted() {
    this.loadData()
  },
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
