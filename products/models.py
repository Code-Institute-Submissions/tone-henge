from tabnanny import verbose
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(
        'Category', related_name='products', null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(blank=True)
