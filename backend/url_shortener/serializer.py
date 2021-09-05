from url_shortener.models import CustomURL
from rest_framework import serializers

from url_shortener.models import CustomURL


class CustomURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomURL
        fields = [
            "id",
            "short_url",
            "long_url",
        ]


class CustomURLCreateSerializer(CustomURLSerializer):
    class Meta:
        model = CustomURL
        fields = [
            "unique_id",
            "short_url",
            "long_url",
        ]
