from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.cart.models import Order
from apps.product.models import SavedForLater

@receiver(post_save, sender=Order)
def delete_saved_for_later(sender, instance, **kwargs):
    product_id = instance.product
    try:
        saved_for_later = SavedForLater.objects.get(product=product_id, user=instance.user)
        saved_for_later.delete()
    except SavedForLater.DoesNotExist:
        pass

