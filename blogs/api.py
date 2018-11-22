from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from blogs.models import Blog
from blogs.permissions import BlogPermission
from blogs.serializers import BlogListSerializer, BlogSerializer
from posts.models import Post
from posts.serializers import PostListSerializer
from project.utils import CaseInsensitiveOrderingFilter


class BlogsViewSet(NestedViewSetMixin, ModelViewSet):

    queryset = Blog.objects.select_related('author').all()
    permission_classes = [BlogPermission]
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter]
    search_fields = ['author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ['name']
    ordering = ['name']

    def get_serializer_class(self):
        return BlogListSerializer if self.action == 'list' else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

