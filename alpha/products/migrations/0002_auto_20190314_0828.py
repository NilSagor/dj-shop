# Generated by Django 2.1.7 on 2019-03-14 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=20),
        ),
    ]
