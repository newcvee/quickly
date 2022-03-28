<template>
<ul>
    <li>{{dish.name}}</li>
    <li>{{dish.img}}</li>
</ul>
<Ingredients v-for="ingredient in ingredients" :key="ingredient.dish_id" :ingredient="ingredient"/>
  
</template>

<script>
import { getDish } from "@/services/api.js";
import { getIngredientByDish } from "@/services/api.js";
import Ingredients from "./IngredientCounterPage.vue"


export default {
  name: "DishDetail",
  components: { Ingredients},
  data() {
    return {
      dish: {},
      ingredients: {}
    };
  },
  mounted() {
    this.loadData()
    this.loadIngredients()
    
  },
  methods: {
    async loadData() {
      this.dish = await getDish();
    },
    async loadIngredients() {
      this.ingredients = await getIngredientByDish();
      
    },
  },

}
</script>

<style>

</style>