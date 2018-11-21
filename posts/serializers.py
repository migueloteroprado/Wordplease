from rest_framework import serializers

from categories.serializers import CategoryListSerializer
from posts.models import Post
from users.serializers import UserListSerializer


class PostListSerializer(serializers.ModelSerializer):

    author = UserListSerializer(read_only=True)
    categories = CategoryListSerializer(read_only=True, many=True)

    class Meta:

        model = Post
        fields = ['id', 'title', 'image', 'author', 'categories']
        read_only_fields = ['author']

class PostSerializer(PostListSerializer):

    author = UserListSerializer()

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
