from django.urls import path
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    SendInquiryViewSet,
)

urlpatterns = [
    path("list/", ProfileListCreateView.as_view(), name="profile-list-create"),
    path(
        "profile/<int:pk>/",
        ProfileRetrieveUpdateDestroyView.as_view(),
        name="profile-retrieve-update-destroy",
    ),
    path(
        "send_inquiry/",
        SendInquiryViewSet.as_view({"get": "list", "post": "create"}),
        name="send_inquiry",
    ),
]
