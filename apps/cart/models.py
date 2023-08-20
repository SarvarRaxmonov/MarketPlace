from django.db import models
from django.contrib.auth.models import User
from apps.product.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.product.name}"


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"
