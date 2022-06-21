<template>
<section class="itemsPage">
<div class="goBack" @click="$router.go(-1)">{{back}}</div>

<button class="button" @click="goToAddItemPage">Add Item</button>
<section class="card" v-for="item in items" :key="item.category_id" >
  <img :src="item.img" />

<p>{{item.name}}</p>
</section></section>
</template>

<script>
import { getItemsByCategory } from "@/services/api.js";
export default {
    name: "Item",
    data(){
        return { 
            items: {},
            back: "< volver",

            };
    },
    mounted() {
        this.loadItems();
    },
    methods: {
        async loadItems() {
            let categoryId = this.$route.params.category_id;
            this.items = await getItemsByCategory(categoryId);
        },

        goToAddItemPage(){
            this.$router.push("/add-item");
        },
    }

}
</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    

}
.itemsPage{
    color: rgb(34, 34, 34);
      background-color: #ebecf0;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: row;
    height: 100vh;
    width: 100vw;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;


}
.itemsPage .card{
    background: rgb(107, 107, 106);
    font-family: "Roboto Mono", monospace;
    border-radius: 10px;
    font-size: 130%;
    font-weight: 900;
    display: flex;
    flex-direction: column;
    width: 40vh;
    height: 40vh;
    margin: 1em;
      color: #babecc;

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
img {
  width: 100%;
  height: 70%;
  border-radius: 10px 10px 0 0;
}

.goBack {
    width: 100vw;
    height: 5vh;
    border: 0;
    padding: 0;
    margin: 0;
    background-color: #ebecf0;
}
.button{
  text-shadow: 1px 1px 1px #fff;

  font-size: 1em;
  align-items: center;
  padding: 2%;
}
</style>