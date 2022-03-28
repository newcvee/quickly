<template>
<ul>
    <li class="name">{{dish.name}}</li>
    <li>{{dish.img}}</li>
</ul>
<Ingredients class="ingredients"  v-for="ingredient in ingredients" :key="ingredient.name" />
  
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
li{
  list-style: none;
}
.name{
  font-size: 5em;
}
.ingredients{
  width: 10px;
  padding: 0%;
}

</style>