# Generated by Django 2.1.3 on 2019-03-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantlocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
