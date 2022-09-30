
const addToCartBtns = document.getElementsByClassName('cart-btn-add')
const removeFromCartBtns = document.getElementsByClassName('cart-btn-remove')
const deleteItemBtns = document.getElementsByClassName('delete-item-btn')

const handleAddToCart = function() {

    const productID = this.getAttribute("data-pid")
    const specificationID = this.getAttribute("data-spec")

    Cart.handleCartItem(productID,specificationID,'A')
    
    const price = document.getElementById('p-'+productID+'?'+specificationID)
    const quantity = parseInt(document.getElementById('q-'+productID+'?'+specificationID).value)
    const totalPrice = document.getElementsByClassName('total-price')
    const currentPrice = parseFloat(price.getAttribute("data-price"))

    document.getElementById('p-'+productID+'?'+specificationID).innerHTML = parseFloat(parseFloat(price.innerHTML) + currentPrice).toFixed(2)
    document.getElementById('q-'+productID+'?'+specificationID).value = quantity + 1

    const newTotalPrice = parseFloat(parseFloat(totalPrice[0].innerHTML) + currentPrice).toFixed(2)
    document.getElementsByClassName('total-price')[0].innerHTML = newTotalPrice
    document.getElementsByClassName('total-price')[1].innerHTML = newTotalPrice
}

const handleRemoveFromCart = function() {
    
    const productID = this.getAttribute("data-pid")
    const specificationID = this.getAttribute("data-spec")

    Cart.handleCartItem(productID,specificationID,'R')

    const price = document.getElementById('p-'+productID+'?'+specificationID)
    const quantity = parseInt(document.getElementById('q-'+productID+'?'+specificationID).value)
    const totalPrice = document.getElementsByClassName('total-price')
    const currentPrice = parseFloat(price.getAttribute("data-price"))

    if (quantity > 1){
        document.getElementById('p-'+productID+'?'+specificationID).innerHTML = parseFloat(parseFloat(price.innerHTML) - currentPrice).toFixed(2)
        document.getElementById('q-'+productID+'?'+specificationID).value = quantity - 1
    } else if (quantity <= 1) {
        
        document.getElementById('r-'+productID+'?'+specificationID).remove()
    }

    const newTotalPrice = parseFloat(parseFloat(totalPrice[0].innerHTML) - currentPrice).toFixed(2)
    document.getElementsByClassName('total-price')[0].innerHTML = newTotalPrice
    document.getElementsByClassName('total-price')[1].innerHTML = newTotalPrice
}

const handleDeleteItem = function() {

    const productID = this.getAttribute("data-pid")
    const specificationID = this.getAttribute("data-spec")

    Cart.removeItemFromCart(productID,specificationID)

    const price = document.getElementById('p-'+productID+'?'+specificationID)
    const quantity = parseInt(document.getElementById('q-'+productID+'?'+specificationID).value)
    const totalPrice = document.getElementsByClassName('total-price')
    const currentPrice = parseFloat(price.getAttribute("data-price"))*parseInt(quantity)

    

    document.getElementById('r-'+productID+'?'+specificationID).remove()

    const newTotalPrice = parseFloat(parseFloat(totalPrice[0].innerHTML) - currentPrice).toFixed(2)
    document.getElementsByClassName('total-price')[0].innerHTML = newTotalPrice
    document.getElementsByClassName('total-price')[1].innerHTML = newTotalPrice

}

for ( let i = 0 ; i < addToCartBtns.length ; i ++ ){

    addToCartBtns[i].addEventListener('click',handleAddToCart)
    removeFromCartBtns[i].addEventListener('click',handleRemoveFromCart)
    deleteItemBtns[i].addEventListener('click', handleDeleteItem)
}