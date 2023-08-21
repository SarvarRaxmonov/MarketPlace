from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    DiscountedCategoryViewSet,
    MainCategoryViewSet,
    ProductViewSet,
    RelatedProductsViewSet,
    ReviewViewSet,
)

router = DefaultRouter()


urlpatterns = [
    path(
        "discounted_categories/",
        DiscountedCategoryViewSet.as_view({"get": "list"}),
        name="discounted_categories",
    ),
    path(
        "main_categories/",
        MainCategoryViewSet.as_view({"get": "list"}),
        name="main_categories",
    ),
    path(
        "products/",
        ProductViewSet.as_view({"get": "list"}),
        name="products",
    ),
    path(
        "products/<int:id>",
        ProductViewSet.as_view({"get": "retrieve"}),
        name="products",
    ),
    path(
        "related_products/<str:tag_name>",
        RelatedProductsViewSet.as_view({"get": "list"}),
        name="related_products",
    ),
    path(
        "review_product/<int:id>",
        ReviewViewSet.as_view({"get": "list", "post": "create"}),
        name="review_products",
    ),
    path(
        "review_detail/<int:id>",
        ReviewViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="review_products",
    ),
]
