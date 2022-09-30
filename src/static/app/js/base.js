function getCsrfToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCsrfToken('csrftoken');

const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
});


getValueById = (id) => {
    try{
        return parseFloat(document.getElementById(id).innerHTML).toFixed(2)
    } catch {
        return undefined;
    }
}

setHtmlElementByIdTo = (elementID, value) => {
    document.getElementById(elementID).innerHTML = value;
}


class Cart{
    
    static url = '/cart/'


    static handleCartItem = async function(productAttributeID, specificationID, action){

        const requestObject = {
            method : "POST",
                headers : {
                    "Content-type":"application/json",
                    "X-CSRFToken" : csrftoken
                },
                body:JSON.stringify({
                    "action": action,
                    "specificationID": specificationID
                })
        }

        try {
            await fetch(Cart.url+productAttributeID+'/', requestObject)

            Cart.#handleCartCount(action)

        } catch(err) {
            console.error(err);
        }

        

    }

    static removeItemFromCart = async function(productAttributeID, specificationID){

        const requestObject = {
            method : "DELETE",
                headers : {
                    "Content-type":"application/json",
                    "X-CSRFToken" : csrftoken
                },
                body:JSON.stringify({
                    "specificationID": specificationID
                })
        }

        try {
            await fetch(Cart.url+productAttributeID+'/', requestObject)

        } catch(err) {
            console.error(err);
        }
        
    }

    static #handleCartCount = function(action){

        const cartCount = parseInt(document.getElementsByClassName("cart-count")[0].innerHTML);

        document.getElementsByClassName("cart-count")[0].innerHTML = action == 'A' ? cartCount+1 : cartCount-1

    }


    static emptyCart = async function(){

        const requestObject = {
            method : "DELETE",
                headers : {
                    "Content-type":"application/json",
                    "X-CSRFToken" : csrftoken
                }
        }

        try {
            await fetch(Cart.url, requestObject)
            window.location.reload();

        } catch(err) {
            console.error(err);
        }
        
    }
}