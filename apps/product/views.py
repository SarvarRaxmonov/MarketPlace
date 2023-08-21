from rest_framework import viewsets
from rest_framework.response import Response
from apps.product.permissions import IsReviewAuthorOrReadOnly, CanCreateOneReview
from .models import Category, MainCategory, Product, Review
from .filters import CategoryFilter, ProductFilter
from .serializers import (
    DiscountedCategorySerializer,
    MainCategorySerializer,
    ProductSerializer,
    RelatedProductSerializer,
    ReviewSerializer,
)


class DiscountedCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = DiscountedCategorySerializer
    filterset_class = CategoryFilter


class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class RelatedProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = RelatedProductSerializer

    def list(self, request, tag_name=None):
        obj = self.get_queryset().filter(tag__name=tag_name)[:6]
        serializer = self.serializer_class(instance=obj, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly, CanCreateOneReview]

    def list(self, request, id=None):
        obj = self.get_queryset().filter(product=id)
        serializer = self.serializer_class(instance=obj, many=True)
        return Response(serializer.data)
