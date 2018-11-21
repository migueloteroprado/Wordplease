from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer


class PostsViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [PostPermission]

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

