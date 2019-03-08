# Generated by Django 2.1.3 on 2018-11-25 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='last_modification',
            field=models.DateTimeField(auto_now=True),
        ),
    ]