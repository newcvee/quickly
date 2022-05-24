<template>
  <main>
    <h1>New Category</h1>
    <form>
      <label for="category-name">Give the new category a name:</label>
      <input type="text" v-model="category.category_id">
      <label for="category-name">Give it a name:</label>
      <input type="text" v-model="category.name">
      <label for="category-image">Now, an image:</label>
      <input type="text" v-model="category.image">
      <button @click.prevent="addNewCategoryForm">Submit</button>
    </form>
    {{$data}}
  </main>
</template>

<script>
import { addNewCategory } from "@/services/api.js";

export default {
  name: "add-category",
  data(){
    return{
      category: {
        category_id: "",
        name: "",
        image: "",
      }
    }
  },
  methods: {
    isValidCategoryForm() {
      if (
        this.category.category_id === "" ||
        this.category.name === "" ||
        this.category.image === "" 
      ) {
        return false;
      } else {
        return true;
      }
    },
    async addNewCategoryForm() {
      if (!this.isValidCategoryForm()) {
        alert("No empty spaces");
        return;
      }
      await addNewCategory(this.category);
      alert("Category added");
      console.log("category added");
      // this.$router.push("/categories");
    },
  }

}
</script>

<style>
form{
  display: flex;
  flex-direction: column;
}
button{
  width: 10%;
}

</style>