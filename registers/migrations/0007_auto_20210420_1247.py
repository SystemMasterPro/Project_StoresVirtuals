# Generated by Django 3.0 on 2021-04-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0006_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='state',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='store',
            name='state',
            field=models.BooleanField(default=True, verbose_name='State'),
        ),
    ]
