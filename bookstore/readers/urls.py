from django.urls import path
from .views import ReaderProfileView


urlpatterns = [
    path(
        "profile",
        ReaderProfileView.as_view(),
        name="reader-profile",
    ),
]
