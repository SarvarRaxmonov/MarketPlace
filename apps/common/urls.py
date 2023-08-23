from django.urls import path
from .views import EmailSubscribeViewSet, ArticleViewSet

urlpatterns = [
    path(
        "email_subscribe/",
        EmailSubscribeViewSet.as_view({"get": "list", "post": "create"}),
        name="email_subscribe",
    ),
    path("articles/", ArticleViewSet.as_view({"get": "list"}), name="articles"),
]
