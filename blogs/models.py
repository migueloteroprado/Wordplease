from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
