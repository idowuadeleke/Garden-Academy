# Generated by Django 2.2 on 2019-04-11 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_register_corps_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 11, 12, 46, 40, 266702), null=True),
        ),
    ]
