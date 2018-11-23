import datetime
from rest_framework.permissions import BasePermission

from posts.models import Post


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action in ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        now = datetime.datetime.now()
        return (view.action == 'retrieve' and obj.pub_date <= now) \
               or obj.author == request.user \
               or request.user.is_superuser
