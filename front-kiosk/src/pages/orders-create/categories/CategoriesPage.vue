<template>
    <section class="categories">
        <div class="category-card" v-for="category in categories" :key="category.category_id" @click="enterCategory(category)">
            <p>{{category.name}}</p>
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
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@200&display=swap');

* {
    margin: 1%;
    box-sizing: border-box;
    background-color: rgb(22, 32, 67);
}
.categories {
    display: flex;
    flex-wrap: wrap;
    margin: auto;
    justify-content: space-between;

}
.category-card {
    font-family: "Roboto Mono", monospace;
    font-size: 3rem;
    font-weight: 900;
    width: 30vw;
    height: 50vh;
    background-color: rgb(41, 79, 112) ;
    background-image: url("https://img.pikbest.com/backgrounds/v3/20190612/blue-nostalgic-japanese-wave-background_1403008.jpg!bw700");
    background-repeat: no-repeat;
    background-size: auto;
    border: thick double rgb(22, 32, 67);
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;

}


.category-card > p{
    /* border: 5px solid rgb(22, 32, 67); */
    border: thick double rgb(22, 32, 67);
    border-radius: 2%;
    background-color: rgb(218, 213, 181) ;
    color: rgb(41, 79, 112);
    width: 20vw;
    height: 20vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>