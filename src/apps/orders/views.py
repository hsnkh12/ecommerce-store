from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from ..shop.cart import Cart
from .forms import ShippingForm
from datetime import datetime
from django.contrib import messages
from .models import Order

class ShippingView(FormView):

    form_class = ShippingForm
    template_name = 'orders/checkout.html'


    def form_valid(self, form):

        cart = Cart(self.request)

        if cart.__len__() == 0:
            messages.error(self.request, "Order is not valid!")
            return redirect('shop:cart')

        order = Order(
            order_date = datetime.now().date(),
            order_time = datetime.now().time(),
            items = cart.items(),
            total_price = cart.data()['total_price'],
            completed = True,
            status = 'P' 
        )

        order.save()

        form.instance.order = order
        form.save()

        cart.removeAll()

        orderURL = f'/'
        message = f'My Order: {orderURL}'
        phone_number = ''

        return redirect(f'https://wa.me/+{phone_number}/?text={message}')


class OrderCompletedView(TemplateView):

    template_name = 'orders/order_completed.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCompletedView, self).get_context_data(**kwargs)

        context['order'] = self.get_queryset()
        return context

    def get_queryset(self):
        orderID = self.request.GET.get('orderID')
        order = Order.objects.get(pk=orderID)
        return order if order.completed else None


def OrderOverView(request, orderID):

    order = Order.objects.get(id=orderID)
    personal = {
        'name' : order.shipping.fullname,
        'email': order.shipping.email,
        'phone_number': order.shipping.phone_number
    }
    address = order.shipping


    overview = {
        'id': order.id,
        'items': order.getItems(),
        'total_price' : order.total_price
    }
    return render(request,'orders/order_overview.html', {'personal': personal, 'address': address, 'overview': overview})

    