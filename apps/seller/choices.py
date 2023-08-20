from django.db import models


class ShippingType(models.TextChoices):
    WORLDWIDE = "worldwide", "Worldwide"
    LOCAL = "local", "Local"


class QuantityType(models.TextChoices):
    KG = "kg", "Kilograms"
    PCS = "pcs", "Pieces"
    LITR = "litr", "Liters"
