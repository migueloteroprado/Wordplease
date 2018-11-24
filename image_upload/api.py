from rest_framework import viewsets

from image_upload.models import Image
from image_upload.permission import ImageUploadPermission
from image_upload.serializers import ImageUploadSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):

    permission_classes = [ImageUploadPermission]
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer

