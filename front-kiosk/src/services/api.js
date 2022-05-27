import config from "@/config.js"


export async function getCategories() {
  const settings = {
    method: "GET",
    
  };
  const response = await fetch(`${config.API_PATH}/categories`, settings);
  const categories = await response.json();
  return categories;
}

export async function getItems() {
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
  const response = await fetch(`${config.API_PATH}/category/items/${category_id}`, settings);
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
  