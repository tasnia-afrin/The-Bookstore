from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import generics
from mainapp.models import CustomUser
from mainapp.permissions import ReaderWritePermission
from .models import Reader
from .serializers import ReaderSerializer


class ReaderProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [ReaderWritePermission]
    serializer_class = ReaderSerializer

    def get_object(self):
        user: CustomUser = self.request.user

        if user.user_type != "reader":
            raise PermissionDenied(
                detail="You do not have permission to access this profile."
            )

        try:
            return Reader.objects.get(reader=user)
        except Reader.DoesNotExist:
            raise NotFound(detail="Reader profile not found.")
