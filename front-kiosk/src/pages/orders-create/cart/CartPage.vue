<template>
  <div>
    <p>"Hello, world!"</p>
    <p>Hi</p>
    <div class="item" v-for="(item, index) in itemsCart" :key="index">
      <p>{{ item.name }}</p>
      <p>{{ item.price }}</p>
      <button @click="removeItemFromCart(item)">Remove from cart</button>

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
    removeItemFromCart(item){
      this.itemsCart.splice(this.itemsCart.indexOf(item), 1)},
  },
};
</script>

<style>
.item{
    border: 2px solid red;
}

</style>
