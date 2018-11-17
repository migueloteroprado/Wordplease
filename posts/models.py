from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(blank=True, null=True)
    published = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

