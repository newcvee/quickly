<template>
  <div>
    <h1>{{item.name}}</h1>
    <!-- <img alt="foto" :src="dish.img" /> -->
  
    <p>{{item.img}}</p>
  </div>

  <button>Añande al carrito</button>
  {{$data}}
</template>

<script>
import { getItemById } from "@/services/api.js";

export default {
  name: "Counter",
  data() {
    return {
      item: {},
    };
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      let ItemId = this.$route.params.id;
      this.item = await getItemById(ItemId);
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
