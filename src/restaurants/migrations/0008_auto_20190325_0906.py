# Generated by Django 2.1.3 on 2019-03-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20190325_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
