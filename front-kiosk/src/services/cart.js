
let cartItems = [];

export function AddItemsToCart(item){
    cartItems.push(item);
    console.log(cartItems);
}

export function sendItemsToCart(){
    return cartItems
}
export function countItems(){
    let len= this.cartItemsvar.length;
    return len

}