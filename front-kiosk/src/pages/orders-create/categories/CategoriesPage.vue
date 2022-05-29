<template>
    <section class="categories">
        <div class="category-card" v-for="category in categories" :key="category.category_id" @click="enterCategory(category)">
            <h1>{{category.name}}</h1>
            <p>{{category.image}}</p>
        </div>
    </section>
</template>

<script>
import { getCategories, getItems } from "@/services/api.js";
export default {
    name: "Categories",
    data(){
        return { 
            categories: {},
            };
    },
    mounted() {
        this.loadCategories();
        this.loadItems();

        
    },
    methods: {
        async loadCategories() {
            this.categories = await getCategories();
        },
        
        async loadItems() {
            this.items = await getItems();
            // console.log(this.items)
        },
        
        enterCategory(category){            
         this.$router.push("/category/items/" + category.category_id)
        },
    }
}
</script>

<style scoped>
* {
    margin: 1%;
}
.categories {
    display: flex;
    flex-wrap: wrap;
    margin: auto;

}
.category-card {
    border: 1px solid black ;
    width: 30vw;
    height: 30vh;
 
}

</style>