# Generated by Django 2.1.3 on 2018-11-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20181120_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
    ]