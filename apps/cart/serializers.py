from rest_framework import serializers
from .models import Order
from apps.product.serializers import RelatedProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = RelatedProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "user", "product", "quantity", "is_paid")


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "product", "quantity")
