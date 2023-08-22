from django.urls import path
from .views import ProfileListCreateView, ProfileRetrieveUpdateDestroyView

urlpatterns = [
    path("/list", ProfileListCreateView.as_view(), name="profile-list-create"),
    path(
        "profile/<int:pk>/",
        ProfileRetrieveUpdateDestroyView.as_view(),
        name="profile-retrieve-update-destroy",
    ),
]

