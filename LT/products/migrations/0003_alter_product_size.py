# Generated by Django 5.0 on 2023-12-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Размер'),
        ),
    ]
