from rest_framework import serializers

from blogs.models import Blog
from users.serializers import UserListSerializer


class BlogListSerializer(serializers.HyperlinkedModelSerializer):

    owner = UserListSerializer(many=False)

    class Meta:

        model = Blog
        fields = ['id', 'name', 'owner']


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = ['id', 'name', 'description']
        read_only_fields = ['owner']
