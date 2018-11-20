from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.views import BlogListView
from users.api import UsersViewSet
from users.views import LoginView, LogoutView, SignupView

router = DefaultRouter()
router.register('users', UsersViewSet, base_name='users')

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='signup'),

    # API
    path('api/1.0/', include(router.urls)),
]
