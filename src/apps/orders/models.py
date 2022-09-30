from email.policy import default
from textwrap import indent
from django.db import models
from django.conf import settings 
from ..utils.models import UUIDModel, SlugModel
from ..shop.models import ProductAttribute
from django.utils.translation import gettext_lazy as _
USER = settings.AUTH_USER_MODEL


class Order(UUIDModel):

    ORDER_STATUS = (
        ("P",_("Pending")),
        ("R",_("Rejected")),
        ("D",_("Deliverd"))
    )

    status = models.CharField(
        verbose_name= _('Order status'),
        max_length=1,
        choices=ORDER_STATUS
    )

    items = models.JSONField(
        null = True,
        verbose_name= _('items'),
        blank = True
    )

    total_price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0.00,
        verbose_name= _('total_price'),
        help_text= _('in KWD')
    )

    order_date = models.DateField(
        verbose_name= _('order date'),
        blank = True
    )

    order_time = models.TimeField(
        verbose_name= _('order time'),
        blank = True
    )
    
    completed = models.BooleanField(
        verbose_name= _('Customer completed order')
    )

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ("-order_date",)

    def getItems(self):

        items = []

        for item in self.items:

            items.append({
                "productAttribute" : ProductAttribute.objects.get(id=item['productID']),
                "quantity" : item['quantity'],
                "specification" : item['specificationID']
            })

        return items

    def __str__(self):
        return f'Date: {self.order_date} | Status: {self.status} | Completed: {self.completed}'


class Shipping(models.Model):

    order = models.OneToOneField(
        'order',
        on_delete= models.CASCADE,
        verbose_name= _('order')
    )

    fullname = models.CharField(
        max_length=200,
        verbose_name= _('full name')
    )

    email = models.EmailField(
        unique=False,
        max_length= 100,
        blank= True,
        null=True,
        verbose_name= _('email'),
        help_text= _('optional')
    )

    phone_number = models.CharField(
        max_length= 15,
        null = True,
        verbose_name = _('Phone number'),
        help_text = '+965 ---- ----'
    )

    city = models.CharField(
        max_length= 100,
        verbose_name = _('City')
    )

    street = models.CharField(
        max_length= 100,
        verbose_name = _('Street')
    )

    building = models.CharField(
        max_length= 100,
        verbose_name = _('Building')
    )

    details = models.TextField(
        verbose_name = _('More details')
    )

    class Meta:
        verbose_name = _('Shipping address')
        verbose_name_plural = _('Shipping addresses')