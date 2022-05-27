<template>
    <section class="category-card" v-for="category in categories" :key="category.category_id" @click="enterCategory(category)">
        <h1>{{category.name}}</h1>
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
.card {
    margin: 1%;
    }

.category-card {
    border: 1px solid black;
    margin-left: auto;
    margin-right: auto;
}

</style>