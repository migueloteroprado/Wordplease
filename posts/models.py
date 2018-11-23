from django.contrib.auth.models import User
from django.db import models

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):

    PUBLISHED = 'PUB'
    DRAFT = 'DFT'

    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=3, choices=STATUS, default=PUBLISHED)
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())
