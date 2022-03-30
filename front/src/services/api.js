// import config from "@/config.js";

// export async function getDish(id) {
//     const settings = {
//       method: "GET",
//       headers: {
//         Authorization: getUserId(),
//       },
//     };
//     const response = await fetch(`${config.API_PATH}/contacts/${id}`, settings);
//     return await response.json();
// }




// export async function getDish(id) {
// const settings = {
//     method: "GET",
    
// };
// const response = await fetch(`${config.APºI_PATH}/dishes/${id}`, settings);
// console.log(response)
// return await response.json();
// }



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
    const response = await fetch(`${config.API_PATH}/dishes/1`, settings);
    const dish = await response.json();
    return dish;
}
export async function getIngredientByDish() {
    const settings = {
      method: "GET",
      
    };
    const response = await fetch(`${config.API_PATH}/dish/ingredients/1`, settings);
    const ingredients = await response.json();
    return ingredients;
}
  