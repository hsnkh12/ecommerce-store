from .models import ProductAttribute, ProductSpecification

class Cart():
    

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart_session')

        if not cart:
            cart = self.session['cart_session'] = {}

        self.cart = cart

    
    def add(self, productID, specificationID):

        #productID = str(productID)
        itemID = str(productID) + '?' + str(specificationID)

        if itemID not in self.cart:
            self.cart[itemID] = {"quantity":1, "specificationID":specificationID}

        else:
            self.cart[itemID]["quantity"] += 1

        self.session.modified = True

    def remove(self, productID, specificationID):
        
        itemID = str(productID) + '?' + str(specificationID)
        item = self.cart[itemID]

        if item["quantity"] <= 1:
            del self.cart[itemID]
        else:
            self.cart[itemID]["quantity"] -= 1

        self.session.modified = True

    def delete(self, productID, specificationID):

        itemID = str(productID) + '?' + str(specificationID)
        del self.session['cart_session'][itemID]
        self.session.modified = True


    def removeAll(self):
        
        del self.session['cart_session']

        self.session.modified = True
    
    def __len__(self):
        return sum( item['quantity'] for item in self.cart.values() )

    def data(self):
        
        data = {}
        
        cart_session = self.session.get('cart_session')
        data = { "items": [], "total_price": 0}

        for key,value in cart_session.items():
            
            try:
                productAttribute = ProductAttribute.objects.select_related('product').get(id = key[0:key.index('?')], available = True)
                
            except:
                del self.session['cart_session'][key]
                self.session.modified = True
                break

            try:
                specification = ProductSpecification.objects.get(id = value['specificationID'])
            except:
                specification = -1
            
            
            data["items"].append({ 
                "productAttribute": productAttribute,
                "quantity": value["quantity"],
                "specification": specification
            })

            initial_price = productAttribute.product.inital_price
            discount_price = productAttribute.product.discount_price

            data["total_price"]+= (discount_price if discount_price else initial_price)*value["quantity"]
        
        return data
    
    def items(self):

        items = []

        for item in self.data()['items']:

            try:
                specification = item['specification'].specification
            except:
                specification = None
            
            items.append({
                "productID" : str(item['productAttribute'].id),
                "quantity" : item['quantity'],
                "specificationID" : specification
            })
        print(items)
        return items
    

    def number_of_items(self):
        return len([ item for item in self.cart.values()])