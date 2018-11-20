from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Blog(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    # Create slug automatically
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    # Method to create a blog automatically when a user is created
    @receiver(post_save, sender=User)
    def create_blog(sender, instance, created, **kwargs):
        if created:
            Blog.objects.create(owner=instance,
                                name='{0} {1}\'s Blog'.format(instance.first_name, instance.last_name),
                                description='{0} {1}\'s Blog'.format(instance.first_name, instance.last_name))

    # Method to update a blog automatically when a user is updated
    @receiver(post_save, sender=User)
    def save_blog(sender, instance, **kwargs):
        instance.blog.save()

