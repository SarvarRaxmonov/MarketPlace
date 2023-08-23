from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Order, UserKupon
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

    def validate_product(self, value):
        if value.price == 0:
            raise ValidationError(
                "This product is negotiable , please contact to the seller of product"
            )
        return value


class OrderCheckSerializer(serializers.ModelSerializer):
    kupon_code = serializers.CharField()

    class Meta:
        model = Order
        fields = ("kupon_code",)


class UserKuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKupon
        fields = ("id", "user", "kupon", "is_used")
