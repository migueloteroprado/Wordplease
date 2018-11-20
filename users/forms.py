from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if username != slugify(username):
            raise forms.ValidationError('Invalid Username \'{0}\'. It can only contain lowercase letters, numbers and hyphens'.format(username))
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User {0} already exists'.format(username))
        return username

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Passwords don\'t match')

