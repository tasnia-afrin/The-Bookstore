from rest_framework import permissions
from mainapp.models import CustomUser


class AuthorReadPermission(permissions.BasePermission):
    message = "Only an AUTHOR can see the view"

    def has_permission(self, request, view):
        if request.user.is_authenticated and  request.user.user_type == "author":
            return True
        return False

class AuthorWritePermission(permissions.BasePermission):
    message = "Only an AUTHOR can edit the object"

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if request.user.is_authenticated and request.user.user_type == "author":
                return True
        return False


class ReaderReadPermission(permissions.BasePermission):
    message = "Only a READER can see the view"

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == "reader":
            return True
        return False


class ReaderWritePermission(permissions.BasePermission):
    message = "Only a Reader can edit the object"

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            if request.user.is_authenticated and request.user.user_type == "reader":
                return True
        return False
