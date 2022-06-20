<template>
<div class="goBack" @click="$router.go(-1)">{{back}}</div>
<section  class="item-container">
    <article class="item" v-for="(item, index) in items" :key="index">
        <!-- <p>{{item.img}}</p> -->
        <img :src="item.img" />
        <p>{{item.name}}</p>
        <button @click="AddToCart(item)">Add to cart</button>
    </article>
</section>
</template>

<script>
import { getItemsByCategory } from "@/services/api.js";
import { AddItemsToCart } from "@/services/cart.js";

export default {
    name: "Items",
    data(){
        return { 
            items: [],
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
        AddToCart(item){
            AddItemsToCart(item)
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
.item-container{
    color: rgb(34, 34, 34);
    background-color: rgb(22, 32, 67);
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
.item-container .item{
    background: rgb(241, 237, 237);
    box-shadow: 0px 0px 8px rgb(184, 181, 181);
    border-radius: 10px;
    font-size: 1.5em;
    display: flex;
    flex-direction: column;
    width: 40vh;
    height: 20vh;
    margin: 1em;
}
button{
  margin: 50px;
  font-family: "Roboto Mono", monospace;
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