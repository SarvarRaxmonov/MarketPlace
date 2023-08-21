from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscountedCategoryViewSet

router = DefaultRouter()


urlpatterns = [
    path(
        "discounted_categories/",
        DiscountedCategoryViewSet.as_view({"get": "list"}),
        name="discounted_categories",
    ),
]
