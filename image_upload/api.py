from rest_framework import viewsets

from image_upload.models import Image
from image_upload.permission import ImageUploadPermission
from image_upload.serializers import ImageUploadSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):

    permission_classes = [ImageUploadPermission]
    queryset = Image.objects.select_related('author').all()
    serializer_class = ImageUploadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
