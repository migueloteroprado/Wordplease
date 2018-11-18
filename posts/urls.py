from django.urls import path

from posts.views import PostListView, NewPostView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new-post', NewPostView.as_view(), name='new_post'),
]
