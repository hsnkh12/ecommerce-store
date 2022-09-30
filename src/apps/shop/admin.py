from django.contrib import admin
from .models import Category, ProductAttribute, Product, ProductSpecification, Color
from mptt.admin import MPTTModelAdmin
# Register your models here.



class SearchAdminProductAttr(admin.ModelAdmin):
    search_fields = ('id','second_name')

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]
    search_fields = ('name', 'category')

admin.site.register(Category,MPTTModelAdmin)
admin.site.register(ProductAttribute,SearchAdminProductAttr)
admin.site.register(ProductSpecification)
admin.site.register(Color)