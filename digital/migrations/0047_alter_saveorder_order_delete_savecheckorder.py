# Generated by Django 4.2.1 on 2023-05-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0046_alter_orderproduct_order_savecheckorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital.order'),
        ),
        migrations.DeleteModel(
            name='SaveCheckOrder',
        ),
    ]
