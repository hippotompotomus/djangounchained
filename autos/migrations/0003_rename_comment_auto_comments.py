# Generated by Django 3.2.5 on 2022-09-08 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_rename_name_auto_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='comment',
            new_name='comments',
        ),
    ]
