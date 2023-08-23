from rest_framework import viewsets
from .models import EmailSubscribe, Article
from .serializers import EmailSubscribeSerializer, ArticleSerializer


class EmailSubscribeViewSet(viewsets.ModelViewSet):
    queryset = EmailSubscribe.objects.all()
    serializer_class = EmailSubscribeSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
