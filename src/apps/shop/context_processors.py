from .cart import Cart 
from .models import Category

def cartProcessor(request):
    return {"cart":Cart(request)}

def categoriesProcessor(request):
    return {'categories':Category.objects.all()}