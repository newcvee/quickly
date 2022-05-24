import config from "@/config.js"

export async function getOrders() {
  const settings = {
      method: "GET",
      
    };
    const response = await fetch(`${config.API_PATH}/orders`, settings);
    const orders = await response.json();
    return orders;
}
