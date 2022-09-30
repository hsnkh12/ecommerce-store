from django.contrib import admin
from .models import Order, Shipping
# Register your models here.


class ShippingInline(admin.TabularInline):
    model = Shipping

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ShippingInline]
    search_fields = ('id','order_date', 'status', 'completed', 'address__phone_number','address__fullname','address__email')