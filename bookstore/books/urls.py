from django.urls import path
from .views import GlobalBookListView, PublicBooklistView

urlpatterns = [
    path(
        "global-book-list",
        GlobalBookListView.as_view(),
        name="global-book-list",
    ),
    path(
        "public-book-list",
        PublicBooklistView.as_view(),
        name="public-book-list",
    ),
]
