from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostsViewSet
from posts.views import PostListView, NewPostView, BlogView, PostDetailView

router = DefaultRouter()
router.register('posts', PostsViewSet, base_name='posts')

urlpatterns = [
    path('blogs/<slug:name>/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('', PostListView.as_view(), name='home'),

    # API
    path('api/1.0/', include(router.urls)),
]
