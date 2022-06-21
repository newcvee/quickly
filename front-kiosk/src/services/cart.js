
let cartItems = [];

export function AddItemsToCart(item){
    cartItems.push(item);
}

export function sendItemsToCart(){
    return cartItems
}
export function countItems(){
    let cartLength = cartItems.length;
    return cartLength
}