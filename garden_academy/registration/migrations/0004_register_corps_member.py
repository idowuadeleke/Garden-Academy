# Generated by Django 2.2 on 2019-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20190411_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='corps_member',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
