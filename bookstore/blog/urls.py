from django.urls import path
from .views import GlobalBlogListView, PublicBlogListView


urlpatterns = [
    path(
        "global-blog-list",
        GlobalBlogListView.as_view(),
        name="global-blog-list",
    ),
    path(
        "public-blog-list",
        PublicBlogListView.as_view(),
        name="public-blog-list",
    ),
]
