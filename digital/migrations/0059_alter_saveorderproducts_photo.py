# Generated by Django 4.2.1 on 2023-05-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0058_alter_saveorderproducts_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveorderproducts',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображения'),
        ),
    ]
