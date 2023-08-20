from django.db import models


class Condition(models.TextChoices):
    REFURBISHED = "refurbished", "Refurbished"
    BRAND_NEW = "brand_new", "Brand New"
    OLD_ITEMS = "old_items", "Old Items"


class Currency(models.TextChoices):
    USD = "USD", "US Dollar"
    EUR = "EUR", "Euro"
    GBP = "GBP", "British Pound"
