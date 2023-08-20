from django.db import models
from .choices import ShippingType, QuantityType
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    shipping_type = models.CharField(max_length=40, choices=ShippingType.choices)

    def __str__(self):
        return self.name


class SendInquiry(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    quantity_type = models.CharField(max_length=40, choices=QuantityType.choices)

    def __str__(self):
        return self.item_name
