# Generated by Django 2.2 on 2019-04-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('number_of_delegates', models.CharField(max_length=200)),
                ('transaction_id', models.CharField(max_length=200)),
                ('invoice_number', models.CharField(max_length=200)),
                ('transaction_reference', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
    ]
