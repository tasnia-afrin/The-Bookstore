from rest_framework import serializers
from .models import Blog
from authors.serializers import AuthorSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["blog", "author", "created_at"]
