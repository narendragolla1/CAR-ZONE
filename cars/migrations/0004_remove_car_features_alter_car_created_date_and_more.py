# Generated by Django 4.1.5 on 2023-01-07 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_created_date_alter_car_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 7, 7, 0, 57, 677655)),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
