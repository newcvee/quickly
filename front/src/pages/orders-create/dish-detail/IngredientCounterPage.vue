<template>
  <div>
    <h1>{{dish.name}}hey</h1>
    <!-- <img alt="foto" :src="dish.img" /> -->
    <p>{{dish.img}}</p>
  </div>
  <section class="counter" v-for="ingredient in ingredients" :key="ingredient.dish_id">
    <section class="buttons" >
      <button @click="onMinusClicked">-</button>
      <h2>{{ counter }}</h2>
      <button @click="onAddClicked">+</button>
    </section>
    <p class="ingredient">{{ingredient.name}}</p>
  </section>
  <button>Añande al carrito</button>
  {{$data}}
</template>

<script>
import { getDishById } from "@/services/api.js";
import { getIngredientByDish } from "@/services/api.js";

export default {
  name: "Counter",
  data() {
    return {
      counter: "with" ,
      dish: {},
      ingredients: {}
    };
  },
  mounted() {
    this.loadData()
    this.loadIngredients()
  },
  methods: {
    onAddClicked() {
      if(this.counter === "with"){
        this.counter = "extra" 
        this.$emit("value-changed", this.counter)
      }
      if(this.counter === "without"){
        this.counter = "with" 
        this.$emit("value-changed", this.counter)
      }
      
     
    },
    onMinusClicked() {
      if(this.counter=== "with"){
        this.counter= "without"
        this.$emit("value-changed", this.counter)
      }
      if(this.counter=== "extra"){
        this.counter= "with"
        this.$emit("value-changed", this.counter)
      }
      
    },
    async loadData() {
      let DishId = this.$route.params.id;
      this.dish = await getDishById(DishId);
    },
    async loadIngredients() {
      this.ingredients = await getIngredientByDish();
      
    },
    CounterValue(){
      let InitialValue= "with"
      console.log(InitialValue)
    }

  },
};
</script>

<style scoped>
.counter {
  padding: 0px;
  width: fit-content;
  font-size: 3em;
  display:flex;
  flex-direction:row;
  justify-content: space-between;
}
.ingredient {
  font-size:0.3em;
  float:left;
  margin: 50px;
}
.counter .buttons {
  display: flex;
  flex-direction:row;
  
  width: 1em;
  height: 1em;
 
  font-size: 1em;
  margin: 10px;
}
h2{
  padding: 10px;
  font-size: 0.3em;
}
.counter .button {
  display: flex;
  width: 10px;
}

</style>
