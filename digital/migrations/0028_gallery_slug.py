# Generated by Django 4.2.1 on 2023-05-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0027_gallery_color_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
