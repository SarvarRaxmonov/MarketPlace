from rest_framework import viewsets
from .models import Category
from .filters import CategoryFilter
from .serializers import CategorySerializer


class DiscountedCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
