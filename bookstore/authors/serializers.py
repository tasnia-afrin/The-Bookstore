from rest_framework import serializers
from .models import Author
from books.models import Book
from books.book_services import BookServices
from users.serializers import UserSerializer
from blog.blog_services import BlogServices
from mainapp.choices import VIEW_PERMISSION_CHOICES


class AuthorSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = "__all__"


class AuthorBookListCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    genre = serializers.CharField(allow_blank=True)
    intro = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        name = validated_data.get("name")
        genre = validated_data.get("genre")
        intro = validated_data.get("intro")
        user = self.context["request"].user

        try:
            writer =  Author.objects.get(author=user)
            BookServices.create_book(
                self=self, name=name, writer=writer, genre=genre, intro=intro
            )

        except Author.DoesNotExist:
            print("Author does not exist")

        return validated_data


class AuthorBlogListCreateSerializer(serializers.Serializer):
    blog = serializers.CharField()
    view_permission = serializers.ChoiceField(
        choices=VIEW_PERMISSION_CHOICES, allow_blank=False
    )

    def create(self, validated_data):
        blog = validated_data.get("blog")
        view_permission = validated_data.get("view_permission")
        user = self.context["request"].user

        try:

            author:Author = Author.objects.get(author=user)
            BlogServices.create_blog(
                self=self, author=author, blog=blog, view_permission=view_permission
            )

        except Author.DoesNotExist:
            print("Author does not exist")

        return validated_data
