# Generated by Django 4.2.1 on 2023-05-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0041_alter_shippingaddress_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Города'),
        ),
    ]
