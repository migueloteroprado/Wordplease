from image_upload.models import Image
from rest_framework import serializers


class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Image
        fields = '__all__'
