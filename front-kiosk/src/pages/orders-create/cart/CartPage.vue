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
  <div class="paying-button" @click="makeAnOrder">PAY</div>
  {{$data}}
</template>

<script>
import { sendItemsToCart } from "@/services/cart.js";
import { v4 as uuidv4 } from "uuid";

export default {
  name: "Cart",
  data() {
    return {
      itemsCart: [],
      order: {
        order_id: "",
        order_date: "",
        order_price: "",
        order_state: "waiting",
        order_description: "",
      },
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
      this.itemsCart.splice(this.itemsCart.indexOf(item), 1)
    },
  
    makeAnOrder(){
      this.order.order_id = uuidv4();
      let today = new Date().toLocaleDateString()
      this.order.order_date = today;
      this.order.order_description = this.itemsCart

    },
  },
};
</script>

<style>
.item{
  border: 2px solid blue;
}

.paying-button{
  border: 2px solid red;
  position:fixed;
  bottom:5%;
  left:49%;
}

</style>
