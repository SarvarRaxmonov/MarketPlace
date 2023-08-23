from rest_framework import viewsets, status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Category, MainCategory, Product, Review, SavedForLater, Kupon
from .filters import CategoryFilter, ProductFilter
from .serializers import (
    DiscountedCategorySerializer,
    MainCategorySerializer,
    ProductSerializer,
    RelatedProductSerializer,
    ReviewSerializer,
    SavedForLaterSerializer,
    KuponSerializer,
)
from apps.product.permissions import (
    IsReviewAuthorOrReadOnly,
    IsReviewAuthorOrReadOnlyProduct,
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
    permission_classes = [IsReviewAuthorOrReadOnlyProduct]
    lookup_field = "id"


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
    permission_classes = [IsReviewAuthorOrReadOnly]
    lookup_field = "id"

    def list(self, request, id=None):
        obj = self.get_queryset().filter(product=id)
        serializer = self.serializer_class(instance=obj, many=True)
        return Response(serializer.data)

    def create(self, request, id=None):
        obj = self.get_queryset().filter(product=id, user=request.user.id)
        if obj.exists():
            raise ValidationError("you can not create two comments for one product")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavedForLaterViewSet(viewsets.ModelViewSet):
    queryset = SavedForLater.objects.all()
    serializer_class = SavedForLaterSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def list(self, request, id=None):
        obj = self.get_queryset().filter(user=request.user.id)
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KuponListCreateView(generics.ListCreateAPIView):
    queryset = Kupon.objects.all()
    serializer_class = KuponSerializer

    def list(self, request, id=None):
        obj = self.get_queryset().filter(profile__user=request.user)
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KuponRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kupon.objects.all()
    serializer_class = KuponSerializer
