# Generated by Django 4.2 on 2023-05-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0018_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=1, verbose_name='Скидка'),
            preserve_default=False,
        ),
    ]
