from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):
    """
    Permissions for /api/1.0/blogs/<id>/posts/ endpoints
    """

    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (view.action == 'retrieve' and obj.pub_date <= timezone.now()) \
            or request.user == obj.author \
            or request.user.is_superuser


class PostListPermission(BasePermission):
    """
    Permissions for /api/1.0/posts/ list endpoint
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.pub_date <= timezone.now() \
            or request.user == obj.author \
            or request.user.is_superuser
