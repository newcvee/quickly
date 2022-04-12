<template>
  <div class="home">
    <button @click="goToCategories">START ORDER</button>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/info')
      this.info = await response.json()
    },
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
