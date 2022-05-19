<template>
<p>hellouuu</p>
<button @click="goToAddDishPage">Add Dish</button>
<section class="card" v-for="dish in dishes" :key="dish.category_id" @click="enterDishDetail(dish)" >
<p>{{dish.img}}</p>
<p>{{dish.name}}</p>
</section>
</template>

<script>
import { getDishesByCategory } from "@/services/api.js";
export default {
    name: "Dish",
    data(){
        return { 
            dishes: {},
            };
    },
    mounted() {
        this.loadDishes();
    },
    methods: {
        async loadDishes() {
            let categoryId = this.$route.params.category_id;
            this.dishes = await getDishesByCategory(categoryId);
        },
        enterDishDetail(dish){            
         this.$router.push("/dishes/" + dish.id)
        },
        goToAddDishPage(){
            this.$router.push("/add-dish");
        },
    }

}
</script>

<style>
.card {
    border: 1px solid;
}

</style>