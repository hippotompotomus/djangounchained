# Generated by Django 3.2.5 on 2022-09-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='name',
            new_name='nickname',
        ),
    ]
