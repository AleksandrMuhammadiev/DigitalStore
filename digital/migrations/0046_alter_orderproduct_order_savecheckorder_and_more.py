# Generated by Django 4.2.1 on 2023-05-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0045_saveorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital.order', verbose_name='Заказ номер'),
        ),
        migrations.CreateModel(
            name='SaveCheckOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital.customer')),
            ],
        ),
        migrations.AlterField(
            model_name='saveorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='digital.savecheckorder'),
        ),
    ]
