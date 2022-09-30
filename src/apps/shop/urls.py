from django.urls import path
from .views import IndexView, ProductsListView, ProductDetailView, CartItemsListView, CartItemAddRemoveView



app_name = 'shop'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('products/', ProductsListView.as_view(),name='products'),
    path('products/<slug>/', ProductDetailView.as_view(),name= 'product'),
    path('cart/', CartItemsListView.as_view(),name='cart'),
    path('cart/<productID>/', CartItemAddRemoveView.as_view(),name='add-to-cart')
]