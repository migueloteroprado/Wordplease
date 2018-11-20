from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from blogs.forms import BlogForm
from users.forms import SignupForm, LoginForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:  # si no existe el usuario con ese username/password
                messages.error(request, 'Wrong username or password')
            else:
                # si el usuario existe, tenemos que hacer login del usuario en la sesión
                django_login(request, user)
                welcome_url = request.GET.get('next', 'home')
                messages.success(request, 'Logged in succesfully')
                return redirect(welcome_url)

        return render(request, 'users/login.html', {'form': login_form})


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')


class SignupView(View):

    def get(self, request):
        user_form = SignupForm()
        blog_form = BlogForm()
        return render(request, 'users/signup.html', {'user_form': user_form, 'blog_form': blog_form })

    def post(self, request):
        user_form = SignupForm(request.POST)
        blog_form = BlogForm(request.POST)
        if user_form.is_valid() and blog_form.is_valid():
            # create user
            new_user = User()
            new_user.first_name = user_form.cleaned_data.get('first_name')
            new_user.last_name = user_form.cleaned_data.get('last_name')
            new_user.username = user_form.cleaned_data.get('username')
            new_user.email = user_form.cleaned_data.get('email')
            new_user.set_password(user_form.cleaned_data.get('password'))
            new_user.save()
            # save blog data
            new_blog = new_user.blog
            new_blog.name = blog_form.cleaned_data.get('name')
            new_blog.description = blog_form.cleaned_data.get('description')
            new_blog.save()

            messages.success(request, 'User signed up successfully!')
            user_form = SignupForm()
            blog_form = BlogForm()

        return render(request, 'users/signup.html', {'user_form': user_form, 'blog_form': blog_form})
