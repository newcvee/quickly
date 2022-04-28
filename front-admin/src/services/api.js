import config from "@/config.js"


export async function getCategories() {
  const settings = {
    method: "GET",
    
  };
  const response = await fetch(`${config.API_PATH}/categories`, settings);
  const categories = await response.json();
  return categories;
}

export async function getDish() {
  const settings = {
      method: "GET",
      
    };
    const response = await fetch(`${config.API_PATH}/dishes`, settings);
    const dish = await response.json();
    return dish;
}

export async function getDishesByCategory(category_id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/category/dishes/${category_id}`, settings);
  const dishes = await response.json();
  return dishes;
}
export async function getDishById(id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/dishes/${id}`, settings);
  const dish = await response.json();
  return dish;
}
  