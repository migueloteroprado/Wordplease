from django.urls import path

from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', SignupView.as_view(), name='signup'),
]
