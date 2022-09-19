# Generated by Django 3.2.5 on 2022-09-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_rename_pic_ad_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]