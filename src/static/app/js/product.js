const addToCartBtn = document.getElementsByClassName("add-to-cart-btn")[0];




addToCart = function() {

    const productAttributeID = this.getAttribute("data-pid")
    
    try{
        const specification = document.getElementsByClassName('specificationID')[0];
        Cart.handleCartItem(productAttributeID, specification.value ,"A")
    }
    catch{
        Cart.handleCartItem(productAttributeID, '' ,"A")
    }
   

}

addToCartBtn.addEventListener('click',addToCart);


