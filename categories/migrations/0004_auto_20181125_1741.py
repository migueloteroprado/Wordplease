# Generated by Django 2.1.3 on 2018-11-25 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='pub_date',
            new_name='creation_date',
        ),
    ]
