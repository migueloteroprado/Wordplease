# Generated by Django 2.1.3 on 2018-11-18 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20181118_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='author',
        ),
    ]
