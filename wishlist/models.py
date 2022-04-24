from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} from {self.user}'s wishlist"
