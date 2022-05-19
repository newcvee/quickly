<template>
  <main>
    <h1>New Dish</h1>
    <form>
      <label for="category-name">What category is your dish from:</label>
      <input type="text" v-model="dish.category_id"> 

      <label for="category-name">Dish id:</label>
      <input type="text" v-model="dish.id">

      <label for="category-name">Name:</label>
      <input type="text" v-model="dish.name">

      <label for="category-image">Image:</label>
      <input type="text" v-model="dish.image">

      <label for="category-image">Price:</label>
      <input type="text" v-model="dish.price">

      <button @click.prevent="addNewDishForm">Submit</button>
    </form>
    {{$data}}
  </main>
</template>

<script>
import { addNewDish } from "@/services/api.js";

export default {
  name: "add-dish",
  data(){
    return{
      dish: {
        category_id: "",
        id: "",
        name: "",
        image: "",
        price: "",
      }
    }
  },
  methods: {
    isValidDishForm() {
      if (
        this.dish.category_id === "" ||
        this.dish.id === "" ||
        this.dish.name === "" ||
        this.dish.image === "" ||
        this.dish.price === "" 
      ) {
        return false;
      } else {
        return true;
      }
    },
    async addNewDishForm() {
      if (!this.isValidDishForm()) {
        alert("No empty spaces");
        return;
      }
      await addNewDish(this.dish);
      alert("Dish added");
      console.log("dish added");
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