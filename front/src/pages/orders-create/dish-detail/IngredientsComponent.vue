<template>
  <div class="home">
    <h1>{{ ingredients.name }}</h1>
    <section class="counters">
      <Counter
        :initialValue="IngredientCounterPage"
        @value-changed="ingredientsChanged"
      />
    </section>
  </div>
</template>

<script>
import Counter from "./IngredientCounterPage.vue";

export default {
  name: "Ingredients",
  components: { Counter },
  props: {
    contact: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      title: "This is the home page!",
      IngredientCounterPage: "with",
      // ingredients= {}
    };
  },
  // mounted() {
  //   this.loadData()
  //   console.log(this.loadData)
  // },

  computed: {
    animals() {
      return this.cows + this.sheeps;
    },
  },
  methods: {
    ingredientChanged(counterValue) {
      this.cows = counterValue;
    },
    // async loadData() {
    //   this.dish = await getDish();
    // },
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
}
</style>
