# Generated by Django 2.2 on 2019-04-11 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20190411_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 12, 51, 36, 472934), null=True),
        ),
    ]
