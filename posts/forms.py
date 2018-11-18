from django import forms

from posts.models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'summary', 'body', 'image', 'categories', 'published']

