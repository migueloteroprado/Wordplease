from rest_framework import serializers

from categories.models import Category


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


