from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer


class PostsViewSet(ModelViewSet):

    permission_classes = [PostPermission]

    def get_queryset(self):
        return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs'))

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=self.kwargs.get('parent_lookup_blogs'))
        serializer.save(author=self.request.user, blog=blog)


class PostListAPIView(NestedViewSetMixin, ModelViewSet):

    serializer_class = PostListSerializer
    queryset = Post.objects.all()
