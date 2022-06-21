<template>
  <main>
    <section class="changing-states">
      <section class="waitlist-state">
        <h3 class="stateTitle">Waitlist</h3>
        <div class="order" v-for="order in waiting" :key="order.order_id">
          <p>{{ order.order_state }}</p>
          <p>{{ order.order_number }}</p>
          <button @click="stateChangeToDoing(order)">empezar</button>
        </div>
      </section>
      <section class="doing-state">
        <h3 class="stateTitle">Doing</h3>
        <div class="order" v-for="order in doing" :key="order.order_id">
          <p>{{ order.order_state }}</p>
          <p>{{ order.order_number }}</p>
          <button @click="stateChangeToDone(order)">terminar</button>
        </div>
      </section>
    </section>
    <section class="done-state">
      <h3 class="stateTitle">Done</h3>
      <div class="order" v-for="order in done" :key="order.order_id">
        <p>{{ order.order_state }}</p>
        <p>{{ order.order_number }}</p>
      </div>
    </section>
  </main>
</template>

<script>
import { getOrders } from "@/services/api.js";
import { updateOrder } from "@/services/api.js";

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
    setInterval(() => {
      this.loadOrders();
    }, 500);
  },
  methods: {
    async loadOrders() {
      this.orders = await getOrders();
      this.waitListOrder();
      this.doingListOrder();
      this.doneListOrder();
    },
    waitListOrder() {
      this.waiting = this.orders.filter((order) => {
        return order.order_state === "waiting";
      });
    },
    doingListOrder() {
      this.doing = this.orders.filter((order) => {
        return order.order_state === "doing";
      });
    },
    doneListOrder() {
      this.done = this.orders.filter((order) => {
        return order.order_state === "done";
      });
    },
    async stateChangeToDoing(order) {
      order.order_state = "doing";
      let orderId = order.order_id;
      console.log("This is the id", orderId, "and the order", order);
      await updateOrder(order, orderId);
    },
    async stateChangeToDone(order) {
      order.order_state = "done";
      let orderId = order.order_id;
      await updateOrder(order, orderId);
    },
    // let eventId = this.$route.params.id;
    //     await modifyEvent(this.event, eventId);
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
  background-color: rgb(109,154,149);

}
.changing-states {
  display: flex;
  flex-direction: row;
}
.waitlist-state {
  width: 50vw;
  height: 50vh;
  border: 1px solid black;
  overflow-y: scroll;
}
.doing-state {
  width: 50vw;
  height: 50vh;
  border: 1px solid black;
  overflow-y: scroll;
}
.done-state {
  width: auto;
  height: 50vh;
  border: 1px solid black;
  overflow-y: scroll;
}
.order {
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 5%;
  background: rgb(218, 213, 181);
  font-size: 2em;
}
.stateTitle {
  position: sticky;
  top: 0;
  font-weight: 900;
  font-size: 3em
}
button{
  width: 15vh;
  height: 10vh;
  border-radius: 5px;
  background-color:rgb(22, 32, 67);
  font-weight: 900;
  color: rgb(218, 213, 181);
}
p{
  margin:auto;
}
</style>
