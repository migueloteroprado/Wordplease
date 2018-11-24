from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
