from rest_framework import serializers

from blogs.models import Blog
from users.serializers import UserListSerializer


class BlogListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserListSerializer(many=False)

    url = serializers.HyperlinkedIdentityField(view_name='blogs-detail', format='html')

    class Meta:

        model = Blog
        fields = ['id', 'url', 'name', 'author']


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = ['id', 'name', 'description', 'author']
        read_only_fields = ['author']
