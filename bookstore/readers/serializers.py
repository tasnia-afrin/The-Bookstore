from rest_framework import serializers
from .models import Reader
from users.serializers import UserSerializer


class ReaderSerializer(serializers.ModelSerializer):
    reader = UserSerializer

    class Meta:
        model = Reader
        fields = ["reader", "intro"]
