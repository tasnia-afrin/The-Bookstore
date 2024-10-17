from django.http import HttpResponseNotFound
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied, NotFound

from .serializers import (
    AuthorSerializer,
    AuthorBookListCreateSerializer,
    AuthorBlogListCreateSerializer,
)
from .models import Author
from books.models import Book
from blog.models import Blog
from mainapp.models import CustomUser
from mainapp.permissions import AuthorWritePermission


class AuthorProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [AuthorWritePermission]
    serializer_class = AuthorSerializer

    def get_object(self):
        user: CustomUser = self.request.user

        if user.user_type != "author":
            raise PermissionDenied(
                detail="You do not have permission to access this profile."
            )

        try:
            return Author.objects.get(author=user)
        except Author.DoesNotExist:
            raise NotFound(detail="Author profile not found.")


class AuthorListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()


class AuthorBookListCreateView(generics.ListCreateAPIView):
    permission_classes = [AuthorWritePermission]
    serializer_class = AuthorBookListCreateSerializer

    def get_queryset(self):
        user: CustomUser = self.request.user

        if user.user_type != "author":
            raise PermissionDenied(
                detail="You do not have permission to access this profile."
            )

        try:
            writer: Author = Author.objects.get(author=user)
            return Book.objects.filter(writer=writer)
        except Author.DoesNotExist:
            raise NotFound("Author does not exist.")


class AuthorBlogListCreateView(generics.ListCreateAPIView):
    permission_classes = [AuthorWritePermission]
    serializer_class = AuthorBlogListCreateSerializer

    def get_queryset(self):
        user: CustomUser = self.request.user

        if user.user_type != "author":
            raise PermissionDenied(
                detail="You do not have permission to access this profile."
            )

        try:
            author = Author.objects.get(author=self.request.user)
            return Blog.objects.filter(author=author)
        except Author.DoesNotExist:
            raise NotFound("Author does not exist.")
