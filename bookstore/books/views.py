from django.http import HttpResponseNotFound
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound


from .models import Book
from .serializers import BookSerializer
from mainapp.models import CustomUser
from authors.models import Author


# Create your views here.
class GlobalBookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(view_permission="global")


class PublicBooklistView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(view_permission="public")


class AuthorBookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

    def get_queryset(self):
        user: CustomUser = self.kwargs.get("id", None)

        if user is None:
            return HttpResponseNotFound("Author not found.")

        try:
            writer: Author = Author.objects.get(author=user)
            return Book.objects.filter(writer=writer)
        except Author.DoesNotExist:
            raise NotFound(detail="Author does not exist.")
