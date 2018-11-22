from django.utils.text import slugify
from rest_framework import serializers

from blogs.models import Blog
from users.serializers import UserListSerializer


class BlogListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserListSerializer()

    url = serializers.HyperlinkedIdentityField(view_name='blog-detail', format='html')

    class Meta:

        model = Blog
        fields = ['id', 'url', 'name', 'author']
        read_only_fields = ['author', 'slug']


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = ['id', 'name', 'description', 'author']

    def get_fields(self, *args, **kwargs):
        fields = super(BlogSerializer, self).get_fields()
        view = self.context.get('view', None)
        if view and view.action in ['update', 'create']:
            fields['author'].read_only = True
        return fields

    def validate_name(self, value):
        slug = slugify(value)
        # validacion si estoy actualizando un blog
        if self.instance is not None and self.instance.slug != slug and Blog.objects.filter(slug=slug).exists():
            raise serializers.ValidationError("Blog '{0}' already exists".format(self.instance.name))

        # validacion si estoy creando un blog
        if self.instance is None and Blog.objects.filter(slug=slug).exists():
            raise serializers.ValidationError("Blog '{0}' already exists".format(value))

        return value
