import django_filters
from django.db.models import Sum
from django.utils import timezone
from apps.product.models import Category, Product


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ("name",)

    @property
    def qs(self):
        parent = super().qs
        most_discounted_categories = (
            parent.filter(product__discount_expire_date__gt=timezone.now())
            .annotate(product_discount_count=Sum("product__discount"))
            .order_by("-product_discount_count")[:5]
        )
        return most_discounted_categories


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    category = django_filters.CharFilter(
        field_name="category__name", lookup_expr="contains"
    )
    brand = django_filters.CharFilter(field_name="brand__name", lookup_expr="contains")
    features = django_filters.CharFilter(
        field_name="features__name", lookup_expr="contains"
    )
    condition = django_filters.CharFilter(
        field_name="condition", lookup_expr="contains"
    )
    verified_only = django_filters.BooleanFilter(
        field_name="profile__is_verified", lookup_expr="exact"
    )
    rate = django_filters.NumberFilter(method="custom_rate_filter")
    price_range = django_filters.RangeFilter(field_name="price")

    class Meta:
        model = Product
        fields = ("name", "brand", "category", "condition")

    def custom_rate_filter(self, queryset, name, value):
        return Product.objects.filter_average_rated_products(rate_value=value)
