# Generated by Django 4.0.4 on 2022-08-01 11:36

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, help_text='will be set by default', max_length=200, unique=True, verbose_name='Safe URL')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Category name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_related', to='shop.category', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='white', max_length=50, verbose_name='name')),
                ('RGB', models.CharField(default='#FFFFFF', help_text='code should be unique', max_length=50, unique=True, verbose_name='Hexadecimal color code')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, help_text='will be set by default', max_length=200, unique=True, verbose_name='Safe URL')),
                ('name', models.CharField(help_text='name should be unique', max_length=200, unique=True, verbose_name='Product name')),
                ('inital_price', models.DecimalField(decimal_places=2, default=0.0, help_text='decimal value. max: 99999.99', max_digits=5, verbose_name='Product initial price')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, help_text='optional', max_digits=5, null=True, verbose_name='Product discount price')),
                ('description', models.TextField(verbose_name='description')),
                ('show_in_public', models.BooleanField(default=False, verbose_name='show in public')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_related', to='shop.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=200, verbose_name='specification')),
            ],
            options={
                'verbose_name': 'Product specification',
                'verbose_name_plural': 'Product specifications',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('second_name', models.CharField(blank=True, help_text='optional', max_length=100, null=True, verbose_name='second name')),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('available', models.BooleanField(default=True, verbose_name='in stock')),
                ('color', models.ForeignKey(blank=True, help_text='optional', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.color', verbose_name='color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes_related', to='shop.product', verbose_name='product')),
                ('specifications', models.ManyToManyField(blank=True, help_text='optional', null=True, to='shop.productspecification', verbose_name='specifications')),
            ],
            options={
                'verbose_name': 'Product attribute',
                'verbose_name_plural': 'Product attributes',
            },
        ),
    ]
