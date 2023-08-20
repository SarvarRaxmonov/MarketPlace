from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from .choices import Condition, Currency
from django.contrib.auth.models import User


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="main_category_images/")
    is_prime = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="category_images/")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.name


class WholeSale(models.Model):
    price_from = models.BigIntegerField(default=0)
    price_to = models.BigIntegerField(default=0)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}"


class Image(models.Model):
    image = models.FileField(upload_to="images/")

    def __str__(self):
        return self.image


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=40, choices=Currency.choices)
    discount = models.PositiveIntegerField()
    discount_expire_date = models.DateTimeField()
    wholesale = models.ManyToManyField(WholeSale)
    images = models.ManyToManyField(Image)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)
    condition = models.CharField(max_length=40, choices=Condition.choices)
    is_recommended = models.BooleanField()
    is_shipping_paid = models.BooleanField()
    description = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SavedForLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rate})"
