<template>
  <main>
    <h1>New Item</h1>
    <form>
      <label for="category-name">What category is your item from:</label>
      <input type="text" v-model="item.category_id"> 

      <label for="category-name">Item id:</label>
      <input type="text" v-model="item.id">

      <label for="category-name">Name:</label>
      <input type="text" v-model="item.name">

      <label for="category-image">Image:</label>
      <input type="text" v-model="item.img">

      <label for="category-image">Price:</label>
      <input type="text" v-model="item.price">

      <button @click.prevent="addNewItemForm">Submit</button>
    </form>
    {{$data}}
  </main>
</template>

<script>
import { addNewItem } from "@/services/api.js";

export default {
  name: "add-item",
  data(){
    return{
      item: {
        category_id: "",
        id: "",
        name: "",
        img: "",
        price: "",
      }
    }
  },
  methods: {
    isValidItemForm() {
      if (
        this.item.category_id === "" ||
        this.item.id === "" ||
        this.item.name === "" ||
        this.item.img === "" ||
        this.item.price === "" 
      ) {
        return false;
      } else {
        return true;
      }
    },
    async addNewItemForm() {
      if (!this.isValidItemForm()) {
        alert("No empty spaces");
        return;
      }
      await addNewItem(this.item);
      alert("Item added");
      console.log("item added");
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