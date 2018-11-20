from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['name', 'description']
        labels = {
            'name': 'Blog Name',
            'description': 'Blog Description'
        }
