from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, UserKupon
from .serializers import (
    OrderSerializer,
    OrderCreateSerializer,
    UserKuponSerializer,
    OrderCheckSerializer,
)
from .utils import calculate_check, calculate_kupon_price
from rest_framework.decorators import action


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def list(self, request, id=None):
        obj = self.get_queryset().filter(user__id=request.user.id, is_paid=False)
        serializer = OrderSerializer(obj, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["delete"],
        url_path="delete_all_cart_items/(?P<user_id>[^/.]+)",
    )
    def delete_item(self, request, user_id=None):
        if user_id is None:
            return Response(
                {"error": "user_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        items_deleted = self.get_queryset().filter(user=user_id, is_paid=False).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCheckSerializer

    def get(self, request, id=None):
        obj = self.get_queryset()
        data = calculate_check(instance=obj, kupon_price=0)
        return Response(data)

    def create(self, request, id=None):
        obj = self.get_queryset()
        kupon = calculate_kupon_price(
            kupon_code=request.data["kupon_code"], user_id=request.user.id
        )
        data = calculate_check(instance=obj, kupon_price=kupon)
        return Response(data)

    def get_queryset(self):
        id = self.kwargs.get("id")
        return Order.objects.filter(
            is_paid=False, user__id=id, product__is_available=True
        )


class UserKuponViewSet(viewsets.ModelViewSet):
    queryset = UserKupon.objects.all()
    serializer_class = UserKuponSerializer
