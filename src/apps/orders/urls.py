from django.urls import path
from .views import ShippingView, OrderOverView, OrderCompletedView, TemplateView


app_name = 'orders'

urlpatterns = [

    path('checkout/', ShippingView.as_view(), name='checkout'),
    path('order-overview/<orderID>/', OrderOverView, name='order-overview'),
    path('order-completed/', OrderCompletedView.as_view(), name='order-completed')
]