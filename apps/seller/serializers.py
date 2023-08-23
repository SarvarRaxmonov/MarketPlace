from rest_framework import serializers
from .models import Profile, Country, SendInquiry


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class ProfileSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Profile
        fields = (
            "user",
            "name",
            "description",
            "country",
            "is_verified",
            "shipping_type",
        )


class SendInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = SendInquiry
        fields = ("id", "item_name", "description", "quantity", "quantity_type")
