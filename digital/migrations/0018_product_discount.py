# Generated by Django 4.2 on 2023-05-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0017_alter_credit_from_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Скидка'),
        ),
    ]