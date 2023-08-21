import django_filters
from django.db.models import Avg, F, Count, Sum
from django.utils import timezone
from apps.product.models import Category


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = [
            "name",
        ]

    @property
    def qs(self):
        parent = super().qs
        most_discounted_categories = (
            parent.filter(product__discount_expire_date__gt=timezone.now())
            .annotate(product_discount_count=Sum("product__discount"))
            .order_by("-product_discount_count")[:5]
        )

        print("---------------------------------------------------------------- \n")
        for category in most_discounted_categories:
            print(
                f"Category: {category.name}, Product Discount Count: {category.product_discount_count}"
            )
        print("\n ---------------------------------------------------------------- \n")
        return most_discounted_categories
