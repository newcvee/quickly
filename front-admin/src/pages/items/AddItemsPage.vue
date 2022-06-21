<template>
  <main>
    <div class="goBack" @click="$router.go(-1)">{{back}}</div>
    <h1>New Item</h1>
    <form>
      <label for="category-name">What category is your item from:</label>
      <input type="text" v-model="item.category_id"> 

      <label for="item-name">Item name:</label>
      <input type="text" v-model="item.name">

      <label for="item-price">Item price:</label>
      <input type="text" v-model="item.price">

      <button @click.prevent="addNewItemForm">Submit</button>
    </form>
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
        img: "hi",
        price: "",
      },
      back: "< volver",

    }
  },
  methods: {
    isValidItemForm() {
      if (
        this.item.category_id === "" ||
        this.item.name === "" ||
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
      this.$router.push("/categories");
    },
  }

}
</script>

<style scoped>
/* form{
  display: flex;
  flex-direction: column;
}
button{
  width: 10%;
} */
/* ruler: 16px;
color-red: #AE1100;
#EBECF0: #EBECF0;
color-shadow: #BABECC;
#FFF: #FFF; */

main {
  background-color: #ebecf0;
  margin: 0;
  padding: 0;
  min-height: 100vh;
}

main,
p,
input,
select,
text,
button {
  font-family: "Montserrat", sans-serif;
  letter-spacing: -0.2px;
  font-size: 16px;
}

div,
p {
  color: #babecc;
  text-shadow: 1px 1px 1px #fff;
}

form {
  padding: 16px;
  width: 16px * 20;
  margin: 0 auto;
}

button,
input {
  border: 0;
  outline: 0;
  font-size: 16px;
  border-radius: 16px * 20;
  padding: 16px;
  background-color: #ebecf0;
  text-shadow: 1px 1px 0 #fff;
}

label {
  display: block;
  margin-bottom: 16px * 1.5;
  width: 100%;
}

input {
  margin-right: 16px/2;
  box-shadow: inset 2px 2px 5px #babecc, inset -5px -5px 10px #fff;
  width: 100%;
  box-sizing: border-box;
  transition: all 0.2s ease-in-out;
  appearance: none;
  -webkit-appearance: none;
}

input:focus {
  box-shadow: inset 1px 1px 2px #babecc, inset -1px -1px 2px #fff;
}

button {
  color: #61677c;
  font-weight: bold;
  box-shadow: -5px -5px 20px #fff, 5px 5px 20px #babecc;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  font-weight: 600;
}

button:hover {
  box-shadow: -2px -2px 5px #fff, 2px 2px 5px #babecc;
}

button:active {
  box-shadow: inset 1px 1px 2px #babecc, inset -1px -1px 2px #fff;
}


button .unit {
  border-radius: 16px/2;
  line-height: 0;
  width: 16px * 3;
  height: 16px * 3;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 16px/2;
  font-size: 16px * 1.2;
}

button .icon {
  margin-right: 0;
}
button .red {
  display: block;
  width: 100%;
  color: #ae1100;
}

.input-group {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
label {
  margin: 0;
  flex: 1;
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
