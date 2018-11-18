from django.contrib.auth.models import User
from django.db import models

from categories.models import Category


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.published)
