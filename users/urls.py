from django.urls import path

from users.api import BlogListAPIView
from users.views import LoginView, LogoutView, SignupView, BlogListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='signup'),

    # API
    path('api/1.0/blogs/', BlogListAPIView.as_view(), name='blog_list_api')
]
