<template>
  <main>

    <section class="changing-states">
      <section class="waitlist-state">
        <div v-for="order in waiting" :key="order.order_id">
          <p>{{ order.order_state }}</p>
          <p>{{ order.order_number }}</p>
        </div>
      </section>
      <section class="doing-state">
          <div v-for="order in doing" :key="order.order_id">
            <p>{{ order.order_state }}</p>
            <p>{{ order.order_number }}</p>
          </div>
        </section>
      
    </section>
    <section class="done-state">
        <div v-for="order in done" :key="order.order_id">
            <p>{{ order.order_state }}</p>
            <p>{{ order.order_number }}</p>
        </div>
    </section>
    {{ $data }}
  </main>
  <button @click="waitListOrder">go</button>
</template>

<script>
import { getOrders } from "@/services/api.js";

export default {
  name: "Order",
  data() {
    return {
      orders: [],
      waiting: [],
      doing: [],
      done: [],
    };
  },
  mounted() {
    this.loadOrders()
  },
  methods: {
    async loadOrders() {
      this.orders = await getOrders()
      this.waitListOrder()
      this.doingListOrder()
      this.doneListOrder()

    },
    waitListOrder() {
      console.log("waitListOrder", this.orders);
      this.waiting = this.orders.filter((order) => {
        console.log(order.order_state);
        return order.order_state === "waiting";
      });
    },
    doingListOrder(){
        this.doing = this.orders.filter((order) => {
        console.log(order.order_state);
        return order.order_state === "doing";
      });
    },
    doneListOrder(){
        this.done = this.orders.filter((order) => {
        console.log(order.order_state);
        return order.order_state === "done";
      });
    }
  },
};
</script>

<style scoped>
article {
  border: 1px solid black;
  margin: 0.5em 0.5em 0.5em;
}
main {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.changing-states {
  border: 1px solid red;
  display: flex;
  flex-direction: row;
}
.waitlist-state {
  width: 50vw;
  height: 50vh;
  background-color: yellow;
}
.doing-state {
  width: 50vw;
  height: 50vh;
  background-color: blue;
}
.done-state {
  width: auto;
  height: 35vh;
  background-color: red;
}
</style>
