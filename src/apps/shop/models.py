from django.db import models
from django.conf import settings 
from ..utils.models import UUIDModel, SlugModel
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField
from .managers import ProductAttributeManager, ProductManager
from django.utils.translation import gettext_lazy as _
USER = settings.AUTH_USER_MODEL




class Category(MPTTModel, SlugModel):
    
    name = models.CharField(
        verbose_name = _('Category name'),
        max_length = 100,
        unique = True,
    )

    parent = TreeForeignKey(
        'self', 
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name="categories_related",
        help_text = _('optional'),
        verbose_name = _('parent category')
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


    def __str__(self):
        return self.name




class Product(SlugModel):

    name = models.CharField(
        max_length= 200,
        verbose_name = _('Product name'),
        help_text = _('name should be unique'),
        unique = True,
    )

    category = models.ForeignKey(
        'category',
        verbose_name= _('category'),
        related_name="products_related",
        on_delete = models.CASCADE
    )

    inital_price = models.DecimalField( 
        verbose_name = _('Product initial price'),
        help_text = _('decimal value. max: 99999.99'),
        max_digits = 5,
        decimal_places = 2,
        default = 0.00
    )

    discount_price = models.DecimalField( 
        verbose_name = _('Product discount price'),
        help_text = _('optional'),
        max_digits = 5,
        decimal_places = 2,
        null = True,
        blank = True,
    )

    description = models.TextField(
        verbose_name= _('description')
    )

    show_in_public = models.BooleanField(
        verbose_name= _('show in public'),
        default = False
    )

    objects = ProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={"slug":self.slug})




class ProductAttribute(UUIDModel):

    product = models.ForeignKey(
        'product',
        verbose_name= _('product'),
        related_name="attributes_related",
        on_delete= models.CASCADE
    )

    color = models.ForeignKey(
        'color',
        verbose_name= _('color'),
        help_text= _('optional'),
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    specifications = models.ManyToManyField(
        'productSpecification',
        verbose_name= _('specifications'),
        help_text= _('optional'),
        null = True,
        blank = True
    )

    second_name = models.CharField(
        max_length=100,
        verbose_name= _('second name'),
        help_text= _('optional'),
        null = True,
        blank = True

    )

    image = CloudinaryField(
        folder ='/'
    )

    available = models.BooleanField(
        verbose_name = _('in stock'),
        default=True,
    )

    objects = ProductAttributeManager()

    class Meta:
        verbose_name = _('Product attribute')
        verbose_name_plural = _('Product attributes')

    def __str__(self):
        return f'{self.product.name} | {self.second_name}'



class ProductSpecification(models.Model):

    specification = models.CharField(
        max_length= 200,
        verbose_name= _('specification')
    )

    class Meta:
        verbose_name = _('Product specification')
        verbose_name_plural = _('Product specifications')

    def __str__(self):
        return f'{self.specification}'


class Color(models.Model):

    name = models.CharField(
        max_length = 50,
        default = 'white',
        verbose_name= _('name')
    )

    RGB = models.CharField(
        verbose_name = 'Hexadecimal color code',
        help_text = _('code should be unique'),
        max_length = 50,
        unique = True,
        default = '#FFFFFF'
    )

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name