from rest_framework import serializers
from rest_framework.exceptions import APIException

from blogs.models import Blog
from blogs.serializers import BlogListSerializer
from categories.serializers import CategoryListSerializer
from posts.models import Post


class BlogNotFoundException(APIException):

    status_code = 404


class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'image', 'summary', 'pub_date']


class PostSerializer(PostListSerializer):

    blog = BlogListSerializer(read_only=True)

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'author', 'blog']

    def validate(self, data):
        # check if blog exists
        #try:
        #    blog_id = self.context.get('view').kwargs.get('parent_lookup_blogs')
        #    blog = Blog.objects.get(pk=blog_id)
        #    return data
        #except:
        #    raise serializers.ValidationError({'detail': 'Blog not found'})

        # check if blog exists and belongs to user
        try:
            blog_id = self.context.get('view').kwargs.get('parent_lookup_blogs')
            blog = Blog.objects.get(pk=blog_id)
        except:
            raise serializers.ValidationError({'detail': 'Blog not found'})
        user = self.context.get('request').user
        if blog.author == user or user.is_superuser:
            return data
        raise serializers.ValidationError({'detail': 'Blog doesn\'t belong to user'})

    def get_fields(self):
        fields = super(PostSerializer, self).get_fields()
        if self.context.get('view').action == 'retrieve':
            fields['categories'] = CategoryListSerializer(read_only=True, many=True)
        return fields

