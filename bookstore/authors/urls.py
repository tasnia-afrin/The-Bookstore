from django.urls import path
from .views import (
    AuthorListView,    
    AuthorBookListCreateView,
    AuthorProfileView,
    AuthorBlogListCreateView,
)
from blog.views import AuthorBlogListView
from books.views import AuthorBookListView


urlpatterns = [
    path(
        "profile",
        AuthorProfileView.as_view(),
        name="author-profile",
    ),
    path(
        "author-list",
        AuthorListView.as_view(),
        name="author-list",
    ),
    path(
        "author-list/<int:id>/books",
        AuthorBookListView.as_view(),
        name="author-book-list",
    ),
    path(
        "author-list/<int:id>/blogs",
        AuthorBlogListView.as_view(),
        name="author-blog-list",
    ),
    path(
        "profile/books",
        AuthorBookListCreateView.as_view(),
        name="author-book-listcreate",
    ),
    path(
        "profile/blogs",
        AuthorBlogListCreateView.as_view(),
        name="author-blog-listcreate",
    ),
]
