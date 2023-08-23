from apps.cart.models import Order
from apps.product.models import Kupon
from django.utils import timezone
from django.db.models import Sum, F, ExpressionWrapper, DecimalField


def calculate_products_total_discount_price(instance: Order):
    total_discount_price = sum(
        order.product.discount_price() * order.quantity
        for order in instance
        if order.product.discount_expire_date > timezone.now()
    )
    return total_discount_price


def calculate_check(instance: Order, kupon_price: int):
    if instance.exists():
        order_data = instance.aggregate(
            subtotal=Sum(
                ExpressionWrapper(
                    F("product__price") * F("quantity"), output_field=DecimalField()
                )
            ),
            tax=Sum(
                ExpressionWrapper(
                    F("product__tax") * F("quantity"), output_field=DecimalField()
                )
            ),
        )

        discount = calculate_products_total_discount_price(instance)

        total = (
            order_data["subtotal"]
            - int(discount)
            - int(kupon_price)
            + order_data["tax"]
        )

        data = {
            "check": {
                "subtotal": order_data["subtotal"],
                "tax": order_data["tax"],
                "discount": discount,
                "kupon": kupon_price,
                "total": total,
            }
        }

        return data
    return "You have not any orders"


def calculate_kupon_price(kupon_code: str, user_id: int):
    try:
        obj = Kupon.objects.get(code=kupon_code, expire_date__gte=timezone.now())
        checking = Order.objects.filter(user=user_id, product=obj.product)
        if checking.exists():
            price = obj.product.price
            kupon_price = (obj.kupon_discount / 100) * price
            return kupon_price
        return 0
    except Kupon.DoesNotExist:
        return 0
