<template>
  <section class="cartPage">
    <div class="goBack" @click="$router.go(-1)">{{back}}</div>
  <div>
    <div class="item" v-for="(item, index) in itemsCart" :key="index">
      <img :src="item.img" />
      <p class="itemInfo">{{ item.name }}</p>
      <p class="itemInfo">{{ item.price }}€</p>
      <button @click="removeItemFromCart(item)">x</button>
    </div>

  <div class="paying-button" @click="makeAnOrder">PAY {{calculateTotalCartPrice()}}</div>
  </div></section>

</template>

<script>
import { sendItemsToCart } from "@/services/cart.js";
import { sendOrder } from "@/services/api.js";
import { v4 as uuidv4 } from "uuid";

export default {
  name: "Cart",
  data() {
    return {
      itemsCart: [],
      back: "< volver",
      order: {
        order_id: "",
        order_number: "",
        order_date: "",
        order_price: 0,
        order_state: "waiting",
        order_items: [],
      },
    };
  },
  mounted() {
    this.CartItems();
    // this.calculateTotalCartPrice();
  },

  methods: {
    calculateTotalCartPrice(){
      let cartPrice = 0;
      for (let item of this.itemsCart){
        cartPrice = cartPrice + item["price"];
      }
      return cartPrice.toFixed(2);
    },
    CartItems() {
      this.itemsCart = sendItemsToCart();
    },
    removeItemFromCart(item){
      this.itemsCart.splice(this.itemsCart.indexOf(item), 1)
    },

      // parseFloat(item["price"])
      // return total.toFixed(2)

    async makeAnOrder(){
      this.order.order_id = uuidv4();
      let number = Math.floor(Math.random() * 100)
      this.order.order_number = number;
      let today = new Date().toLocaleDateString()
      this.order.order_date = today;
      this.order.order_price = this.calculateTotalCartPrice()
      this.order.order_items = this.itemsCart
      await sendOrder(this.order);
      this.itemsCart= []
    },

  },
};
</script>

<style scoped>
.cartPage{
  background-color: rgb(22, 32, 67);
  height: 100vh;
}
.item{
  font-family: "Roboto Mono", monospace;
  font-weight: 900;
  width: 50vw;
  height: 18vh;
  display: flex;
  justify-content: space-between;
  border-radius: 10px 10px 10px 10px;
  margin: auto;
  background: rgb(218, 213, 181);
  border: thick double rgb(22, 32, 67);
  color: rgb(22, 32, 67);
  
}

.paying-button{
  border: 2px solid red;
  position:fixed;
  bottom:5%;
  left:35%;
  font-family: "Roboto Mono", monospace;
  font-size: 2.5rem;
  font-weight: 900;
  border: thick double rgb(22, 32, 67);
  background-color: rgb(109,154,149);
  width: 30vw;
  height: 15vh;
  border-radius: 10px;
  color: rgb(22, 32, 67);
  letter-spacing: 1px;
  padding-top: 10px;
}


.goBack {
  width: 98vw;
  height: 5vh;
  border: 0;
  padding: 0;
  margin: 0;
  color: rgb(218, 213, 181);
  background-color: rgb(22, 32, 67);
}
img {
  width: 30%;
  height: 100%;
  border-radius: 10px 0 0 10px;
}
button{
  font-family: "Roboto Mono", monospace;
  font-weight: 900;
  font-size: 4em;
  color: rgb(255, 255, 255);
  letter-spacing: 1px;
  border-radius:0 10px  10px 0;
  position: relative;
  background-color: rgb(201, 6, 6);
  width: 20%;
  height: 100%;
  margin-left: 5%;
}
.itemInfo{
  margin: auto;
}
</style>
