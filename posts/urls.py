from django.urls import path

from posts.views import PostListView, NewPostView, BlogView, PostDetailView

urlpatterns = [
    path('blogs/<slug:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('blogs/<slug:username>/', BlogView.as_view(), name='blog'),
    path('new-post/', NewPostView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
]
