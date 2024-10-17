from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    writer = AuthorSerializer(many = True, read_only=True)

    class Meta:
        model = Book
        fields = ["name", "writer", "genre", "intro"]

