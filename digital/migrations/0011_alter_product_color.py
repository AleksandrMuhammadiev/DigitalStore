# Generated by Django 4.2 on 2023-05-05 10:21

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0010_alter_gallery_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='', image_field='images', max_length=18, samples=None, verbose_name='Цвет'),
        ),
    ]
