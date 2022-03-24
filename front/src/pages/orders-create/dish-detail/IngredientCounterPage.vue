<template>
  <section class="counter">
    <section class="buttons">
      <button @click="onMinusClicked">-</button>
      <h2>{{ counter }}</h2>
      <button @click="onAddClicked">+</button>
    </section>
  </section>
</template>

<script>
export default {
  name: "Counter",
  props: {
    initialValue: { type: String, default: "with" },
  },
  data() {
    return {
      counter: this.initialValue,
    };
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
  },
};
</script>

<style scoped>
.counter {
  border: 1px solid #abc;
  padding: 1em;
  max-width: 6em;
  font-size: 3em;
}
.counter .buttons {
  display: flex;
  width: 100%;
  justify-content: space-between;
}
.counter button {
  font-size: 1em;
  padding: 0 1em;
}
</style>
