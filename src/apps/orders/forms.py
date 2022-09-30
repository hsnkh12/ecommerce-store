from django.forms import ModelForm
from .models import Shipping


class ShippingForm(ModelForm):

    class Meta:
        model = Shipping
        fields = ['fullname','email','phone_number','city','street','building','details']


