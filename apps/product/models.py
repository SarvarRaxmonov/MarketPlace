from django.db import models
from django.db.models import Avg
from django.utils import timezone
from ckeditor.fields import RichTextField
from .choices import Condition, Currency
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from apps.seller.models import Profile
from .managers import ProductManager


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="main_category_images/")
    is_prime = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(
        MainCategory, on_delete=models.DO_NOTHING, related_name="categories"
    )
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
    count_from = models.BigIntegerField(default=0)
    count_to = models.BigIntegerField(default=0)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.id}"


class Image(models.Model):
    image = models.FileField(upload_to="images/")

    def __str__(self):
        return f"{self.image}"


class Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product"
    )
    price = models.BigIntegerField(default=0)
    tax = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=40, choices=Currency.choices)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    discount_expire_date = models.DateTimeField()
    wholesale = models.ManyToManyField(
        WholeSale, blank=True, related_name="product_wholesale"
    )
    images = models.ManyToManyField(Image)
    tag = models.ManyToManyField(Tag)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)
    condition = models.CharField(max_length=40, choices=Condition.choices)
    is_available = models.BooleanField(default=True)
    is_recommended = models.BooleanField()
    is_shipping_paid = models.BooleanField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        return self.name

    def average_rate(self):
        return self.review_product.aggregate(avg_rate=Avg("rate"))["avg_rate"] or 0

    def discount_price(self):
        if self.discount > 0 and self.discount_expire_date > timezone.now():
            price = self.price
            discount_price = (self.discount / 100) * price
            return int(discount_price)
        return 0


class Kupon(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code = models.CharField(max_length=300)
    kupon_discount = models.IntegerField(validators=[MaxValueValidator(100)])
    expire_date = models.DateTimeField()


class SavedForLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="review_product"
    )
    text = models.TextField()
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rate})"
