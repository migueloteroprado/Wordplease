from django.urls import path, include
from rest_framework.routers import DefaultRouter

from image_upload.api import ImageUploadViewSet

router = DefaultRouter()
router.register('image_upload', ImageUploadViewSet)


urlpatterns = [

    # API
    path('api/1.0/', include(router.urls)),
]