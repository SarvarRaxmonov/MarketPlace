from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    DiscountedCategoryViewSet,
    MainCategoryViewSet,
    ProductViewSet,
    RelatedProductsViewSet,
    ReviewViewSet,
    SavedForLaterViewSet,
    KuponListCreateView,
    KuponRetrieveUpdateDestroyView,
    PersonalizedRecommendationViewSet,
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
        ProductViewSet.as_view({"get": "list", "post": "create"}),
        name="products",
    ),
    path(
        "products/<int:id>",
        ProductViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
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
    path(
        "saved-for-later-products/",
        SavedForLaterViewSet.as_view({"get": "list", "post": "create"}),
        name="saved-for-later-products",
    ),
    path(
        "saved-for-later-product/<int:pk>",
        SavedForLaterViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="saved-for-later-retrieve-destroy",
    ),
    path("kupons/", KuponListCreateView.as_view(), name="kupon-list-create"),
    path(
        "kupons/<int:pk>/",
        KuponRetrieveUpdateDestroyView.as_view(),
        name="kupon-retrieve-update-destroy",
    ),
    path(
        "you-may-like/",
        PersonalizedRecommendationViewSet.as_view({"get": "list"}),
        name="you-may-like",
    ),
]
