# Generated by Django 4.2.1 on 2023-05-24 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0042_alter_shippingaddress_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='total_price',
            field=models.FloatField(default=1, verbose_name='Общая стоимость'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество'),
        ),
    ]
