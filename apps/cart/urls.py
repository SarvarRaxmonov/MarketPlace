from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CheckOrdersViewSet, UserKuponViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "orders/",
        OrderViewSet.as_view({"get": "list", "post": "create"}),
        name="order-list-create",
    ),
    path(
        "orders/<int:pk>/",
        OrderViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}),
        name="order-retrieve-update-destroy",
    ),
    path(
        "check/<int:id>/",
        CheckOrdersViewSet.as_view({"get": "get", "post": "create"}),
        name="check",
    ),
    path("user_kupon/", UserKuponViewSet.as_view({"post": "create"})),
]
