<template>
  <div>
    <p>"Hello, world!"</p>
    <p>Hi</p>
    <div class="item" v-for="item in itemsCart" :key="item.id">
      <p>{{ item.name }}</p>
      <p>{{ item.price }}</p>

    </div>
  </div>
</template>

<script>
import { sendItemsToCart } from "@/services/cart.js";
export default {
  name: "Cart",
  data() {
    return {
      itemsCart: [],
    };
  },
  mounted() {
    this.CartItems();
  },
  methods: {
    CartItems() {
      this.itemsCart = sendItemsToCart();
      console.log(this.itemsCart);
    },
  },
};
</script>

<style>
.item{
    border: 2px solid red;
}

</style>
