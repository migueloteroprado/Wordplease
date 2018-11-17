from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
