from django.shortcuts import get_object_or_404
from rest_framework import serializers

from blogs.models import Blog
from blogs.serializers import BlogListSerializer
from categories.serializers import CategoryListSerializer
from posts.models import Post
from users.serializers import UserListSerializer


class PostListSerializer(serializers.ModelSerializer):

    # author = UserListSerializer(read_only=True)

    class Meta:

        model = Post
        #fields = ['id', 'blog', 'title', 'image', 'categories']
        fields = ['id', 'title', 'image', 'summary', 'pub_date']



class PostSerializer(PostListSerializer):

    #author = UserListSerializer()
    blog = BlogListSerializer(read_only=True)
    #categories = CategoryListSerializer(read_only=True, many=True)

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['author', 'blog']

    def validate(self, attrs):
        # check if blog exists and belongs to logged user
        blog = get_object_or_404(Blog, pk=self.context.get('view').kwargs.get('parent_lookup_blogs'))

        return attrs
