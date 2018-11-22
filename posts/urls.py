from django.urls import path
from posts.views import PostListView, NewPostView, PostDetailView


urlpatterns = [
    path('blogs/<slug:name>/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('', PostListView.as_view(), name='home'),
]
