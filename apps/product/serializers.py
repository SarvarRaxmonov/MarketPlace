from django.db.models import Avg
from rest_framework import serializers
from .models import (
    Category,
    MainCategory,
    Product,
    Review,
    WholeSale,
    Feature,
    Image,
    SavedForLater,
)
from apps.cart.models import Order
from django.utils import timezone
from apps.seller.serializers import ProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    lowest_price = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "main_category", "name", "image", "lowest_price")

    def get_lowest_price(self, obj):
        obj = Product.objects.filter(category=obj.id).order_by("price").first()
        return f"{obj.price} {obj.currency}"


class MainCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = MainCategory
        fields = ("id", "name", "image", "is_prime", "categories")


class DiscountedCategorySerializer(serializers.ModelSerializer):
    average_discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "main_category", "name", "image", "average_discount_percentage")

    def get_average_discount_percentage(self, obj):
        average_discount = Category.objects.filter(
            id=obj.id, product__discount_expire_date__gt=timezone.now()
        ).aggregate(average_discount_percentage=Avg("product__discount"))[
            "average_discount_percentage"
        ]
        return f"-{int(average_discount)} %"


class WholeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholeSale
        fields = ("id", "count_from", "count_to", "price")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image")


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("id", "name", "description")


class ProductSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    orders_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField(read_only=True, default=0)
    wholesale = WholeSaleSerializer(many=True)
    features = FeatureSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "profile",
            "name",
            "average_rate",
            "price",
            "tax",
            "orders_count",
            "reviews_count",
            "discount_price",
            "currency",
            "discount",
            "discount_expire_date",
            "brand",
            "condition",
            "is_recommended",
            "is_shipping_paid",
            "is_available",
            "description",
            "wholesale",
            "category",
            "tag",
            "images",
            "features",
            "created_at",
            "updated_at",
        )

    def get_orders_count(self, obj):
        count = Order.objects.filter(product=obj.id, is_paid=True).count()
        return count



    def get_reviews_count(self, obj):
        return Review.objects.filter(product=obj.id).count() or 0


class RelatedProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "images", "name", "price", "discount_price", "currency")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user", "product", "text", "rate", "created_at", "updated_at")


class SavedForLaterSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()

    class Meta:
        model = SavedForLater
        fields = ("user", "product", "product_detail")
        extra_kwargs = {
            "product": {
                "write_only": True,
            }
        }

    def get_product_detail(self, obj):
        instance = Product.objects.get(id=obj.product.id)
        serializer = RelatedProductSerializer(instance)
        return serializer.data

