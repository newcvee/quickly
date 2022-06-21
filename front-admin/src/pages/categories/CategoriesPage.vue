<template>
  <section class="categoriesPage">
    <div class="goBack" @click="$router.go(-1)">{{ back }}</div>
    <button @click="goToAddCategoryPage">Add Category</button>
    <br />
    <section
      class="card"
      v-for="category in categories"
      :key="category.category_id"
    >
      <article class="category-card" @click="enterCategory(category)">
        <p>{{ category.name }}</p>
      </article>
    </section>
  </section>
</template>

<script>
import { getCategories } from "@/services/api.js";
export default {
  name: "Categories",
  data() {
    return {
      back: "< volver",
      categories: {},
    };
  },
  mounted() {
    this.loadCategories();
  },
  methods: {
    async loadCategories() {
      this.categories = await getCategories();
    },

    enterCategory(category) {
      this.$router.push("/category/items/" + category.category_id);
    },
    goToAddCategoryPage() {
      this.$router.push("/add-category");
    },
  },
};
</script>

<style scoped>
.categoriesPage {
  height: 100%;
  width: 100%;
  background-color: #ebecf0;
  margin: 0;
  padding: 0;
  font-family: "Montserrat", sans-serif;
  font-weight: 600;
  text-shadow: 1px 1px 0 #fff;
}

.card {
  display: flex;
  flex-direction: column;
  background-color: #ebecf0;
}

.category-card {
  width: 30vw;
  height: 30vh;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 1%;
  margin-top: 1%;
  border-radius: 10px;
  border: 0;
  box-shadow: -5px -5px 20px #cfd2e1, 5px 5px 20px #9396a2;
}

p {
  text-shadow: 1px 1px 1px #fff;
  margin-top: 20%;
  margin-bottom: 0;
  font-size: 2em;
  padding: 0;
  height: 20%;
}
button {
  width: 15vw;
  height: 10vh;
  background-color: #babecc;
  box-shadow: -5px -5px 20px #cfd2e1, 5px 5px 20px #23252b;

  color: #2c3e50;

  border-radius: 10px;
  font-weight: 900;
  margin-bottom: 1%;
}
.goBack {
  width: 98vw;
  height: 5vh;
  border: 0;
  padding: 0;
  margin-bottom: 1%;

  color: #2c3e50;
}
</style>
