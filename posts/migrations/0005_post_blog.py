# Generated by Django 2.1.3 on 2018-11-20 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20181120_2254'),
        ('posts', '0004_auto_20181118_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog'),
            preserve_default=False,
        ),
    ]
