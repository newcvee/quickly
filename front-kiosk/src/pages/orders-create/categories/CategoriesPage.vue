<template>
    <p>hello there</p>
    <section class="card" v-for="category in categories" :key="category.category_id">
        <h1>{{category.name}}</h1>
        <div class="card" v-for="item in filteredItems" :key="item.id" >
            <p>{{item.img}}</p>
            <p>{{item.name}}</p>
            <p>hey</p>
            <button>Add to cart</button>
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
            items: [],
            filteredItems: [],
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
        
        // enterCategory(category){            
        //  this.$router.push("/category/items/" + category.category_id)
        // }
        filterItems(){
            this.filteredItems= this.items.filter(this.item.category_id === this.category.category_id);
            console.log(this.filteredItems)
        }
   

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