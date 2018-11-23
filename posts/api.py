from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer
from project.utils import CaseInsensitiveOrderingFilter


class BlogNotFoundException(APIException):

    status_code = 404


class PostsViewSet(ModelViewSet):

    permission_classes = [PostPermission]
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'summary', 'body']
    ordering_fields = ['title', 'pub_date']
    ordering = ['-pub_date']
    filter_fields = ['categories'] #'status', 'categories']

    def get_queryset(self):
        blog_id = self.kwargs.get('parent_lookup_blogs')
        try:
            blog = Blog.objects.get(pk=blog_id)
            user = self.request.user
            if (user.is_authenticated and user == blog.author) or user.is_superuser:
                return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs')).select_related('author').prefetch_related('categories')
            now = timezone.now()
            return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs'), pub_date__lte=now).select_related('author').prefetch_related('categories')
        except:
            raise BlogNotFoundException({'detail': 'Blog not found'})

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
#        pub_date = timezone.now() if serializer.validated_data.get('status') == Post.PUBLISHED else None
        blog = Blog.objects.get(pk=self.kwargs.get('parent_lookup_blogs'))
        # set post blog and author. The author is the blog owner
        serializer.save(author=blog.author, blog=blog, pub_date=pub_date)

#    def perform_update(self, serializer):
#        pub_date = timezone.now() if serializer.validated_data.get('status') == Post.PUBLISHED else None
#        serializer.save(pub_date=pub_date)

