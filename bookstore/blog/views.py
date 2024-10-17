from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import generics

from .models import *
from .serializers import *
from mainapp.models import CustomUser


class GlobalBlogListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(view_permission="global")

class PublicBlogListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(view_permission="public")


class AuthorBlogListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer

    def get_queryset(self):
        user: CustomUser = self.kwargs.get("id", None)

        if user is None:
            return HttpResponseNotFound("Author not found.")

        try:
            author: Author = Author.objects.get(author=user)
            return Blog.objects.filter(author=author)
        except Author.DoesNotExist:
            raise NotFound(detail="Author does not exist.")
