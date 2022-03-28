<template>
<ul>
    <li>{{dish.name}}</li>
    <li>{{dish.img}}</li>
</ul>
<Ingredients />
  
</template>

<script>
import { getDish } from "@/services/api.js";
import Ingredients from "./IngredientCounterPage.vue"


export default {
  name: "DishDetail",
  components: { Ingredients},
  data() {
    return {
      dish: {},
    };
  },
  mounted() {
    this.loadData()
    console.log(this.loadData)
  },
  methods: {
    async loadData() {
      this.dish = await getDish();
    },
  },

}
</script>

<style>

</style>