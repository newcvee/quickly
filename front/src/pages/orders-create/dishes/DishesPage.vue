<template>
<p>hellouuu</p>
<section class="card" v-for="dish in dishes" :key="dish.category_id">
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
        
    }

}
</script>

<style>
.card {
    border: 1px solid;
}

</style>