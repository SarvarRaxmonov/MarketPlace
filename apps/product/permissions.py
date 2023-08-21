from rest_framework import permissions
from apps.product.models import Review


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CanCreateOneReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.POST:
            print(
                id,
                "................................................................",
                request.data,
            )
            existing_reviews = Review.objects.filter(
                user=request.user, product=request.data.get("product")
            )
            return not existing_reviews.exists()
        return True
