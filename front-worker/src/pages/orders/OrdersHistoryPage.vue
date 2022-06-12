<template>
<main>
    <!-- <p>hello </p>
    <article v-for="order in orders" :key="order.order_id">
    <p>{{order.order_state}}</p>
    <p>{{order.order_id}}</p>
    </article> -->
    <section class="changing-states">
        <section class="waitlist-state"></section>
        <section class="doing-state"></section>
    </section>
    <section class="done-state"></section>
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

<style scoped>
article {
    border: 1px solid black;
    margin: 0.5em 0.5em 0.5em;
}
main{
    width: 100%;
    display: flex;
    flex-direction: column;
}
.changing-states{
    border: 1px solid red;
    display: flex;
    flex-direction: row;
}
.waitlist-state{
    width: 50vw;
    height: 50vh;
    background-color: yellow;
}
.doing-state{
    width: 50vw;
    height: 50vh;
    background-color: blue;
}
.done-state{
    width: auto;
    height: 35vh;
    background-color: red;
}
</style>