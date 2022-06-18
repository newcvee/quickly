import config from "@/config.js";

export async function getCategories() {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/categories`, settings);
  const categories = await response.json();
  return categories;
}
export async function getCategoryById(category_id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/category/${category_id}`, settings);
  const category = await response.json();
  return category;
}

export async function getItem() {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/items`, settings);
  const item = await response.json();
  return item;
}

export async function getItemsByCategory(category_id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(
    `${config.API_PATH}/category/items/${category_id}`,
    settings
  );
  const items = await response.json();
  return items;
}
export async function getItemById(id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/items/${id}`, settings);
  const item = await response.json();
  return item;
}

export async function getOrders() {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/orders`, settings);
  const orders = await response.json();
  return orders;
}

export async function addNewCategory(category) {
  const settings = {
    method: "POST",
    body: JSON.stringify(category),
    headers: {
      Authorization: localStorage.userId,
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/categories`, settings);
}
export async function addNewItem(item) {
  const settings = {
    method: "POST",
    body: JSON.stringify(item),
    headers: {
      Authorization: localStorage.userId,
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/items`, settings);
}

export async function modifyCategory(category, category_id) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(category, category_id),
    headers: {
      Authorization: localStorage.userId,
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/category/${category_id}`, settings);
}




