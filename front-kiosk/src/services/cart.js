
let cartItems = [];

export function AddItemsToCart(item){
    cartItems.push(item);
    console.log(cartItems);
}

export function sendItemsToCart(){
    return cartItems
}