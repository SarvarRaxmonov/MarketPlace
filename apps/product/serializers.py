from django.utils import timezone
from django.db.models import Avg
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    average_discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["main_category", "name", "image", "average_discount_percentage"]

    def get_average_discount_percentage(self, obj):
        average_discount = Category.objects.filter(
            id=obj.id, product__discount_expire_date__gt=timezone.now()
        ).aggregate(average_discount_percentage=Avg("product__discount"))[
            "average_discount_percentage"
        ]
        return f"-{int(average_discount)} %"
