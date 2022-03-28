<template>
  <div>
    
    <section class="counters">
      <Counter
        :initialValue="IngredientCounterPage"
        @value-changed="ingredientsChanged"
      />
    </section>
    <h1>{{ ingredients }}</h1>
  </div>
</template>

<script>

import Counter from "./IngredientCounterPage.vue";

export default {
  name: "Ingredients",
  components: { Counter },
  props: {
    ingredients: {
      type: String,
      required: true,
    },
    
  },
  data() {
    return {
      title: "This is the home page!",
      IngredientCounterPage: "with",
      
    };
  },
  

  computed: {
    animals() {
      return this.cows + this.sheeps;
    },
  },
  methods: {
    ingredientChanged(counterValue) {
      this.cows = counterValue;
    },
    
  },
  
};

  
</script>

<style scoped>
h1 {
  font-style: italic;
}
.counters {
  display: flex;
  gap: 1em;
  width: 10px;
  padding: 0%;
}
</style>
