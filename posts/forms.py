from django import forms

from blogs.models import Blog
from posts.models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['blog', 'title', 'summary', 'body', 'image', 'video', 'categories', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author=user)
