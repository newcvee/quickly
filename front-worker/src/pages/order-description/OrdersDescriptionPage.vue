<template>
<main>
    <article v-for="order in orders" :key="order.order_id">
    <p>{{order.order_id}}</p>
    <p>{{order.order_description}}</p>
    </article>
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
article {
    border: 1px solid black;
    margin: 0.5em 0.5em 0.5em;
    
}

</style>