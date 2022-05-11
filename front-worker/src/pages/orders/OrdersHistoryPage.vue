<template>
<main>
    <table >
      <tr>
          <th>Id</th>
          <th>Description</th>
      </tr>
      <tr v-for="order in orders" :key="order.order_id">
        <td>{{order.order_id}}</td>
        <td>{{order.order_description}}</td>
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

<style>

table, th, td {
  border: 1px solid;
  border-collapse: collapse;
  width: 100vw;
}

</style>