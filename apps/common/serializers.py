from rest_framework import serializers
from .models import EmailSubscribe, Article


class EmailSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscribe
        fields = ("email",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "image",
            "is_prime",
            "description",
            "created_at",
            "updated_at",
        )
