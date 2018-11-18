from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)
