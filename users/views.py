from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, redirect
from django.views import View

from project.settings import ITEMS_PER_PAGE
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
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form })

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            # create user
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()


            django_login(request, new_user)
            welcome_url = request.GET.get('next', 'home')
            messages.success(request, 'User signed up successfully!')
            return redirect(welcome_url)

        return render(request, 'users/signup.html', {'form': form})

class UsersView(View):

    def get(self, request):

        user_list = User.objects.all().order_by(Lower('username'))

        # Pagination
        paginator = Paginator(user_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        users = paginator.get_page(page)

        return render(request, 'users/users.html', {'users': users})
