# Generated by Django 4.2.1 on 2023-05-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0034_alter_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='color',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='color_name',
        ),
        migrations.AddField(
            model_name='product',
            name='color_name',
            field=models.CharField(blank=True, default='Белый', max_length=100, null=True, verbose_name='Цвет'),
        ),
    ]