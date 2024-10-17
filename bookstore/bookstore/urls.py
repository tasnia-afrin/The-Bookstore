from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    #  path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
    path("authors/", include("authors.urls")),
    path("users/", include("users.urls")),
    path("blogs/", include("blog.urls")),
    path("readers/", include("readers.urls")),
]
