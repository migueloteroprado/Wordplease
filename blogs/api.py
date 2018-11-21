from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet

from blogs.models import Blog
from blogs.serializers import BlogListSerializer, BlogSerializer
from posts.models import Post
from posts.serializers import PostListSerializer
from project.utils import CaseInsensitiveOrderingFilter


class BlogsViewSet(ModelViewSet):

    queryset = Blog.objects.select_related('owner').all()
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter]
    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name']
    ordering_fields = ['name']
    ordering = ['name']


    def get_serializer_class(self):
        return BlogListSerializer if self.action == 'list' else BlogSerializer

class BlogPostsAPIView(APIView):

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        posts = Post.objects.prefetch_related('categories').select_related('author').filter(author=user.id)
        for post in posts:
            print(post)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

