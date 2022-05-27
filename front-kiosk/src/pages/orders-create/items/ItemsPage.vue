<template>
<p>hellouuu</p>
<section class="card" v-for="item in items" :key="item.category_id" >
<p>{{item.img}}</p>
<p>{{item.name}}</p>
<button @click="AddToCart(item)">Add to cart</button>
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
.card {
    border: 1px solid;
}

</style>