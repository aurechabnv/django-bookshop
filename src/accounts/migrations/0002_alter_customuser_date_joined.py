# Generated by Django 4.1.2 on 2022-10-11 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 18, 40, 11, 667436)),
        ),
    ]
