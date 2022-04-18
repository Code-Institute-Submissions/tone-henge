import uuid
from django.db import models
from django.db.models import Sum
from products.models import Product


class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_id = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_id(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_id}'
