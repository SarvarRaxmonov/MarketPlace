from django.db import models
from django.contrib.auth.models import User
from apps.product.models import Product
from apps.product.models import Kupon


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.product.name}"


class UserKupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kupon = models.ForeignKey(Kupon, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
