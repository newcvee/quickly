<template>
<section  class="item-container">
    <article class="item" v-for="(item, index) in items" :key="index">
        <p>{{item.img}}</p>
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

        // enterItemDetail(item){            
        //  this.$router.push("/items/" + item.id)
        // },
        AddToCart(item){
            console.log(item)
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
    font-family: Montserrat;
    display: flex;
    flex-direction: row;
    gap: 1em;
    height: fit-content;
    width: 100%;
    grid-auto-rows: 18rem;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 50rem), 1fr));
    margin: 0em 2em 1.5em 1.5em;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;


}
.item-container .item{
    background: rgb(241, 237, 237);
    box-shadow: 0px 0px 8px rgb(184, 181, 181);
    border-radius: 10px;
    font-size: larger;
    display: flex;
    flex-direction: column;
    width: 40%;
    margin: 1em;
}

</style>