<template>
<main>
    <div class="goBack" @click="$router.go(-1)">{{back}}</div>
    <table >
      <tr>
          <th>Id</th>
          <th>Date</th>
      </tr>
      <tr v-for="order in orders" :key="order.order_id">
        <td>{{order.order_id}}</td>
        <td>{{order.order_date}}</td>
      </tr>
    </table>
</main>
  
</template>

<script>
import { getOrders } from "@/services/api.js";

export default {
    name: "Order",
    data(){
        return{
            orders: {},
            back: "< volver",

        };
    },
    mounted() {
        this.loadOrders();
    },
    methods: {
        async loadOrders() {
            this.orders = await getOrders();
            console.log("Orders loaded", this.orders)
        }
    }

}
</script>


<style scoped>
table, th, td {
  border: 1px solid;
  border-collapse: collapse;
  width: 100vw;
}


main {
  background-color: #ebecf0;
  margin: 0;
  padding: 0;
  min-height: 100vh;
}

button {
  font-family: "Montserrat", sans-serif;
  letter-spacing: -0.2px;
  font-size: 16px;
}


p {
  color: #babecc;
  text-shadow: 1px 1px 1px #fff;
}




td {
  border: 0;
  outline: 0;
  font-size: 16px;
  border-radius: 16px * 20;
  padding: 16px;
  background-color: #ebecf0;
  text-shadow: 1px 1px 0 #fff;
box-shadow: inset 2px 2px 5px #babecc, inset -5px -5px 10px #fff;
}




tr {
  color: #61677c;
  font-weight: bold;
  box-shadow: -5px -5px 20px #fff, 5px 5px 20px #babecc;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  font-weight: 600;
}



</style>


