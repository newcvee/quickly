import config from "@/config.js"

export async function getOrders() {
  const settings = {
      method: "GET",
      
    };
    const response = await fetch(`${config.API_PATH}/orders`, settings);
    const orders = await response.json();
    return orders;
}

export async function updateOrder(order, order_id){
  const settings = {
    method: "PUT",
    body: JSON.stringify(order, order_id),
    headers: {
      "Content-Type": "application/json"
    },
  };
  await fetch(`${config.API_PATH}/order/${order_id}`, settings);
}

