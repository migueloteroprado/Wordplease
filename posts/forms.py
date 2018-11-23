import datetime
from django import forms
from django.forms import DateTimeInput

from blogs.models import Blog
from posts.models import Post
from project.settings import DATETIME_INPUT_FORMATS


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['blog', 'title', 'summary', 'body', 'image', 'video', 'categories', 'pub_date']
        #widgets = {
        #    'pub_date': DateTimeInput(attrs={'type': 'text'})
        #}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author=user)
