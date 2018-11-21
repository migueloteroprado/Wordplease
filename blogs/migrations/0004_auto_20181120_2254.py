# Generated by Django 2.1.3 on 2018-11-20 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0003_auto_20181120_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]