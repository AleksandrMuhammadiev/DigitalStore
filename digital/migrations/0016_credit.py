# Generated by Django 4.2 on 2023-05-05 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0015_alter_gallery_color_alter_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_price', models.FloatField(default=0, verbose_name='От какой стоимости')),
                ('month', models.IntegerField(default=0, verbose_name='Месяцы')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='digital.product')),
            ],
            options={
                'verbose_name': 'Товар в рассрочку',
                'verbose_name_plural': 'Товары в рассрочку',
            },
        ),
    ]
