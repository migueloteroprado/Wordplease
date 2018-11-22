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
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter]
    search_fields = ['title', 'summary', 'body']
    ordering_fields = ['title', 'pub_date']
    ordering = ['-pub_date']

    def get_queryset(self):
        blog_id = self.kwargs.get('parent_lookup_blogs')
        try:
            blog = Blog.objects.get(pk=blog_id)
            user = self.request.user
            if (user.is_authenticated and user == blog.author) or user.is_superuser:
                return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs'))
            return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs'), status=Post.PUBLISHED)
        except:
            raise BlogNotFoundException({'detail': 'Blog not found'})

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=self.kwargs.get('parent_lookup_blogs'))
        # set post blog and author. The author is the blog owner
        serializer.save(author=blog.author, blog=blog)
