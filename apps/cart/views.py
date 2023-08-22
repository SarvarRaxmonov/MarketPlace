from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def list(self, request, id=None):
        obj = self.get_queryset().filter(user__id=request.user.id, is_paid=False)
        serializer = OrderSerializer(obj, many=True)
        return Response(serializer.data)


class CheckOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def get(self, request, id=None):
        obj = self.get_queryset()
        subtotal = obj.filter(is_paid=False, user__id=id).aggregate(
            subtotal_price=Sum("product__price")
        )["subtotal_price"]
        discount = obj.filter(
            is_paid=False,
            user__id=id,
            product__discount_expire_date__gte=timezone.now(),
        ).aggregate(discount_price=Sum("product__discount"))["discount_price"]
        tax = obj.filter(is_paid=False, user__id=id).aggregate(
            tax_price=Sum("product__tax")
        )["tax_price"]
        discount_price = (discount / 100) * subtotal
        total = (int(subtotal) - int(discount_price)) + tax
        return Response(
            {
                "check": {
                    "subtotal": subtotal,
                    "discount": discount_price,
                    "tax": tax,
                    "total": total,
                }
            }
        )
