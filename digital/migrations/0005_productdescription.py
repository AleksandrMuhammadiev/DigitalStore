# Generated by Django 4.2 on 2023-05-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0004_gallery_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=255, verbose_name='Название параметра')),
                ('parameter_info', models.CharField(max_length=255, verbose_name='Описание параметра')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='digital.product')),
            ],
            options={
                'verbose_name': 'Описание товара',
                'verbose_name_plural': 'Описание товаров',
            },
        ),
    ]
