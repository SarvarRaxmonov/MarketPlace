from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("seller/", include("apps.seller.urls")),
    path("products/", include("apps.product.urls")),
    path("cart/", include("apps.cart.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
