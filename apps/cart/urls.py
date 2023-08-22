from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CheckOrdersViewSet

router = DefaultRouter()


urlpatterns = [
    path(
        "orders/",
        OrderViewSet.as_view({"get": "list", "post": "create"}),
        name="order-list-create",
    ),
    path(
        "orders/<int:pk>/",
        OrderViewSet.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
            }
        ),
        name="order-retrieve-update-destroy",
    ),
    path(
        "check/<int:id>/",
        CheckOrdersViewSet.as_view(
            {
                "get": "get",
            }
        ),
        name="check",
        )
]



